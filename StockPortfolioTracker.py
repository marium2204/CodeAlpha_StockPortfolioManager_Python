import yfinance as yf

class StockPortfolioManager:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, symbol, amount):
        if symbol in self.stocks:
            self.stocks[symbol] += amount  
        else:
            self.stocks[symbol] = amount  

    def remove_stock(self, symbol):
        if symbol in self.stocks:
            del self.stocks[symbol]  

    def update_quantity(self, symbol, amount):
        if symbol in self.stocks:
            self.stocks[symbol] = amount  

    def fetch_latest_price(self, symbol):
        try:
            stock_data = yf.Ticker(symbol)
            latest_price = stock_data.history(period='1d')['Close'].iloc[-1]
            return latest_price
        except Exception as e:
            print(f"Error fetching price for {symbol}: {e}")
            return 0  

    def calculate_portfolio_value(self):
        total_value = 0
        for symbol, amount in self.stocks.items():
            price = self.fetch_latest_price(symbol)
            total_value += price * amount
        return total_value

def portfolio_tracker():
    portfolio = StockPortfolioManager()

    while True:
        symbol = input("Enter stock symbol (or 'done' to finish): ")
        if symbol.lower() == 'done':
            break
        try:
            amount = int(input(f"Enter the amount of shares for {symbol}: "))
            portfolio.add_stock(symbol, amount)
        except ValueError:
            print("Invalid amount. Please enter a number.")

    print("\nCurrent Stock Holdings:")
    for symbol, amount in portfolio.stocks.items():
        price = portfolio.fetch_latest_price(symbol)
        total_value = price * amount
        print(f"{symbol}: {amount} shares at ${price:.2f} each - Total Value: ${total_value:.2f}")

    total_portfolio_value = portfolio.calculate_portfolio_value()
    print(f"\nTotal Portfolio Value: ${total_portfolio_value:.2f}")

    update_symbol = input("\nEnter a stock symbol to update its quantity: ")
    new_amount = int(input(f"Enter the new amount of shares for {update_symbol}: "))
    portfolio.update_quantity(update_symbol, new_amount)

    remove_symbol = input("Enter a stock symbol to remove it from the portfolio: ")
    portfolio.remove_stock(remove_symbol)

    print("\nUpdated Stock Holdings:")
    for symbol, amount in portfolio.stocks.items():
        price = portfolio.fetch_latest_price(symbol)
        total_value = price * amount
        print(f"{symbol}: {amount} shares at ${price:.2f} each - Total Value: ${total_value:.2f}")

    total_portfolio_value = portfolio.calculate_portfolio_value()
    print(f"\nTotal Portfolio Value: ${total_portfolio_value:.2f}")

if __name__ == "__main__":
    portfolio_tracker()
