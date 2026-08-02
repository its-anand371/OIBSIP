# BMI Calculator

**Oasis Infobyte Summer Internship Program**
**Track:** Python Programming | **Task 2** | **Beginner Tier**

## Objective

A command-line Python program that calculates a user's Body Mass Index (BMI)
from their weight and height, then classifies the result into a standard
health category.

## Technologies Used

- Python 3 (`input()`, basic arithmetic — no external libraries required)

## Features

- Prompts the user for weight (kg) and height (m) via the command line
- Calculates BMI using the standard formula: `BMI = weight / (height²)`
- Classifies the result into one of four categories:
  - Underweight (BMI < 18.5)
  - Normal (18.5 – 24.9)
  - Overweight (25 – 29.9)
  - Obese (BMI ≥ 30)
- Displays the BMI value rounded to 2 decimal places, alongside the category
- Input validation: rejects non-numeric input and zero/negative values, with
  a clear error message, and keeps re-prompting until valid input is given

## Usage

```bash
python BMI_Calculator.py
```

Example run:

```
--BMI CALCULATOR--
The weight of the person is : 70
Enter the value of height in meters : 1.75
Your BMI is : 22.86
Acc to the your weight and height by bmi farmula you are classified as : Normal
```

## How it Works (Design Notes)

- `get_positive_value_weight()` and `get_positive_value_height()` each loop
  until a valid positive number is entered, using `try` / `except ValueError`
  to catch non-numeric input and an `if number <= 0` check to catch
  zero/negative values.
- `calculate_bmi(weight, height)` applies the BMI formula.
- `classify_bmi(bmi)` maps the numeric BMI value to a health category using
  a simple `if` / `elif` chain.
- `main()` ties it all together: gets valid inputs, calculates, classifies,
  and prints the result.

## Project Structure

```
OIBSIP/Python-Task2-BMICalculator/
├── BMI_Calculator.py   # main application
└── README.md           # this file
```

---
*Submitted as part of the Oasis Infobyte Summer Internship Program (SIP).*
