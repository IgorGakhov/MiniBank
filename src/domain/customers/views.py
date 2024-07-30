from fastapi import APIRouter, Depends, Body, Query, status

from src.domain.base.unit_of_work import AbstractUnitOfWork, SqlAlchemyUnitOfWork
from .schemas import (
    IndividualCustomerCreate,
    BusinessCustomerCreate,
    IndividualCustomerPatch,
    BusinessCustomerPatch,
)
from .services import IndividualCustomersService, BusinessCustomersService


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
    objs = await IndividualCustomersService().get_all(limit, page - 1, uow)
    return objs


@router.get(
    path="/individual/{customer_id}",
    summary="Получение информации о клиенте-физлице по его идентификатору",
)
async def get_individual_customer_by_id(
    customer_id: int,
    uow: AbstractUnitOfWork = Depends(SqlAlchemyUnitOfWork),
):
    obj = await IndividualCustomersService().get_by_id(customer_id, uow)
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
    obj = await IndividualCustomersService().add(dict(request), uow)
    return obj


@router.patch(
    path="/individual",
    summary="Изменение клиента-физлица",
)
async def patch_individual_customer(
    request: IndividualCustomerPatch = Body(),
    uow: AbstractUnitOfWork = Depends(SqlAlchemyUnitOfWork),
):
    customer_id = request.id
    request = dict(request)
    del request[customer_id]
    obj = await IndividualCustomersService().patch(customer_id, request, uow)
    return obj


@router.delete(
    path="/individual/{customer_id}",
    summary="Удаление клиента-физлица",
)
async def delete_individual_customer(
    customer_id: int,
    uow: AbstractUnitOfWork = Depends(SqlAlchemyUnitOfWork),
):
    await IndividualCustomersService().delete(customer_id, uow)


@router.get(
    path="/business",
    summary="Получение списка клиентов-юрлиц",
)
async def get_business_customers(
    page: int = Query(1, ge=1, description="Номер страницы"),
    limit: int = Query(20, gt=0, le=100, description="Лимит объектов на странице"),
    uow: AbstractUnitOfWork = Depends(SqlAlchemyUnitOfWork),
):
    objs = await BusinessCustomersService().get_all(limit, page - 1, uow)
    return objs


@router.get(
    path="/business/{customer_id}",
    summary="Получение информации о клиенте-юрлице по его идентификатору",
)
async def get_business_customer_by_id(
    customer_id: int,
    uow: AbstractUnitOfWork = Depends(SqlAlchemyUnitOfWork),
):
    obj = await BusinessCustomersService().get_by_id(customer_id, uow)
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
    obj = await BusinessCustomersService().add(dict(request), uow)
    return obj


@router.patch(
    path="/business",
    summary="Изменение клиента-юрлица",
)
async def patch_business_customer(
    request: BusinessCustomerPatch = Body(),
    uow: AbstractUnitOfWork = Depends(SqlAlchemyUnitOfWork),
):
    customer_id = request.id
    request = dict(request)
    del request[customer_id]
    obj = await BusinessCustomersService().patch(customer_id, request, uow)
    return obj


@router.delete(
    path="/business/{customer_id}",
    summary="Удаление клиента-юрлица",
)
async def delete_business_customer(
    customer_id: int,
    uow: AbstractUnitOfWork = Depends(SqlAlchemyUnitOfWork),
):
    await BusinessCustomersService().delete(customer_id, uow)
