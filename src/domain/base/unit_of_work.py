from src.infrastructure.database.interfaces.unit_of_work import AbstractUnitOfWork
from src.infrastructure.database.engine import async_session_maker
from .repositories import SqlAlchemyRepository


class SqlAlchemyUnitOfWork(AbstractUnitOfWork):

    def __init__(self):
        self.session_factory = async_session_maker

    async def __aenter__(self):

        from src.domain.accounts import (
            IndividualAccountsRepository,
            BusinessAccountsRepository,
        )
        from src.domain.currencies import CurrenciesRepository
        from src.domain.customers import (
            IndividualCustomersRepository,
            BusinessCustomersRepository,
        )
        from src.domain.remittances import RemittancesRepository

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
