# Grammar of Exbrainfuck



## Quick Start

Here is an example program. The following program will output `hi!\n` to the screen after it finishes running:

```exbf
#RAW [-]
#RAW ++++++++++ ++++++++++ ++++++++++ ++++++++++ ++++++++++ ++++++++++ ++++++++++ ++++++++++ ++++++++++ ++++++++++ ++++ ; 104
OUT
#RAW + ; 105
OUT
#RAW [-]
#RAW ++++++++++ ++++++++++ ++++++++++ +++ ; 33
OUT
#RAW [-]
#RAW ++++++++++ ; 10
OUT
#RAW [-]
```

This program can be found at [../include/bf_demo/hi.exbf](../include/bf_demo/hi.exbf). If your current working directory is the root of the project, you can run it with `python3 src/bfi.py include/bf_demo/hi.exbf`.



## Alias Command

In exbrainfuck, we have defined aliases for some of the basic commands. If you want to use them in an `.exbf` program, please use their aliases.

| Raw Name | Alias Name |
| -------- | ---------- |
| +        | ADD        |
| -        | SUB        |
| <        | LSH        |
| >        | RSH        |
| [        | REP        |
| ]        | END        |
| ,        | INP        |
| .        | OUT        |



## Macro Command

Line begin with `#` will be regarded as a macro command.

| Command | Explanation                                                  | Example                  |
| ------- | ------------------------------------------------------------ | ------------------------ |
| `#RAW`  | append raw brainfuck scripts in the `.exbf` program.         | `#RAW [-]`               |
| `#USE`  | to include another `.bf` file or `.exbf` file as a subroutine of the `.exbf` program. | `#USE path/to/file.exbf` |

Please note that macro command `#USE` only searches for files using relative paths relative to the current `.exbf` file.

