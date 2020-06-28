# Created by PyCharm Professional.
# User: romandemyanchuk
# Date: 6/27/20
# Time: 7:33 PM
# To change this template use File | Settings | File and Code Templates.

from src.api.db.queries.stocks import StockQueries


class StockModel:
    def __init__(self):
        self.query = StockQueries()

    def get_stocks_list(self) -> list:
        return self.query.get_stocks()

    def get_stock_detail(self, symbol: str) -> object:
        return self.query.get_stock(symbol)
