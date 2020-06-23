# Created by PyCharm Professional.
# User: romandemyanchuk
# Date: 11.06.2020
# Time: 19:17
# To change this template use File | Settings | File and Code Templates.

from fastapi import FastAPI

# from .views import user
from src.api.db.base import Base, engine
from src.api.v1.models.exports.symbols_csv import export_symbols_data


app = FastAPI(
    title='StockCompsAPI',
    description='API Microservices stock application',
    version='0.0.1',
)
# app.include_router(router=user.router, tags=['Users'], prefix='/api/v1')


@app.on_event('startup')
def run_database():
    Base.metadata.create_all(engine)


@app.on_event('startup')
def export_data_to_tables():
    export_symbols_data()
