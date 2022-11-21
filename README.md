# FUNX

> FIB LP 2022-202

# Build

To build the Parser, execute the following command:

```shell
antlr4 -Dlanguage=Python3 -no-listener -visitor Funx.g4
```

# TODO

- [x] Basic Operations (`+`, `-`, `*`, `/`, `%`)
- [ ] Booleans (`True`, `False`, `=`, `!=`, `>`, `<`, `>=`, `<=`)
    - [x] Types and Operations
    - [x] FIX ERROR: `True = True` -> `False`
    - [ ] FIX ERROR: `1=1 = True` -> `False` && `1=1 = 1=1` correct tree