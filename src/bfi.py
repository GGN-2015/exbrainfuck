# optimized brainfuck interpreter
import sys
import json
import time
from bfc import BrainfuckCompiler
import colors



class BrainfuckInterpreter:
    def __get_file(self, filename: str) -> str: # get all content in a file
        if filename[-5:] == ".exbf":
            return BrainfuckCompiler(filename).get() # just run exbf in string
        else:
            f = open(filename, "r", encoding="utf-8")
            return f.read()

    def __check_same_type(self, ope1: str, ope2: str) -> bool:
        for ope_set in [set(["+", "-"]), set(["<", ">"])]:
            if set([ope1, ope2]).issubset(ope_set):
                return True
        return False

    def __merge(self, line: str) -> str:
        dic = {"+": 0, "-": 0, "<": 0, ">": 0}
        for c in line:
            dic[c] += 1
        dic['+'] -= dic['-'] # delta move, delta sum
        dic['-']  = 0
        dic['>'] -= dic['<']
        dic['<']  = 0

        if dic['+'] != 0:
            return ("+%d" % dic['+']) if dic['+'] > 0 else str(dic["+"])
        if dic['>'] != 0:
            return (">%d" % dic['>']) if dic['>'] > 0 else ("<%d" % abs(dic[">"]))
        return ""

    def __get_optimized_code(self, source_code) -> list:
        arr = []
        source_code = [c for c in source_code if c in self.OPERATOR_SET]

        # merge same type operator
        for c in source_code:
            if len(arr) > 0 and self.__check_same_type(arr[-1][0], c):
                arr[-1] += c
            else:
                arr.append(c)

        # merge operator count
        for i in range(len(arr)):
            line = arr[i]
            if line[0] in ['+', '-', '<', '>']:
                arr[i] = self.__merge(line)
        return [x for x in arr if x != ""] # delete empty strings

    def __check_match(self, optimized_code: list) -> None:
        match_position  = {}
        stack           = []
        for i in range(len(optimized_code)):
            if optimized_code[i] == '[':
                stack.append(i)

            if optimized_code[i] == ']': # there must be match in stack
                if len(stack) == 0:
                    colors.error_log("error: ']' not match with '['.", 1)

                *stack, top = stack # delete stack top, and then match them
                match_position[top] = i
                match_position[i  ] = top
        
        if len(stack) != 0:
            colors.error_log("error: '[' is more than ']'.", 1)
        return match_position

    def __touch_memoty(self, pos: int) -> None:
        if pos < 0:
            colors.error_log("runtime error: access memory position %d." % pos, 1)
        
        if self.memory.get(pos) is None: # auto initialize to zero
            self.memory[pos] = 0

    def __init__(self, file_bf: str, initial_memory = {}) -> None:
        self.OPERATOR_SET   = ['+', '-', '<', '>', ',', '.', '[', ']'] # all operators
        self.source_code    = self.__get_file(file_bf)                 # input source code
        self.optimized_code = self.__get_optimized_code(self.source_code)
        self.match_position = self.__check_match(self.optimized_code)  # check the match of '[' and ']'
        self.initial_memory = initial_memory
        self.memory         = {}
        self.pointer        = 0 # memory pointer to use
        self.program_pos    = 0
        self.instr_cnt      = 0
    
    def __add(self, val: int): # add or sub
        self.__touch_memoty(self.pointer)
        self.memory[self.pointer] = (self.memory[self.pointer] + val) % 256

    def __set(self, val: int): # set the val of some memory
        self.__touch_memoty(self.pointer)
        self.memory[self.pointer] = val % 256

    def __get(self): # use the value of some memory
        self.__touch_memoty(self.pointer)
        return self.memory[self.pointer]

    def __deep_copy(self, dic: dict): # deep copy a dict, json.loads(json.dumps(...)) NOT available
        return {x: dic[x] for x in dic}

    def run(self):
        self.instr_cnt   = 0 # count the number of instruction used
        self.program_pos = 0
        self.pointer     = 0
        self.memory      = self.__deep_copy(self.initial_memory) # deep copy
        while True:
            if self.program_pos >= len(self.optimized_code): # normally terminated
                return (self.memory, self.pointer, self.instr_cnt)
            cmd = self.optimized_code[self.program_pos]

            if cmd[0] == '+': # deal with add instruction
                self.__add(int(cmd))
                self.program_pos += 1
                self.instr_cnt   += int(cmd) % 256

            if cmd[0] == '-': # deal with sub instruction
                self.__add(int(cmd))
                self.program_pos += 1
                self.instr_cnt   += (-int(cmd)) % 256

            if cmd[0] == '<': # move pointer left
                self.pointer -= int(cmd[1:])
                self.program_pos += 1
                self.instr_cnt   += int(cmd[1:])

            if cmd[0] == '>': # move pointer right
                self.pointer += int(cmd[1:])
                self.program_pos += 1
                self.instr_cnt   += int(cmd[1:])

            if cmd == ',': # input char
                self.__set(ord(sys.stdin.read(1)) % 256) # mod 256 ASCII
                self.program_pos += 1
                self.instr_cnt   += 1

            if cmd == '.': # output char
                print(chr(self.__get()), end="", flush=True)
                self.program_pos += 1
                self.instr_cnt   += 1

            if cmd == '[': # while loop
                val = self.__get()
                self.instr_cnt += 1

                if val == 0:
                    self.program_pos = self.match_position[self.program_pos] + 1
                else:
                    self.program_pos += 1

            if cmd == ']': # while loop end
                val = self.__get()
                self.instr_cnt += 1
                
                if val != 0:
                    self.program_pos = self.match_position[self.program_pos]
                else:
                    self.program_pos += 1
        


if __name__ == "__main__":
    argv_list = json.loads(json.dumps(sys.argv))
    if len(argv_list) not in [2, 3]:
        line1 = "usage: python3 \"%s\" <file.bf>" % sys.argv[0]
        line2 = "       python3 \"%s\" <file.bf> \"{initialized_memory}\" " % sys.argv[0]
        colors.error_log(line1 + "\n" + line2, 1)

    # get initialized_memory
    if len(argv_list) == 3:
        initialized_memory = eval(argv_list[2])
        colors.info_log(initialized_memory)

        if not isinstance(initialized_memory, dict):
            colors.error_log("error: initialized_memory should be dict type.", 1)
    else:
        initialized_memory = {}

    file_bf                      = str(argv_list[1])
    brainfuck_interpreter        = BrainfuckInterpreter(file_bf, initial_memory=initialized_memory)
    begin_time                   = time.time()
    final_memory, ptr, instr_cnt = brainfuck_interpreter.run()
    end_time                     = time.time()

    colors.info_log("done. instr_cnt = %d, time_cost = %.2f" % (instr_cnt, end_time - begin_time))
    colors.info_log("%s ptr = %d" % (str(final_memory), ptr))