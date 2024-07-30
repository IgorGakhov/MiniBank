from typing import Any, Dict

from src.domain.base.unit_of_work import AbstractUnitOfWork


class CurrenciesService:

    async def get_all(
        self,
        limit: int,
        offset: int,
        uow: AbstractUnitOfWork,
    ):
        async with uow:
            objs = await uow.currencies_repo.list(limit, offset)
        return objs

    async def get_by_id(
        currency_id: int,
        uow: AbstractUnitOfWork,
    ):
        async with uow:
            obj = await uow.currencies_repo.get_by_id(currency_id)
        return obj

    async def add(
        self,
        currency: Dict,
        uow: AbstractUnitOfWork,
    ):
        async with uow:
            obj = await uow.currencies_repo.add(currency)
            await uow.commit()
        return obj

    async def put(
        self,
        currency_id: int,
        data: Any,
        uow: AbstractUnitOfWork,
    ):
        async with uow:
            obj = await uow.currencies_repo.update(currency_id, data)
            await uow.commit()
        return obj

    async def delete(
        currency_id: int,
        uow: AbstractUnitOfWork,
    ):
        async with uow:
            await uow.currencies_repo.delete(currency_id)
            await uow.commit()
