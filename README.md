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
    - [x] Bool operators (and, or, not, xor)
  - [ ] Lists
    - [x] Basic declaration `[1, 2, 3, 4]`
    - [x] Variable indexing `a[0]`
    - [x] Slice `a[1:3]`
    - [x] Len, Max
    - [x] Concatenation (list+list | list+int | int+list)
    - [ ] Map, Filter, Unfold (High order functions :|)
  - [ ] I/O
  - [ ] Elseif
  - [ ] For Loop
  - [ ] Switch
