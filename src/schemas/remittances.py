from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from ..db.enums import CustomerType


class Remittance(BaseModel):
    id: int
    sender_id: int
    sender_type: CustomerType
    recipient_id: int
    recipient_type: CustomerType
    amount: float
    currency_id: int
    message: Optional[str] = None
    date_create: datetime


class RemittanceListItem(BaseModel):
    id: int
    sender_id: int
    sender_type: CustomerType
    recipient_id: int
    recipient_type: CustomerType
    amount: float
    currency_id: int
    date_create: datetime


class RemittancesList(BaseModel):
    content: Optional[List[RemittanceListItem]]
