# FUNX

> Joaquim Torra Garcia
>
> FIB LP 2022-2023
>
> https://github.com/gebakx/lp-funcions

Funx is an interpreted functional programming language written in ANTRL4 and Python.

## Build

Clone this repository to your local machine and use the following command to generate the Lexer and Parser.

```shell
antlr4 -Dlanguage=Python3 -no-listener -visitor Funx.g4
```

## Usage

Currently there's 2 options to use Funx in your machine:

- CLI Interpreter
  > Run `python funx_cli.py` to start the Funx interpreter on your machine.
- Web Page
  > Run `flask --app funx_web.py run` to start the server. Using your favorite browser, go to `127.0.0.1:5000` and start using Funx.

Funx is designed to work always in the same way:

1. Declarations
2. Solve a single statement

This is how a Funx example would look like:

```funx
# Declare the function
Fibo n
{
    if n < 2 { n }
    (Fibo n-1) + (Fibo n-2)
}

# Run the function
Fibo 5
```

## Syntax

### Expressions

You can run any simple expression with numbers:

```funx
# addition
1 + 1
> 2

# multiplication
5 * 10
> 50
```

You can also perform some of these operations with Lists

```funx
1 + [2, 3, 4]
> [1, 2, 3, 4]

[1, 2, 3] + 4
> [1, 2, 3, 4]

[1] + [2]
> [1, 2]
```

Additionally, you can work with booleans

```funx
True and False
> False

True and True
> True

False or False
> False

not False
> True
```

> Here's the list of available operations:
>
> **binary ops:** +, -, \*, /, %, ^
>
> **locig ops:** =, !=, >, <, >=, <=, and, or, xor, not

### Lists

```funx
# Initialize a simple list and save it on a variable a
a <- [1, 2, 3, 4]

# Get a single value from the list
a[0]
> 1

# Get a sublist
a[1:3]
> [2, 3]

# Initialize a ranged list
a <- [1..10]
a
> [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Variables

In Funx, variables **always** are named starting with a lowercase letter.

A variable is defined at the moment of it's assignment.

To assign a value to a variable we use `<-`:

```funx
a <- 3

b <- a + 4
```

### Conditionals

If-Then-Else functions don't need parenthesys

```funx
if expression
{

}
else
{

}
```

### Loops

Both loops, **while** and **for**, are available:

```funx
# While loop
a <- 3
while a > 0 {
    a <- a-1
}

# For loop
l <- [1, 2, 3, 4]
s <- 0
for x in l {
    s <- s + x
}
```

### Functions

Functions, in the other hand, are named starting with a capital letter.

This is an example of a function declaration:

```funx
# The function Suma receives 2 arguments
# x and y and adds them together
Suma x y {
    x + y
}
```

### Input/Output

We have some i/o ops that are rarely used.

`print x` will print the variable x on screen without returning the value

`input x` will wait for user input and assign it's value to the variable x
