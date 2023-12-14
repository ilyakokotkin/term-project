"""
This module defines the InvestmentPortfolio class, 
which manages investment operations for the main program.
"""
class InvestmentPortfolio:
    """
    A class to represent an investment portfolio.

    Attributes:
        portfolio_name (str): The name of the portfolio.
        investments (dict): A dictionary to store investment details.
        _balance (float): A private attribute to track the 
        total investment balance.
    """
    def __init__(self, name):
        """
        Constructs all the necessary attributes for the 
        InvestmentPortfolio object.

        Args:
            name (str): The name of the investment portfolio.
        Returns:
            nothing
        """
        self.portfolio_name = name
        self.investments = {}
        self._balance = 0

    def __str__(self):
        """
        Returns a string representation of the investment portfolio,
        including each stock and its value, and the total balance.
        """
        portfolio_details = [(f"-" * 20)]
        portfolio_details.append(f"Portfolio: '{self.portfolio_name}' \nBreakdown:")
        for stock, value in self.investments.items():
            portfolio_details.append(f"  - {stock}: {value:,.2f}")
        portfolio_details.append((f"-" * 20))
        portfolio_details.append(f"Total balance: {self._balance:,.2f}")
        return "\n".join(portfolio_details)

    def __getitem__(self, item):
        """
        Allows dictionary-like access to the investments.

        Args:
            item (str): The name of the investment.

        Returns:
            The amount of the specified investment or a not found message.
        """
        return self.investments.get(item, "Not found")

    def _update_balance(self):
        """
        A private method to update the portfolio balance based on the investments.
        
        Args:
            none
        Returns:
            nothing
        """

        self._balance = sum(self.investments.values())

    def add_investment(self, name, amount):
        """
        Adds a new investment to the portfolio.

        Args:
            name (str): The name of the investment.
            amount (float): The amount to be invested.
        Returns:
            nothing
        """
        self.investments[name] = amount
        self._update_balance()

    def remove_investment(self, name):
        """
        Removes an investment from the portfolio.

        Args:
            name (str): The name of the investment to be removed.
        Returns:
            nothing
        Raises:
            ValueError: If the investment name is not found in the portfolio.
        """
        if name in self.investments:
            del self.investments[name]
            self._update_balance()
        else:
            raise ValueError(f"InvalidInput: '{name}' investment name is not found")
    
    def save_to_file(self, file_name):
        """
        Saves the current state of the investment portfolio to the input file.

        Args:
            file_name (str): The name of the file to save the portfolio data.
        """
        with open(file_name, 'w') as file:
            for name, amount in self.investments.items():
                file.write(f"{name},{amount}\n")
