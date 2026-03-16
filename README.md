# Python Learning Exercises

A structured collection of Python programming exercises organized by concept, progressing from fundamentals to multi-concept projects. Each section builds on skills developed in previous sections.

## About This Repository

This repository documents my structured approach to mastering Python programming through multiple high-quality resources:

| Platform | Focus | Status |
|----------|-------|--------|
| [Codedex](https://www.codedex.io/) | Interactive Python fundamentals and projects | In Progress |
| [Python Crash Course, 3rd Edition](https://ehmatthes.github.io/pcc_3e/) | Introductory programming book by Eric Matthes (No Starch Press) | In Progress |
| Coursera | Academic approach to computer science and Python | Coming Soon |

## Repository Structure

Exercises are organized into numbered folders that reflect a logical learning progression. Within each folder, files are numbered to indicate recommended completion order.

```
00_projects/              Multi-concept exercises combining all skills learned
01_variables_and_math/    Fundamentals: variables, arithmetic, type conversion
02_conditionals/          Control flow: if/elif/else, logical operators
03_loops/                 Iteration: while loops, for loops, range(), loop control
04_modules/               Importing and using Python modules (random)
05_lists/                 List creation, indexing, slicing, methods, iteration
```

## Exercises

### 00 - Projects

Multi-concept exercises that combine skills from all previous sections.

| # | Exercise | Description | Concepts |
|---|----------|-------------|----------|
| 1 | [sorting_hat.py](00_projects/01_sorting_hat.py) | Hogwarts Sorting Hat quiz | Variables, accumulators (`+=`), input, conditionals |
| 2 | [FizzBuzz.py](00_projects/02_FizzBuzz.py) | The famous fizzbuzz test | Loops, Conditionals, Modulo operator (`%`), Logical ordering (checking 15 before 3 or 5) |

### 01 - Variables and Math

Covers variable assignment, arithmetic operators, exponents, user input, and type conversion.

| # | Exercise | Description | Concepts |
|---|----------|-------------|----------|
| 1 | [temperature.py](01_variables_and_math/01_temperature.py) | Fahrenheit to Celsius conversion | Variables, arithmetic operators |
| 2 | [bmi.py](01_variables_and_math/02_bmi.py) | Body Mass Index calculation | Exponents (`**`) |
| 3 | [hypotenuse.py](01_variables_and_math/03_hypotenuse.py) | Pythagorean theorem calculator | `input()`, `int()`, square roots |
| 4 | [currency.py](01_variables_and_math/04_currency.py) | Multi-currency to USD converter | Multiple inputs, type conversion |
| 5 | [report_card.py](01_variables_and_math/05_student_report_card.py) | What are the data types of variables? | Learning about `type()` |
| 6 | [f_string_name.py](01_variables_and_math/06_f_string_full_name.py) | Print your name including variables | Introducing `f' strings` |

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
| 3 | [detention.py](03_loops/03_detention.py) | Detention writing lines exercise | `range()` function testing with a `for` loop|
| 4 | [99_bottles.py](03_loops/04_99_bottles.py) | Writing all 99 bottles lyrics with 5 lines of code | `range()` functions but with reversed and with steps, f-strings and interpolation (`and`) |
| 5 | [snake_eyes.py](03_loops/05_Snake_eyes.py) | This simulates rolling two six-sided dice until both dice show 1 | `random` library import, `while` loop, and `randint()` function |


### 04 - Modules

Covers importing Python modules and using the `random` library.

| # | Exercise | Description | Concepts |
|---|----------|-------------|----------|
| 1 | [themagic8ball.py](04_modules/01_themagic8ball.py) | Magic 8-Ball simulator | `import random`, `randint()` |
| 2 | [snapple_random.py](04_modules/02_snapple_random.py) | Random Snapple bottle cap facts | `random` module, multi-branch selection |

### 05 - Lists

Covers list creation, indexing, negative indexing, slicing, built-in functions (`min()`, `max()`), list methods (`.append()`, `.remove()`, `.pop()`), and iterating over lists with `for` loops.

| # | Exercise | Description | Concepts |
|---|----------|-------------|----------|
| 1 | [todo_list.py](05_lists/01_todo_list.py) | To-do list with indexing and slicing | List syntax, indexing, negative indexing, slicing |
| 2 | [inventory.py](05_lists/02_inventory.py) | LEGO parts inventory analysis | `min()`, `max()` built-in functions |
| 3 | [reading_list.py](05_lists/03_reading_list.py) | Managing a reading list | `.append()`, `.remove()`, `.pop()` methods |
| 4 | [roadrip_karaoke.py](05_lists/04_roadrip_karaoke.py) | Road trip playlist printer | `for` loop, `range()`, `len()`, list iteration |
| 5 | [academy_awards.py](05_lists/05_academy_awards.py) | Adding things to a list using a list method | `.insert` list method |

## Skills Demonstrated

- **Data Types**: `int`, `float`, `str`, `list`
- **Operators**: Arithmetic (`+`, `-`, `*`, `/`, `**`), relational (`>`, `<`, `>=`, `==`), logical (`and`, `or`), modulo (`%`)
- **User Input**: `input()` with type conversion (`int()`, `float()`)
- **Control Flow**: `if`/`elif`/`else` conditional branching
- **Iteration**: `while` loops with counters, `for` loops with `range()` and `len()`
- **Lists**: Indexing, negative indexing, slicing, `.append()`, `.remove()`, `.pop()`, `min()`, `max()`
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
