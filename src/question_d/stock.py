# === 1. Create the Stock class with private variables ===
class Stock:
    def __init__(self, symbol, company_name):  # Constructor
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):  # 2. Method to return symbol
        return self.__symbol

    def get_company_name(self):  # 3. Method to return company name
        return self.__company_name


def stock_purchase_history():
    stock1 = Stock("AAPL", "Apple Inc")
    stock2 = Stock("CAT", "Caterpillar")
    stock3 = Stock("EK", "Eastman Kodak")
    stock4 = Stock("GOOG", "Google")
    stock5 = Stock("MSFT", "Microsoft")

    # Return as a list
    return [stock1, stock2, stock3, stock4, stock5]