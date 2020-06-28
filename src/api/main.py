# Created by PyCharm Professional.
# User: romandemyanchuk
# Date: 11.06.2020
# Time: 19:17
# To change this template use File | Settings | File and Code Templates.

from fastapi import FastAPI

from src.api.db.queries.stocks import StockQueries
from src.api.v1.views import user, stocks
from src.api.db.base import Base, engine
from src.api.core.symbols_csv import export_symbols_data

app = FastAPI(
    title='StockCompsAPI',
    description='API Microservices stock application',
    version='0.0.1',
)

app.include_router(router=user.router, tags=['Users'], prefix='/api/v1')
app.include_router(router=stocks.router, tags=['Stocks'], prefix='/api/v1')


@app.on_event('startup')
def run_database():
    Base.metadata.create_all(engine)


# MARK:
# ----
# Uncomment if stock_table is empty!

# @app.on_event('startup')
def export_data_to_tables():
    use_cols = ['Symbol', 'Name', 'IPOyear', 'Sector', 'industry']
    data = export_symbols_data(name='companylist.csv', use_cols=use_cols)
    StockQueries().insert_symbols_stock_data(exported=data)
