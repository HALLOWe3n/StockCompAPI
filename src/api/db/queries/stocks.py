# Created by PyCharm Professional.
# User: romandemyanchuk
# Date: 6/27/20
# Time: 2:19 AM
# To change this template use File | Settings | File and Code Templates.

import math
import typing
import pandas as pd

from sqlalchemy.orm import Session

from ..base import engine, StockSymbol


class StockQueries:
    def __init__(self):
        self.model = StockSymbol
        self.session = Session(bind=engine)

    def insert_symbols_stock_data(self, exported: pd.DataFrame) -> None:
        """
        Bulk insert to database stock info
        :param exported: pandas dataframe exported from csv
        :return: None
        """
        self.session.bulk_save_objects([
            self.model(
                symbol=data[0],
                name=data[1],
                ipo_year=int(data[2]) if not math.isnan(data[2]) else None,
                sector=data[3] if not math.isnan(data[2]) else None,
                industry=data[4] if not math.isnan(data[2]) else None,
            )
            for data in zip(*[exported[column] for column in exported.columns.values])
        ], return_defaults=True)

        self.session.commit()

    def get_stocks(self) -> typing.List:
        stocks = self.session.query(self.model).all()
        return stocks

    def get_stock(self, symbol: str) -> object:
        stock = self.session.query(self.model).filter_by(symbol=symbol).first()
        return stock
