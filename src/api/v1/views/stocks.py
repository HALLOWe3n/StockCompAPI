# Created by PyCharm Professional.
# User: romandemyanchuk
# Date: 6/27/20
# Time: 1:47 AM
# To change this template use File | Settings | File and Code Templates.

from fastapi import APIRouter

from ..models.stocks.stocks import StockModel

router = APIRouter()
stock = StockModel()


@router.get('/stocks')
async def stock_list() -> dict:
    return {'stocks': stock.get_stocks_list()}


@router.get('/stock/{name}')
async def stock_detail(symbol: str) -> dict:
    return {'stock': stock.get_stock_detail(symbol)}

