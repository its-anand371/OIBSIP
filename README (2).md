# Random Password Generator

**Oasis Infobyte Summer Internship Program**
**Track:** Python Programming | **Task 3** | **Beginner Tier**

## Objective

A command-line Python tool that generates strong, random passwords based on
user-defined criteria: desired length and which character types to include.

## Technologies Used

- Python 3 — `random` and `string` modules (both built into Python, no
  external libraries required)

## Features

- Prompts for a desired password length, enforcing a minimum of 8 characters
- Lets the user choose which character types to include: uppercase letters,
  lowercase letters, numbers, and symbols
- Requires at least 2 character types to be selected before generating
- Input validation: rejects non-numeric or too-short lengths, and rejects
  fewer than 2 character types, with clear error messages and a retry loop
- Option to generate another password without restarting the program

## Usage

```bash
python Password_Generator.py
```

Example run:

```
=== Random Password Generator ===
Enter desired password length (minimum 8): 12

Choose which character types to include (answer y/n for each):
Include uppercase letters? (y/n): y
Include lowercase letters? (y/n): y
Include numbers? (y/n): y
Include symbols? (y/n): n

Generated password: 2DGucJz7F00J

Generate another password? (y/n): n
Goodbye!
```

## How it Works (Design Notes)

- `get_length()` loops until a valid integer of at least 8 is entered,
  using `try` / `except ValueError` to catch non-numeric input.
- `get_character_choices()` asks yes/no for each character type, then
  checks that at least 2 were chosen before continuing.
- `build_character_pool()` combines the chosen character sets from
  Python's built-in `string` module (`string.ascii_uppercase`,
  `string.ascii_lowercase`, `string.digits`, `string.punctuation`) into
  one pool to draw from.
- `generate_password()` uses `random.choice()` in a loop to pick random
  characters from that pool, one at a time, until reaching the requested
  length.
- The whole flow repeats inside a loop in `main()`, so the user can
  generate multiple passwords in one run.

## Project Structure

```
OIBSIP/Python-Task3-PasswordGenerator/
├── Password_Generator.py
└── README.md
```

---
*Submitted as part of the Oasis Infobyte Summer Internship Program (SIP).*
