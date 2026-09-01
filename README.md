# Calculator-via-DIY-Math-Interpreter

## Overview

This project is a small calculator built around a custom math interpreter. Instead of relying on Python's built-in `eval`, it breaks mathematical input into tokens, organizes those tokens into a syntax tree, and then evaluates the tree step by step.

This pattern is common in calculators, scripting languages, formula engines, and domain-specific languages. It makes it easier to support arithmetic precedence, parentheses, unary operations, and validation of invalid input.

## Tkinter Calculator UI

The project uses Python's `tkinter` package to build a lightweight calculator interface. The UI is designed to let a user type or click numbers and operators, then pass the full expression into the interpreter pipeline. The GUI is intentionally simple and focused on demonstrating how a front-end input can connect to a back-end expression evaluator.

In other words, the calculator interface handles user interaction, while the interpreter handles understanding and evaluating the math expression. This makes the project a good example of combining a basic graphical interface with parsing logic.

## How the Interpreter Works

### Lexer

The lexer is responsible for reading raw input text and turning it into meaningful tokens. It scans each character and groups them into recognized pieces such as numbers, operators, parentheses, and whitespace. For example, the input `3 + 4 * (2 - 1)` is converted into a sequence of token objects representing numbers and operators.

```
[(NUMBER: 3), (PLUS), (NUMBER: 4), (MULTIPLY), (LPAREN), (NUMBER: 2), (MINUS), (NUMBER: 1), (RPAREN)]
```

This stage is important because it simplifies parsing by converting raw text into structured data. The lexer also helps catch invalid characters early, which improves error handling.

### Parser

The parser takes the token stream produced by the lexer and builds an expression tree. It applies operator precedence and grouping rules so that multiplication and division are handled before addition and subtraction, and parentheses override normal ordering.

This stage is where the structure of an expression becomes explicit. For example, the parser can turn:

```
3 + 4 * (2 - 1)
```

into a tree of nodes representing the correct math structure, and correctly evaluate it as:

```
(3.0 + (4.0 * (2.0 - 1.0)))
```

### Interpreter

The interpreter walks the generated parse tree and evaluates it recursively. Each node type has a corresponding visit method that performs its operation, such as addition, subtraction, multiplication, division, or exponentiation.

Once evaluation is complete, the interpreter returns the final numeric result, which the calculator UI can display to the user.

## Unit Testing

The project includes unit tests for both the lexer and parser behavior. These tests were especially valuable because they helped reveal subtle bugs that were easy to miss during manual testing.

The lexer tests helped confirm that numbers, whitespace handling, and token generation were behaving correctly. The parser tests helped verify that arithmetic expressions were being constructed with the right precedence and structure, including nested expressions and multi-step operations.

These tests were critical in discovering issues such as incorrect token handling, expression grouping problems, and logic errors in how the parser composed nodes. The parser and lexer test commits represent a key part of the project’s learning process: they turned vague debugging into concrete, repeatable checks that improved confidence in the implementation.

## Requirements

To run this project, you need:

- Python ^3.8

## Running the Program

From the project root, run:

```bash
cd src
python calc.py
```

You can also run the tests with:

```bash
cd src
python -m unittest lexer_test parser_test interpreter_test
```

## Summary

This project demonstrates a practical way to build a calculator using a custom interpreter architecture: the user enters math, the lexer tokenizes it, the parser structures it, and the interpreter evaluates it. With a simple `tkinter` UI layered on top, the project becomes a clear, hands-on example of how interpreters and calculators work together.

Thanks to [@davidcallanan](https://github.com/davidcallanan) for the great [math interpreter tutorial](https://www.youtube.com/watch?v=88lmIMHhYNs&list=PLJp-g8uP8qlaZZiJ2gy-DiVbqXlWglrnP)
