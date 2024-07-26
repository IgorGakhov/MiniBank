from fastapi import APIRouter, Depends, Body, Query, status

from ...schemas import (
    IndividualCustomerCreate,
    BusinessCustomerCreate,
    IndividualCustomerPatch,
    BusinessCustomerPatch,
)
from ...service_layer.unit_of_work import AbstractUnitOfWork, SqlAlchemyUnitOfWork


router = APIRouter(prefix="/customers", tags=["Клиенты"])


@router.get(
    path="/individual",
    summary="Получение списка клиентов-физлиц",
)
async def get_individual_customers(
    page: int = Query(1, ge=1, description="Номер страницы"),
    limit: int = Query(20, gt=0, le=100, description="Лимит объектов на странице"),
    uow: AbstractUnitOfWork = Depends(SqlAlchemyUnitOfWork),
):
    async with uow:
        objs = await uow.individual_customers_repo.list(limit, page - 1)
    return objs


@router.get(
    path="/individual/{customer_id}",
    summary="Получение информации о клиенте-физлице по его идентификатору",
)
async def get_individual_customer_by_id(
    customer_id: int,
    uow: AbstractUnitOfWork = Depends(SqlAlchemyUnitOfWork),
):
    async with uow:
        obj = await uow.individual_customers_repo.get_by_id(customer_id)
    return obj


@router.post(
    path="/individual",
    summary="Регистрация клиента-физлица",
    status_code=status.HTTP_201_CREATED,
)
async def post_individual_customer(
    request: IndividualCustomerCreate = Body(),
    uow: AbstractUnitOfWork = Depends(SqlAlchemyUnitOfWork),
):
    async with uow:
        obj = await uow.individual_customers_repo.add(dict(request))
        await uow.commit()
    return obj


@router.patch(
    path="/individual",
    summary="Изменение клиента-физлица",
)
async def patch_individual_customer(
    request: IndividualCustomerPatch = Body(),
    uow: AbstractUnitOfWork = Depends(SqlAlchemyUnitOfWork),
):
    account_id = request.id
    request = dict(request)
    del request[account_id]
    async with uow:
        obj = await uow.individual_customers_repo.update(account_id, dict(request))
        await uow.commit()
    return obj


@router.delete(
    path="/individual/{customer_id}",
    summary="Удаление клиента-физлица",
)
async def delete_individual_customer(
    customer_id: int,
    uow: AbstractUnitOfWork = Depends(SqlAlchemyUnitOfWork),
):
    async with uow:
        await uow.individual_customers_repo.delete(customer_id)
        await uow.commit()


@router.get(
    path="/business",
    summary="Получение списка клиентов-юрлиц",
)
async def get_business_customers(
    page: int = Query(1, ge=1, description="Номер страницы"),
    limit: int = Query(20, gt=0, le=100, description="Лимит объектов на странице"),
    uow: AbstractUnitOfWork = Depends(SqlAlchemyUnitOfWork),
):
    async with uow:
        objs = await uow.business_customers_repo.list(limit, page - 1)
    return objs


@router.get(
    path="/business/{customer_id}",
    summary="Получение информации о клиенте-юрлице по его идентификатору",
)
async def get_business_customer_by_id(
    customer_id: int,
    uow: AbstractUnitOfWork = Depends(SqlAlchemyUnitOfWork),
):
    async with uow:
        obj = await uow.business_customers_repo.get_by_id(customer_id)
    return obj


@router.post(
    path="/business",
    summary="Регистрация клиента-юрлица",
    status_code=status.HTTP_201_CREATED,
)
async def post_business_customer(
    request: BusinessCustomerCreate = Body(),
    uow: AbstractUnitOfWork = Depends(SqlAlchemyUnitOfWork),
):
    async with uow:
        obj = await uow.business_customers_repo.add(dict(request))
        await uow.commit()
    return obj


@router.patch(
    path="/business",
    summary="Изменение клиента-юрлица",
)
async def patch_business_customer(
    request: BusinessCustomerPatch = Body(),
    uow: AbstractUnitOfWork = Depends(SqlAlchemyUnitOfWork),
):
    account_id = request.id
    request = dict(request)
    del request[account_id]
    async with uow:
        obj = await uow.business_customers_repo.update(account_id, dict(request))
        await uow.commit()
    return obj


@router.delete(
    path="/business/{customer_id}",
    summary="Удаление клиента-юрлица",
)
async def delete_business_customer(
    customer_id: int,
    uow: AbstractUnitOfWork = Depends(SqlAlchemyUnitOfWork),
):
    async with uow:
        await uow.business_customers_repo.delete(customer_id)
        await uow.commit()
