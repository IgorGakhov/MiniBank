from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    BigInteger,
    String,
    DateTime,
    Date,
    Numeric,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import ENUM

from src.infrastructure.database.engine import Base
from .enums import AccountTypesEnum


class AbstractAccount(Base):
    __abstract__ = True


class IndividualAccount(AbstractAccount):
    __tablename__ = "individual_accounts"

    id = Column(BigInteger, primary_key=True, index=True)
    number = Column(String(20))
    expiration = Column(Date)
    secret = Column(String(3))
    balance = Column(Numeric(2), default=0)
    currency_id = Column(Integer, ForeignKey("currencies.id"))
    type = Column(  # type: ignore
        ENUM(AccountTypesEnum), nullable=False, default=AccountTypesEnum.debit
    )
    date_create = Column(DateTime, default=datetime.utcnow)  # type: ignore
    date_modify = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)  # type: ignore
    date_last_use = Column(DateTime)

    currency = relationship("Currency")
    owner_id = Column(BigInteger, ForeignKey("individual_customers.id"))
    owner = relationship("IndividualCustomer", back_populates="accounts")


class BusinessAccount(AbstractAccount):
    __tablename__ = "business_accounts"

    id = Column(BigInteger, primary_key=True, index=True)
    number = Column(String(20))
    expiration = Column(Date)
    secret = Column(String(3))
    balance = Column(Numeric(2), default=0)
    currency_id = Column(Integer, ForeignKey("currencies.id"))

    currency = relationship("Currency")
    owner_id = Column(BigInteger, ForeignKey("business_customers.id"))
    owner = relationship("BusinessCustomer", back_populates="accounts")
