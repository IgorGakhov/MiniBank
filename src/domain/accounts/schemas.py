from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from .enums import AccountTypesEnum


class IndividualAccountCreate(BaseModel):
    owner_id: int
    currency_id: int
    type: AccountTypesEnum


class IndividualAccountPatch(BaseModel):
    id: int
    currency_id: int
    type: AccountTypesEnum


class IndividualAccount(BaseModel):
    id: int
    number: str
    balance: float
    currency_id: int
    date_create: datetime
    date_modify: datetime
    date_last_use: datetime


class IndividualAccountListItem(BaseModel):
    id: int
    number: str
    date_last_use: datetime


class IndividualAccountsList(BaseModel):
    content: Optional[List[IndividualAccountListItem]]


class BusinessAccountCreate(BaseModel):
    owner_id: int
    currency_id: int


class BusinessAccountPatch(BaseModel):
    id: int
    currency_id: int
    type: AccountTypesEnum


class BusinessAccount(BaseModel):
    id: int
    number: str
    balance: float
    currency_id: int
    date_create: datetime
    date_modify: datetime
    date_last_use: datetime


class BusinessAccountListItem(BaseModel):
    id: int
    number: str
    date_last_use: datetime


class BusinessAccountsList(BaseModel):
    content: Optional[List[BusinessAccountListItem]]
