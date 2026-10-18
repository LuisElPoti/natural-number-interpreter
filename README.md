
# Natural Number Interpreter

A Python command-line application developed for the Omilia programming assignment.

The program takes a sequence of numbers separated by spaces, converts it into a complete number, and checks whether it is a valid Greek phone number. It also identifies different possible interpretations when the input is ambiguous.

## Requirements

- Python 3.9 or higher
- No external libraries required

## How to Run

Clone or download the repository and open a terminal in the project directory.

Run the application with:

```bash
python main.py
```

Enter a sequence of numbers separated by spaces. Each number can have up to 3 digits.

Type `exit` to close the program.

## Example

**Input:**

```text
2 10 69 30 6 6 4
```

**Output:**

```text
2106930664   VALID
210693664    INVALID
2106093664   VALID
21060930664  INVALID
```

## Implementation

The program is divided into three main parts:

- **Number interpretation:** Checks the input and joins the numbers into a single string, preserving leading zeros.
- **Phone number validation:** Checks whether the number has 10 or 14 digits and starts with one of the prefixes specified in the assignment.
- **Ambiguity detection:** Uses recursion and backtracking to generate different interpretations of the input.

For example, 30 6 can be interpreted as 306 or 36, while 69 can be interpreted as 69 or 609.

The backtracking algorithm explores these possibilities and combines them to generate different results. A set is used to avoid duplicate interpretations.

The ambiguity rules are based on the examples provided in the assignment, since not every possible case is explicitly defined.

## Project Structure

```text
natural-number-interpreter/
├── main.py
├── interpreter.py
├── validator.py
├── ambiguity.py
└── README.md
```

## Notes

- The program runs directly from the command line.
- No installation or build process is required.
- Input values must contain between 1 and 3 digits.
- Invalid inputs are handled with error messages.
- Each generated interpretation is checked against the Greek phone number validation rules.
