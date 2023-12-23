## `bf_io` manual

In `bf_io`, you can call basic subroutines defined in `bf_raw`, which provides convenient input/output functions for users to address integer input/output problems.

## endl.bf

> {\*} => {0}
>
> and output an `\n` onto the terminal.

## puti.exbf

> {a, \*, \*, \*, \*, \*, \*, \*, \*, \*, \*, \*, \*, \*} => {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
>
> and output the decimal format of `a`.

`puti.exbf` uses subroutines `bf_raw::copy.bf`，`bf_raw::eq0.bf`，`bf_raw::div.exbf`，`bf_raw::swap.bf`，`bf_raw::eq.exbf`，`bf_raw::not.exbf`，`bf_raw::add.bf`.
