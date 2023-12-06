from portfolio import InvestmentPortfolio

def read_portfolio_data(file_name):
    investments = {}
    try:
        with open(file_name, 'r') as file:
            for line in file:
                name, amount = line.split(',')
                investments[name.strip()] = float(amount.strip())
    except FileNotFoundError:
        print("File not found.")
    else:
        return investments

def main():
    portfolio_data_file = 'investments.txt'
    investments_data = read_portfolio_data(portfolio_data_file)

    if investments_data:
        portfolio = InvestmentPortfolio("My Portfolio")
        
        for name, amount in investments_data.items():
            portfolio.add_investment(name, amount)

        print(portfolio)
        print("Apple Investment Details:", portfolio['Apple'])  # Using __getitem__

if __name__ == "__main__":
    main()
