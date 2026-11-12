# Fibonacci Sequence Generator

A lightweight Python command-line tool that generates a 12-number Fibonacci sequence starting from any two integers provided by the user.

## Features
* **Custom Starting Points:** Generates a Fibonacci sequence from any two valid integers you enter.
* **Input Validation:** Ensures the input contains a comma, checks that exactly two values are provided, and prevents crashes from non-numeric entries.
* **Recursive Calculation:** Uses a clean recursive function to compute and print the first 12 numbers in the sequence.

## Prerequisites
* **Python 3.x** (No external libraries required—uses built-in Python features only).

## Installation & Setup
1. Clone this repository to your local machine:
   ```bash
   git clone git@github.com:yourusername/your-repo-name.git
   ```
2. Navigate into the project directory:
   ```bash
   cd your-repo-name
   ```

## Usage
Run the script from your terminal (replace `fibonacci.py` with your actual filename):
```bash
python fibonacci.py
```

### Example Output
```text
FIBONACCI NUMBERS
enter two numbers which you want to see the fibonacci numbers of(separate number by ','): 0, 1
0
1
1
2
3
5
8
13
21
34
55
89
```

## How It Works
1. The program prompts the user to enter two comma-separated integers (for example, `0, 1` or `5, 8`).
2. It validates the input using `split(',')` and a `try/except` block to catch invalid text or missing numbers.
3. Once valid integers are confirmed, it prints the initial two numbers and recursively calculates the next 10 numbers until 12 terms are displayed.
