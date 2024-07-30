from datetime import datetime, timedelta
import random
from typing import Any, Dict

from src.domain.base.unit_of_work import AbstractUnitOfWork
from .repositories import IndividualAccountsRepository, BusinessAccountsRepository


class IndividualAccountsService:

    async def get_all(
        self,
        limit: int,
        offset: int,
        uow: AbstractUnitOfWork,
    ):
        async with uow:
            objs = await uow.individual_accounts_repo.list(limit, offset)
        return objs

    async def get_by_id(
        account_id: int,
        uow: AbstractUnitOfWork,
    ):
        async with uow:
            obj = await uow.individual_accounts_repo.get_by_id(account_id)
        return obj

    async def add(
        self,
        account: Dict,
        uow: AbstractUnitOfWork,
    ):
        async with uow:
            obj = await uow.individual_accounts_repo.add(account)
            await uow.commit()
        return obj

    async def patch(
        self,
        account_id: int,
        data: Any,
        uow: AbstractUnitOfWork,
    ):
        async with uow:
            obj = await uow.individual_accounts_repo.update(account_id, data)
            await uow.commit()
        return obj

    async def delete(
        account_id: int,
        uow: AbstractUnitOfWork,
    ):
        async with uow:
            await uow.individual_accounts_repo.delete(account_id)
            await uow.commit()


class BusinessAccountsService:

    async def get_all(
        self,
        limit: int,
        offset: int,
        uow: AbstractUnitOfWork,
    ):
        async with uow:
            objs = await uow.business_accounts_repo.list(limit, offset)
        return objs

    async def get_by_id(
        account_id: int,
        uow: AbstractUnitOfWork,
    ):
        async with uow:
            obj = await uow.business_accounts_repo.get_by_id(account_id)
        return obj

    async def add(
        self,
        account: Dict,
        uow: AbstractUnitOfWork,
    ):
        async with uow:
            obj = await uow.business_accounts_repo.add(account)
            await uow.commit()
        return obj

    async def patch(
        self,
        account_id: int,
        data: Any,
        uow: AbstractUnitOfWork,
    ):
        async with uow:
            obj = await uow.individual_accounts_repo.update(account_id, data)
            await uow.commit()
        return obj

    async def delete(
        account_id: int,
        uow: AbstractUnitOfWork,
    ):
        async with uow:
            await uow.business_accounts_repo.delete(account_id)
            await uow.commit()


class CardData:

    @staticmethod
    async def generate_card_data():
        """Генерация данных карты (номер, CVV, срок действия)."""
        return {
            # "number": await __class__.generate_card_number(),
            "secret": __class__.generate_card_secret(),
            "expiration": __class__.generate_card_expiration(),
        }

    @staticmethod
    async def generate_card_number(
        individual_repo = IndividualAccountsRepository(),
        business_repo = BusinessAccountsRepository(),
    ):
        """Генерация номера карты."""
        unique = False
        while not unique:
            card_number = [random.randint(0, 9) for _ in range(16)]
            card_number = "".join(map(str, card_number))

            individual_exists = await individual_repo.get_by_number(card_number)
            business_exists = await business_repo.get_by_number(card_number)

            if not individual_exists and not business_exists:
                unique = True

        return card_number

    @staticmethod
    def generate_card_secret():
        """Генерация CVV (3 цифры)."""
        return "".join([str(random.randint(0, 9)) for _ in range(3)])

    @staticmethod
    def generate_card_expiration(years=5):
        """Генерация срока действия карты."""
        current_date = datetime.now()
        expiration_date = current_date + timedelta(days=years * 365)
        return expiration_date
