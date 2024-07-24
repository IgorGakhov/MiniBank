from fastapi import APIRouter, Body, Query

from ...schemas import (
    IndividualCustomerCreate,
    BusinessCustomerCreate,
    IndividualCustomerPatch,
    BusinessCustomerPatch,
)


router = APIRouter(prefix="/customers", tags=["Клиенты"])


@router.get(
    path="/individual",
    summary="Получение списка клиентов-физлиц",
)
async def get_individual_customers(
    page: int = Query(1, ge=1, description="Номер страницы"),
    limit: int = Query(20, gt=0, le=100, description="Лимит объектов на странице"),
):
    pass


@router.get(
    path="/individual/{customer_id}",
    summary="Получение информации о клиенте-физлице по его идентификатору",
)
async def get_individual_customer_by_id(customer_id: int):
    pass


@router.post(
    path="/individual",
    summary="Регистрация клиента-физлица",
)
async def post_individual_customer(
    request: IndividualCustomerCreate = Body(),
):
    pass


@router.patch(
    path="/individual/{customer_id}",
    summary="Изменение клиента-физлица",
)
async def patch_individual_customer(
    request: IndividualCustomerPatch = Body(),
):
    pass


@router.delete(
    path="/individual/{customer_id}",
    summary="Удаление клиента-физлица",
)
async def delete_individual_customer(customer_id: int):
    pass


@router.get(
    path="/business",
    summary="Получение списка клиентов-юрлиц",
)
async def get_business_customers(
    page: int = Query(1, ge=1, description="Номер страницы"),
    limit: int = Query(20, gt=0, le=100, description="Лимит объектов на странице"),
):
    pass


@router.get(
    path="/business/{customer_id}",
    summary="Получение информации о клиенте-юрлице по его идентификатору",
)
async def get_business_customer_by_id(customer_id: int):
    pass


@router.post(
    path="/business",
    summary="Регистрация клиента-юрлица",
)
async def post_business_customer(
    request: BusinessCustomerCreate = Body(),
):
    pass


@router.patch(
    path="/business/{customer_id}",
    summary="Изменение клиента-юрлица",
)
async def patch_business_customer(
    request: BusinessCustomerPatch = Body(),
):
    pass


@router.delete(
    path="/business/{customer_id}",
    summary="Удаление клиента-юрлица",
)
async def delete_business_customer(customer_id: int):
    pass
