from sqlalchemy import Column, Integer, String, Numeric

from ..base import Base


class AbstractCurrency(Base):
    __abstract__ = True


class Currency(AbstractCurrency):
    __tablename__ = "currencies"

    id = Column(Integer, primary_key=True, index=True)
    designation = Column(String(3), unique=True)
    usd_buy_price = Column(Numeric(2), nullable=False)
    usd_sale_price = Column(Numeric(2), nullable=False)
