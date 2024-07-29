from src.domain.base.repositories import SqlAlchemyRepository
from .models import IndividualAccount, BusinessAccount


class IndividualAccountsRepository(SqlAlchemyRepository):
    model = IndividualAccount


class BusinessAccountsRepository(SqlAlchemyRepository):
    model = BusinessAccount
