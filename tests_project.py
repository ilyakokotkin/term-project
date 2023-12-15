"""
Unit tests for InvestmentPortfolio methods
"""

from portfolio import InvestmentPortfolio

if __name__ == "__main__":

    # Test for add_investment method

    test_portfolio = InvestmentPortfolio("Test Portfolio")
    test_portfolio.add_investment("Apple", 5000.00)
    assert "Apple" in test_portfolio.investments, \
        "Error: Apple should be in investments"
    assert test_portfolio.investments["Apple"] == 5000.00, \
        "Error: Apple amount should be 5000.00"

    # Test for remove_investment method

    test_portfolio = InvestmentPortfolio("Test Portfolio")
    test_portfolio.add_investment("Google", 7000.00)
    test_portfolio.remove_investment("Google")
    assert "Google" not in test_portfolio.investments, \
        "Error: Google should not be in investments after removal"

    print("All tests passed successfully!")
