from abc import ABC, abstractmethod

from ..adapters.repositories import (
    AbstractRepository,
    SqlAlchemyRepository,
    IndividualAccountsRepository,
    BusinessAccountsRepository,
    CurrenciesRepository,
    IndividualCustomersRepository,
    BusinessCustomersRepository,
    RemittancesRepository,
)
from ..db.base import async_session_maker


class AbstractUnitOfWork(ABC):
    currencies_repo: AbstractRepository
    individual_accounts_repo: AbstractRepository
    business_accounts_repo: AbstractRepository
    individual_customers_repo: AbstractRepository
    business_customers_repo: AbstractRepository
    remittances_repo: AbstractRepository

    @abstractmethod
    def __init__(self):
        raise NotImplementedError

    @abstractmethod
    async def __aenter__(self):
        raise NotImplementedError

    @abstractmethod
    async def __aexit__(self, *args):
        raise NotImplementedError

    @abstractmethod
    async def commit(self):
        raise NotImplementedError

    @abstractmethod
    async def rollback(self):
        raise NotImplementedError


class SqlAlchemyUnitOfWork(AbstractUnitOfWork):

    def __init__(self):
        self.session_factory = async_session_maker

    async def __aenter__(self):
        self.session = self.session_factory()
        self.currencies_repo: \
            SqlAlchemyRepository = CurrenciesRepository(self.session)
        self.individual_accounts_repo: \
            SqlAlchemyRepository = IndividualAccountsRepository(self.session)
        self.business_accounts_repo: \
            SqlAlchemyRepository = BusinessAccountsRepository(self.session)
        self.individual_customers_repo: \
            SqlAlchemyRepository = IndividualCustomersRepository(self.session)
        self.business_customers_repo: \
            SqlAlchemyRepository = BusinessCustomersRepository(self.session)
        self.remittances_repo: \
            SqlAlchemyRepository = RemittancesRepository(self.session)

    async def __aexit__(self, *args):
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
