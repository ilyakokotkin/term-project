class InvestmentPortfolio:
    def __init__(self, name):
        self.portfolio_name = name
        self.investments = {}
        self._balance = 0

    def __str__(self):
        return f"Portfolio '{self.portfolio_name}' with balance: {self._balance}"

    def __getitem__(self, item):
        return self.investments.get(item, "Not found")

    def _update_balance(self):
        self._balance = sum(self.investments.values())

    def add_investment(self, name, amount):
        self.investments[name] = amount
        self._update_balance()

    def remove_investment(self, name):
        if name in self.investments:
            del self.investments[name]
            self._update_balance()
