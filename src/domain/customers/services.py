from typing import Any, Dict

from src.domain.base.unit_of_work import AbstractUnitOfWork


class IndividualCustomersService:

    async def get_all(
        self,
        limit: int,
        offset: int,
        uow: AbstractUnitOfWork,
    ):
        async with uow:
            objs = await uow.individual_customers_repo.list(limit, offset)
        return objs

    async def get_by_id(
        customer_id: int,
        uow: AbstractUnitOfWork,
    ):
        async with uow:
            obj = await uow.individual_customers_repo.get_by_id(customer_id)
        return obj

    async def add(
        self,
        customer: Dict,
        uow: AbstractUnitOfWork,
    ):
        async with uow:
            obj = await uow.individual_customers_repo.add(customer)
            await uow.commit()
        return obj

    async def patch(
        self,
        customer_id: int,
        data: Any,
        uow: AbstractUnitOfWork,
    ):
        async with uow:
            obj = await uow.individual_customers_repo.update(customer_id, data)
            await uow.commit()
        return obj

    async def delete(
        customer_id: int,
        uow: AbstractUnitOfWork,
    ):
        async with uow:
            await uow.individual_customers_repo.delete(customer_id)
            await uow.commit()


class BusinessCustomersService:

    async def get_all(
        self,
        limit: int,
        offset: int,
        uow: AbstractUnitOfWork,
    ):
        async with uow:
            objs = await uow.business_customers_repo.list(limit, offset)
        return objs

    async def get_by_id(
        customer_id: int,
        uow: AbstractUnitOfWork,
    ):
        async with uow:
            obj = await uow.business_customers_repo.get_by_id(customer_id)
        return obj

    async def add(
        self,
        customer: Dict,
        uow: AbstractUnitOfWork,
    ):
        async with uow:
            obj = await uow.business_customers_repo.add(customer)
            await uow.commit()
        return obj

    async def patch(
        self,
        customer_id: int,
        data: Any,
        uow: AbstractUnitOfWork,
    ):
        async with uow:
            obj = await uow.business_customers_repo.update(customer_id, data)
            await uow.commit()
        return obj

    async def delete(
        customer_id: int,
        uow: AbstractUnitOfWork,
    ):
        async with uow:
            await uow.business_customers_repo.delete(customer_id)
            await uow.commit()
