from datetime import datetime

from sqlalchemy import Column, BigInteger, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from src.infrastructure.database.engine import Base


class AbstractCustomer(Base):
    __abstract__ = True


class IndividualCustomer(AbstractCustomer):
    __tablename__ = "individual_customers"

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String(100))
    patronymic = Column(String(100), nullable=True)
    surname = Column(String(100))
    email = Column(String(100), unique=True, index=True)
    phone = Column(String(50), unique=True)
    taxpayer_id_number = Column(String(50), unique=True)
    date_create = Column(DateTime, default=datetime.utcnow)  # type: ignore
    date_modify = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)  # type: ignore

    business_customers = relationship("BusinessCustomer", back_populates="owner")
    accounts = relationship("IndividualAccount", back_populates="owner")


class BusinessCustomer(AbstractCustomer):
    __tablename__ = "business_customers"

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String(200))
    owner_id = Column(BigInteger, ForeignKey("individual_customers.id"))
    taxpayer_id_number = Column(String(50), unique=True)
    main_state_reg_number = Column(String(50), unique=True)
    date_create = Column(DateTime, default=datetime.utcnow)  # type: ignore
    date_modify = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)  # type: ignore

    owner = relationship("IndividualCustomer", back_populates="business_customers")
    accounts = relationship("BusinessAccount", back_populates="owner")
