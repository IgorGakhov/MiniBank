from typing import List, Optional

from pydantic import BaseModel


class CurrencyCreate(BaseModel):
    designation: str
    usd_buy_price: float
    usd_sale_price: float


class CurrencyPut(BaseModel):
    designation: str
    usd_buy_price: float
    usd_sale_price: float


class Currency(BaseModel):
    id: int
    designation: str
    usd_buy_price: float
    usd_sale_price: float


class CurrencyListItem(BaseModel):
    id: int
    designation: str
    usd_buy_price: float
    usd_sale_price: float


class CurrenciesList(BaseModel):
    content: Optional[List[CurrencyListItem]]
