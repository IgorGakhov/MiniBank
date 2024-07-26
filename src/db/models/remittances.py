from datetime import datetime

from sqlalchemy import Column, Integer, BigInteger, Text, Numeric, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import ENUM

from ..base import Base
from ..enums import CustomerType


class AbstractRemittance(Base):
    __abstract__ = True


class Remittance(AbstractRemittance):
    __tablename__ = "remittances"

    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(BigInteger, nullable=False)
    sender_type = Column(ENUM(CustomerType), nullable=False)  # type: ignore
    recipient_id = Column(BigInteger, nullable=False)
    recipient_type = Column(ENUM(CustomerType), nullable=False)  # type: ignore
    amount = Column(Numeric(2), nullable=False)
    currency_id = Column(Integer, ForeignKey("currencies.id"), nullable=False)
    message = Column(Text)
    date_create = Column(DateTime, default=datetime.utcnow)  # type: ignore

    currency = relationship("Currency")
