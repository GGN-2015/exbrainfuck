# exbrainfuck
Expanded Brainfuck Interpreter



## what is brainfuck

- https://en.wikipedia.org/wiki/Brainfuck



## source files

In our project, there are two types of source code files. One type is `.bf` files, and the other type is `.exbf` files. The `.bf` files adhere to the definition of the brainfuck language, while the `.exbf` files use our own defined set of macro-expanded brainfuck language syntax.

Grammar of exbrainfuck is listed in [./doc/grammar.md](./doc/grammar.md) .



## provided tools

`bfc.py`: exbf compiler, which compiles a `.exbf` file into a `.bf` file.

`bfi.py`: brainfuck interpreter, which can run not only `.bf` files but also `.exbf` files.



### how to use these tools

- The following command will generate a `.bf` file with the same name as `file.exbf` and save it in the same folder：

```bash
python3 bfc.py path/to/file.exbf
```

- The following command can be used to run a brainfuck program, whether it is an `.exbf` file or a `.bf` file:

```bash
python3 bfi.py path/to/file
```

- If you want the brainfuck program to be executed with non-zero initial memory content, you can use a command similar to the following, where `0:x` represents the position at index 0 in memory being filled with `x`:

```bash
python3 bfi.py path/to/file "{0:x,1:y,2:z,...}"
```



## special thanks

- https://esolangpark.vercel.app/ide/brainfuck
