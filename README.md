
# Investment Portfolio Management Program

This Python program is my term project for MET CS 521 course. It is designed to manage an investment portfolio, demonstrating various features of Python including classes, file handling, and data structures.

## Features

- Utilizes four container types: list, tuple, set, and dictionary.
- Implements iteration using a for loop.
- Includes conditional statements (if).
- Contains a try-except-else block for error handling.
- Features a user-defined function with parameters/arguments.
- Reads from an input file to load investment data.
- Includes a user-defined class `InvestmentPortfolio` with private/public attributes and methods.

## Files

- `portfolio.py`: Contains the `InvestmentPortfolio` class.
- `main.py`: The main program that uses the `InvestmentPortfolio` class.
- `investments.txt`: Sample input file with investment data.

## Usage

1. Ensure all files (`portfolio.py`, `main.py`, `investments.txt`) are in the same directory.
2. Run `main.py` to execute the program.

## Class `InvestmentPortfolio`

- **Attributes**
  - Private: `_balance`
  - Public: `investments`, `portfolio_name`
- **Methods**
  - Private: `_update_balance`
  - Public: `add_investment`, `remove_investment`
  - Magic: `__getitem__`
  - Others: `__init__`, `__str__`

The class manages the investment portfolio, tracks the balance, and allows adding and removing investments.

## Function `read_portfolio_data`

This function reads investment data from a file and returns it as a dictionary.

## Sample Input File Format

The `investments.txt` file should contain lines in the following format:

```
InvestmentName,Amount
```

Example:
```
Apple,5000.00
Google,7000.00
Tesla,3000.00
```

## Contribution

This is a basic version of an investment portfolio management program. Contributions to enhance its functionality are welcome.

## License

[MIT License](LICENSE.md)
