from fastapi import APIRouter, Depends, Body, Query, status

from src.domain.base.unit_of_work import AbstractUnitOfWork, SqlAlchemyUnitOfWork
from .schemas import (
    IndividualAccountCreate,
    BusinessAccountCreate,
    IndividualAccountPatch,
    BusinessAccountPatch,
)
from .services import IndividualAccountsService, CardData


router = APIRouter(prefix="/accounts", tags=["Банковские счета"])


@router.get(
    path="/individual",
    summary="Получение списка счетов физлиц",
)
async def get_individual_accounts(
    page: int = Query(1, ge=1, description="Номер страницы"),
    limit: int = Query(20, gt=0, le=100, description="Лимит объектов на странице"),
    uow: AbstractUnitOfWork = Depends(SqlAlchemyUnitOfWork),
):
    objs = await IndividualAccountsService().get_all(limit, page - 1, uow)
    return objs


@router.get(
    path="/individual/{account_id}",
    summary="Получение информации о счете физлица по его идентификатору",
)
async def get_individual_account_by_id(
    account_id: int,
    uow: AbstractUnitOfWork = Depends(SqlAlchemyUnitOfWork),
):
    obj = await IndividualAccountsService().get_by_id(account_id, uow)
    return obj


@router.post(
    path="/individual",
    summary="Регистрация счета для физлица",
    status_code=status.HTTP_201_CREATED,
)
async def post_individual_account(
    request: IndividualAccountCreate = Body(),
    uow: AbstractUnitOfWork = Depends(SqlAlchemyUnitOfWork),
):
    card_data = await CardData.generate_card_data()
    account = {**dict(request), **card_data}
    obj = await IndividualAccountsService().add(account, uow)
    return obj


@router.patch(
    path="/individual",
    summary="Изменение счета физлица",
)
async def patch_individual_account(
    request: IndividualAccountPatch = Body(),
    uow: AbstractUnitOfWork = Depends(SqlAlchemyUnitOfWork),
):
    account_id = request.id
    request = dict(request)
    del request[account_id]
    obj = await IndividualAccountsService().patch(account_id, request, uow)
    return obj


@router.delete(
    path="/individual/{account_id}",
    summary="Удаление счета физлица",
)
async def delete_individual_account(
    account_id: int,
    uow: AbstractUnitOfWork = Depends(SqlAlchemyUnitOfWork),
):
    await IndividualAccountsService().delete(account_id, uow)


@router.get(
    path="/business",
    summary="Получение списка счетов юрлиц",
)
async def get_business_accounts(
    page: int = Query(1, ge=1, description="Номер страницы"),
    limit: int = Query(20, gt=0, le=100, description="Лимит объектов на странице"),
    uow: AbstractUnitOfWork = Depends(SqlAlchemyUnitOfWork),
):
    async with uow:
        objs = await uow.business_accounts_repo.list(limit, page - 1)
    return objs


@router.get(
    path="/business/{account_id}",
    summary="Получение информации о счете юрлице по его идентификатору",
)
async def get_business_account_by_id(
    account_id: int,
    uow: AbstractUnitOfWork = Depends(SqlAlchemyUnitOfWork),
):
    async with uow:
        obj = await uow.business_accounts_repo.get_by_id(account_id)
    return obj


@router.post(
    path="/business",
    summary="Регистрация счета для юрлица",
    status_code=status.HTTP_201_CREATED,
)
async def post_business_account(
    request: BusinessAccountCreate = Body(),
    uow: AbstractUnitOfWork = Depends(SqlAlchemyUnitOfWork),
):
    async with uow:
        obj = await uow.business_accounts_repo.add(dict(request))
        await uow.commit()
    return obj


@router.patch(
    path="/business",
    summary="Изменение счета юрлица",
)
async def patch_business_account(
    request: BusinessAccountPatch = Body(),
    uow: AbstractUnitOfWork = Depends(SqlAlchemyUnitOfWork),
):
    account_id = request.id
    request = dict(request)
    del request[account_id]
    async with uow:
        obj = await uow.business_accounts_repo.update(account_id, dict(request))
        await uow.commit()
    return obj


@router.delete(
    path="/business/{account_id}",
    summary="Удаление счета юрлица",
)
async def delete_business_account(
    account_id: int,
    uow: AbstractUnitOfWork = Depends(SqlAlchemyUnitOfWork),
):
    async with uow:
        await uow.business_accounts_repo.delete(account_id)
        await uow.commit()
