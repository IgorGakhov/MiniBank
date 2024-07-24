from fastapi import APIRouter, Body, Query

from ...schemas import CurrencyCreate, CurrencyPut


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
):
    pass


@router.get(
    path="/{currency_id}",
    summary="Получение информации о валюте по её идентификатору",
)
async def get_currency_by_id(currency_id: int):
    pass


@router.post(
    path="/",
    summary="Создание записи валюты",
)
async def post_currency(
    request: CurrencyCreate = Body(),
):
    pass


@router.put(
    path="/{currency_id}",
    summary="Обновление информации о валюте",
)
async def put_currency(
    request: CurrencyPut = Body(),
):
    pass


@router.delete(
    path="/{currency_id}",
    summary="Удаление валюты",
)
async def delete_currency(currency_id: int):
    pass
