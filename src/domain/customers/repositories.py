from src.domain.base.repositories import SqlAlchemyRepository
from .models import IndividualCustomer, BusinessCustomer


class IndividualCustomersRepository(SqlAlchemyRepository):
    model = IndividualCustomer


class BusinessCustomersRepository(SqlAlchemyRepository):
    model = BusinessCustomer
