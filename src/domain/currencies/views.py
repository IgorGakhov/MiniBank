from fastapi import APIRouter, Depends, Body, Query, status

from src.domain.base.unit_of_work import AbstractUnitOfWork, SqlAlchemyUnitOfWork
from .schemas import CurrencyCreate, CurrencyPut
from .services import CurrenciesService


router = APIRouter(prefix="/currencies", tags=["Валюты"])


@router.get(
    path="/calculator",
    summary="Валютный калькулятор",
)
async def calculate_cache_by_currency(
    amount: float = Query(1, ge=0, description="Сумма"),
    from_cur: str = Query(description="Из валюты"),
    to_cur: str = Query(description="В валюту"),
):
    pass


@router.get(
    path="/",
    summary="Получение списка валют",
)
async def get_currencies(
    page: int = Query(1, ge=1, description="Номер страницы"),
    limit: int = Query(20, gt=0, le=100, description="Лимит объектов на странице"),
    uow: AbstractUnitOfWork = Depends(SqlAlchemyUnitOfWork),
):
    objs = await CurrenciesService().get_all(limit, page - 1, uow)
    return objs


@router.get(
    path="/{currency_id}",
    summary="Получение информации о валюте по её идентификатору",
)
async def get_currency_by_id(
    currency_id: int,
    uow: AbstractUnitOfWork = Depends(SqlAlchemyUnitOfWork),
):
    obj = await CurrenciesService().get_by_id(currency_id, uow)
    return obj


@router.post(
    path="/",
    summary="Создание записи валюты",
    status_code=status.HTTP_201_CREATED,
)
async def post_currency(
    request: CurrencyCreate = Body(),
    uow: AbstractUnitOfWork = Depends(SqlAlchemyUnitOfWork),
):
    obj = await CurrenciesService().add(dict(request), uow)
    return obj


@router.put(
    path="/",
    summary="Обновление информации о валюте",
)
async def put_currency(
    request: CurrencyPut = Body(),
    uow: AbstractUnitOfWork = Depends(SqlAlchemyUnitOfWork),
):
    currency_id = request.id
    obj = await CurrenciesService().put(currency_id, request, uow)
    return obj


@router.delete(
    path="/{currency_id}",
    summary="Удаление валюты",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_currency(
    currency_id: int,
    uow: AbstractUnitOfWork = Depends(SqlAlchemyUnitOfWork),
):
    await CurrenciesService().delete(currency_id, uow)
