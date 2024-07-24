from fastapi import APIRouter, Body, Query

from ...schemas import (
    IndividualAccountCreate,
    BusinessAccountCreate,
    IndividualAccountPatch,
    BusinessAccountPatch,
)


router = APIRouter(prefix="/accounts", tags=["Банковские счета"])


@router.get(
    path="/individual",
    summary="Получение списка счетов физлиц",
)
async def get_individual_accounts(
    page: int = Query(1, ge=1, description="Номер страницы"),
    limit: int = Query(20, gt=0, le=100, description="Лимит объектов на странице"),
):
    pass


@router.get(
    path="/individual/{account_id}",
    summary="Получение информации о счете физлица по его идентификатору",
)
async def get_individual_account_by_id(account_id: int):
    pass


@router.post(
    path="/individual",
    summary="Регистрация счетов для физлица",
)
async def post_individual_account(
    request: IndividualAccountCreate = Body(),
):
    pass


@router.patch(
    path="/individual/{account_id}",
    summary="Изменение счета физлица",
)
async def patch_individual_account(
    request: IndividualAccountPatch = Body(),
):
    pass


@router.delete(
    path="/individual/{account_id}",
    summary="Удаление счета физлица",
)
async def delete_individual_account(account_id: int):
    pass


@router.get(
    path="/business",
    summary="Получение списка счетов юрлиц",
)
async def get_business_accounts(
    page: int = Query(1, ge=1, description="Номер страницы"),
    limit: int = Query(20, gt=0, le=100, description="Лимит объектов на странице"),
):
    pass


@router.get(
    path="/business/{account_id}",
    summary="Получение информации о счете юрлице по его идентификатору",
)
async def get_business_account_by_id(account_id: int):
    pass


@router.post(
    path="/business",
    summary="Регистрация счета для юрлица",
)
async def post_business_account(
    request: BusinessAccountCreate = Body(),
):
    pass


@router.patch(
    path="/business/{account_id}",
    summary="Изменение счета юрлица",
)
async def patch_business_account(
    request: BusinessAccountPatch = Body(),
):
    pass


@router.delete(
    path="/business/{account_id}",
    summary="Удаление счета юрлица",
)
async def delete_business_account(account_id: int):
    pass
