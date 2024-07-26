from .base import SqlAlchemyRepository
from ...db.models import IndividualAccount, BusinessAccount


class IndividualAccountsRepository(SqlAlchemyRepository):
    model = IndividualAccount


class BusinessAccountsRepository(SqlAlchemyRepository):
    model = BusinessAccount
