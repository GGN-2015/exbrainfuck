import os
import sys



def error_log(msg, ret): # die and log on the stderr
    sys.stderr.write("%s\n" % msg)
    exit(ret)



class BrainfuckCompiler:
    def __init__(self, filename: str) -> None:
        self.source_code = open(filename, "r", encoding="utf-8").read()
        self.source_code = [line.strip() for line in self.source_code.split('\n')]
        self.filepath    = os.path.abspath(filename)
        self.filedirname = os.path.dirname(filename)

    def get(self) -> str:
        if self.filepath[-3:] == '.bf': # just read `.bf` in 
            return open(self.filepath, "r", encoding="utf-8").read()

        bf_code = []
        for line in self.source_code:

            if ';' not in line: # to keep there at least one comment
                line += ';'
            cmd, comment = line.split(';', 1)
            cmd          = cmd.strip()

            if cmd == "": # empty command
                continue

            if cmd.upper() == "ADD":
                bf_code.append("+")

            elif cmd.upper() == "SUB":
                bf_code.append("-")

            elif cmd.upper() == "LSH":
                bf_code.append("<")

            elif cmd.upper() == "RSH":
                bf_code.append(">")

            elif cmd.upper() == "INP":
                bf_code.append(",")

            elif cmd.upper() == "OUT":
                bf_code.append(".")

            elif cmd.upper() == "REP":
                bf_code.append("[")

            elif cmd.upper() == "END":
                bf_code.append("]")

            else:
                cmd, filename = cmd.split(maxsplit=1)

                assert cmd.upper() == '#USE'
                filename      = os.path.join(self.filedirname, filename)
                bf_code.append(BrainfuckCompiler(filename).get())

        return "".join(bf_code)



if __name__ == "__main__":
    if len(sys.argv) != 2:
        error_log("usage: python3 \"%s\" <file.exbf>" % sys.argv[0], 1)

    filename = sys.argv[1]
    if filename[-3:] == '.bf': # do not compile `.bf` file
        exit(0)
    assert filename[-5:] == ".exbf" # only compile .exbf

    bf_code  = BrainfuckCompiler(filename).get()
    outputf  = filename[:-5] + ".bf" 

    with open(outputf, "w", encoding="utf-8") as f: # output to same dir
        f.write(bf_code)