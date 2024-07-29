from abc import ABC, abstractmethod

from .repositories import AbstractRepository


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
