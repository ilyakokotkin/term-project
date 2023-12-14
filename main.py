"""
This is the main module for the Investment Portfolio Management Program.
It allows users to manage their investment portfolio through 
a command-line interface.
"""

from portfolio import InvestmentPortfolio

def read_portfolio_data(file_name):
    """
    Reads investment data from a file.

    Args:
        file_name (str): The name of the file to read investment data from.

    Returns:
        dict: A dictionary of investments.
    """
    investments = {}
    try:
        with open(file_name, 'r') as file:
            for line in file:
                name, amount = line.split(',')
                investments[name.strip()] = float(amount.strip())
    except FileNotFoundError:
        print("File not found. Please check the file's existence or path.")
    else:
        return investments
    
def get_user_input(prompt, data_type=float):
    """
    Gets user input and validates it.

    Args:
        prompt (str): The prompt to display to the user.
        data_type (type, optional): The type of data expected.

    Returns:
        The validated user input converted to the specified data type.
    """
    while True:
        try:
            return data_type(input(prompt))
        except ValueError:
            print(f"Please enter a valid {data_type.__name__}.")

def manage_portfolio(portfolio):
    """
    Manages the investment portfolio through user input by
    caling InvestmentPortfolio class methods.

    Args:
        portfolio (InvestmentPortfolio): The investment portfolio to manage.
    """
    while True:
        print("\n1. Add Investment\n2. Remove Investment\n3. View Portfolio\n4. Exit")
        choice = input("Choose an option: ")

        # Add investment
        if choice == '1':
            name = input("Enter investment name: ")
            amount = get_user_input("Enter amount (e.g., 5000.00): ")
            portfolio.add_investment(name, amount)
            print(f"Investment '{name}' added.")

        # Remove investment
        elif choice == '2':
            while True:
                try:
                    name = input("Enter investment name to remove: ")
                    portfolio.remove_investment(name)
                    print(f"Investment '{name}' removed.")
                    break
                except ValueError as e:
                    print(e)

        # View portfolio
        elif choice == '3':
            print(portfolio)

        # Save changes in input file and exit the program
        elif choice == '4':
            portfolio.save_to_file('investments.txt') 
            print("Portfolio changes saved. Exiting program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    portfolio_data_file = 'investments.txt'
    investments_data = read_portfolio_data(portfolio_data_file)

    portfolio = InvestmentPortfolio("My Portfolio")
    if investments_data:
        for name, amount in investments_data.items():
            portfolio.add_investment(name, amount)

    manage_portfolio(portfolio)