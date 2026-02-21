# Python Learning Exercises

A structured collection of Python programming exercises organized by concept, progressing from fundamentals to multi-concept projects. Each section builds on skills developed in previous sections.

## About This Repository

This repository documents my structured approach to mastering Python programming through multiple high-quality resources:

| Platform | Focus | Status |
|----------|-------|--------|
| [Codedex](https://www.codedex.io/) | Interactive Python fundamentals and projects | In Progress |
| Udemy | Specialized Python topics and real-world applications | Coming Soon |
| Coursera | Academic approach to computer science and Python | Coming Soon |

## Repository Structure

Exercises are organized into numbered folders that reflect a logical learning progression. Within each folder, files are numbered to indicate recommended completion order.

```
01_variables_and_math/    Fundamentals: variables, arithmetic, type conversion
02_conditionals/          Control flow: if/elif/else, logical operators
03_loops/                 Iteration: while loops, counters, loop control
04_modules/               Importing and using Python modules (random)
05_projects/              Multi-concept exercises combining all skills above
```

## Exercises

### 01 - Variables and Math

Covers variable assignment, arithmetic operators, exponents, user input, and type conversion.

| # | Exercise | Description | Concepts |
|---|----------|-------------|----------|
| 1 | [temperature.py](01_variables_and_math/01_temperature.py) | Fahrenheit to Celsius conversion | Variables, arithmetic operators |
| 2 | [bmi.py](01_variables_and_math/02_bmi.py) | Body Mass Index calculation | Exponents (`**`) |
| 3 | [hypotenuse.py](01_variables_and_math/03_hypotenuse.py) | Pythagorean theorem calculator | `input()`, `int()`, square roots |
| 4 | [currency.py](01_variables_and_math/04_currency.py) | Multi-currency to USD converter | Multiple inputs, type conversion |

### 02 - Conditionals

Covers `if`, `elif`, `else` statements, relational operators, and logical operators (`and`, `or`).

| # | Exercise | Description | Concepts |
|---|----------|-------------|----------|
| 1 | [grades.py](02_conditionals/01_grades.py) | Pass/fail grade checker | `if`/`else` |
| 2 | [ph_levels.py](02_conditionals/02_ph_levels.py) | pH scale classifier | `elif`, relational operators (`<`, `>`) |
| 3 | [highschool_usa.py](02_conditionals/03_highschool_usa.py) | Grade-to-classification mapping | Multiple `elif`, equality (`==`) |
| 4 | [restaurant_reviews.py](02_conditionals/04_restaurant_reviews.py) | Star rating classifier | `float` input, range comparisons |
| 5 | [the_cyclone.py](02_conditionals/05_the_cyclone.py) | Roller coaster eligibility check | Logical `and` operator |
| 6 | [seasons_of_the_year.py](02_conditionals/06_seasons_of_the_year.py) | Month-to-season mapper | Logical `or` operator |
| 7 | [planet_weights.py](02_conditionals/07_planet_weights.py) | Weight on different planets | Extended `elif` chains, `float` math |

### 03 - Loops

Covers `while` loops, loop conditions, counters, and loop termination.

| # | Exercise | Description | Concepts |
|---|----------|-------------|----------|
| 1 | [bank_pin.py](03_loops/01_bank_pin.py) | PIN validation with retry | `while` loop, input validation |
| 2 | [guess_the_number.py](03_loops/02_guess_the_number.py) | Number guessing game | `while` with counter, compound conditions (`and`) |

### 04 - Modules

Covers importing Python modules and using the `random` library.

| # | Exercise | Description | Concepts |
|---|----------|-------------|----------|
| 1 | [themagic8ball.py](04_modules/01_themagic8ball.py) | Magic 8-Ball simulator | `import random`, `randint()` |
| 2 | [snapple_random.py](04_modules/02_snapple_random.py) | Random Snapple bottle cap facts | `random` module, multi-branch selection |

### 05 - Projects

Multi-concept exercises that combine skills from all previous sections.

| # | Exercise | Description | Concepts |
|---|----------|-------------|----------|
| 1 | [sorting_hat.py](05_projects/01_sorting_hat.py) | Hogwarts Sorting Hat quiz | Variables, accumulators (`+=`), input, conditionals |

## Skills Demonstrated

- **Data Types**: `int`, `float`, `str`
- **Operators**: Arithmetic (`+`, `-`, `*`, `/`, `**`), relational (`>`, `<`, `>=`, `==`), logical (`and`, `or`)
- **User Input**: `input()` with type conversion (`int()`, `float()`)
- **Control Flow**: `if`/`elif`/`else` conditional branching
- **Iteration**: `while` loops with counters and compound exit conditions
- **Modules**: `import random`, `random.randint()`
- **Patterns**: Accumulator pattern, input validation, multi-branch selection

## Running the Exercises

Each file is a standalone Python script:

```bash
python3 01_variables_and_math/01_temperature.py
```

## Current Focus

- Python fundamentals and syntax
- Data structures and algorithms
- Problem-solving and computational thinking
- Building towards data science and bioinformatics applications

---

*This is a living repository that grows with my learning. All code represents my current understanding and will evolve as I advance through the curriculum.*
