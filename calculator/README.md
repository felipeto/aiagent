# Calculator App

This is a simple calculator application. It takes a mathematical expression as a command-line argument and evaluates it.  It uses a `Calculator` class to perform the calculation and a `render` function to display the result in a box.

## Files

*   `main.py`: The main entry point of the application. It handles user input, calls the calculator and render functions, and prints the result.
*   `pkg/calculator.py`:  Defines the `Calculator` class, which contains the logic for evaluating mathematical expressions. It supports addition, subtraction, multiplication, and division.
*   `pkg/render.py`: Defines the `render` function, which takes an expression and its result and formats it in a box for display.

## Usage

To run the calculator, execute `main.py` from the command line with the expression as an argument.

```bash
python main.py "<expression>"
```

Example:

```bash
python main.py "3 + 5 * 2"
```

## Example Output

Running the example command above will produce the following output:

```
┌─────────┐
│ 3 + 5 * 2 │
│           │
│ =        │
│           │
│ 13.0      │
└─────────┘
```
