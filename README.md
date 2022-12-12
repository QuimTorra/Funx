# FUNX

> Joaquim Torra Garcia
>
> FIB LP 2022-2023
>
> https://github.com/gebakx/lp-funcions

# Build

To build the Parser, execute the following command:

```shell
antlr4 -Dlanguage=Python3 -no-listener -visitor Funx.g4
```

# TODO

- [x] Basic Operations (`+`, `-`, `*`, `/`, `%`)
  - [x] Parenthesys
- [x] Variables
  - [x] Init to 0
  - [x] Assignment
  - [x] Global/Local Scope
- [x] Statements
  - [x] If / Else
  - [x] While
- [x] Functions
  - [x] Declaration
  - [x] Invocation
  - [x] Return
- [x] Comments
- [ ] CL Interpreter
  - [x] Flags
    - [x] --file [file].funx: Interpret from a `*.funx` file
    - [x] --view-tree: Allows you to view the AST
    - [x] --help: To see all the flags that can be used
  - [x] Functions
    - [x] :quit
    - [x] :clear
    - [x] :load
- [ ] Extensions
  - [x] Booleans (`True`, `False`, `=`, `!=`, `>`, `<`, `>=`, `<=`)
    - [x] Types and Operations
    - [ ] Bool operators (and, or, not)
    - [x] FIX ERROR: `True = True` -> `False`
    - [x] FIX ERROR: `1=1 = True` -> `False` && `1=1 = 1=1` correct tree
  - [ ] Elseif
  - [ ] For Loop
  - [ ] Switch
