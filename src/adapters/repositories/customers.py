from .base import SqlAlchemyRepository
from ...db.models import IndividualCustomer, BusinessCustomer


class IndividualCustomersRepository(SqlAlchemyRepository):
    model = IndividualCustomer


class BusinessCustomersRepository(SqlAlchemyRepository):
    model = BusinessCustomer
