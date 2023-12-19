# `bf_raw` manual

We promise that any complete program must guarantee the preservation of the pointer positions before and after execution. `bf_raw` is the most fundamental type of `brainfuck` subroutine. It implements basic functionalities of byte-level arithmetic (addition, subtraction, multiplication, division) and logic (AND, OR, NOT). **All arithmetic operations are performed modulo 256**.

## add.bf

> {a, b} => {a+b, 0}

**Regarding the notation interpretation:** `{a, b}` denotes that prior to program execution, the pointer points to the location containing the value `a`. The program guarantees that no modifications will be made to any position preceding `a`. After program execution, the value at the original  `a` position changes to `a+b`, and the value at the original  `b` position is set to zero.

## clr.bf

> {a} => {0}

## copy.bf

> {a, x, \*} => {a, a+x, 0}
>
> >  specially, when `x == 0`:
> >
> > {a, 0, *} => {a, a, 0}

## eq0.bf

> {a, \*, \*, \*} => {[a==0], 0, 0, 0}

**Regarding the notation interpretation:** The value of `[S]` is `1` if the condition specified by `S` is true; otherwise, it is `0`.

## mul.exbf

> {a, b, \*, \*} => {a\*b, 0, 0, 0}

`mul.exbf` uses subroutine `clr.bf` and `copy.bf`.

## not.exbf

> {a, \*, \*, \*} => {!a, 0, 0, 0}

**Regarding the notation interpretation:** `!a` is similar to the logical NOT operator in the C language. If the value of a is not zero, `!a` will be equal to `0`. Otherwise, `!a` will be equal to `1`.

`not.exbf` use `eq0.bf` as its directly implementation.

## sub.bf

> {a, b} => {a-b, 0}

