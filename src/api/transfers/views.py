from fastapi import APIRouter, Query


router = APIRouter(prefix="/transfers", tags=["Транзакции"])


@router.get(
    path="",
    summary="Получение списка операций перевода денежных средств",
)
async def get_transfers(
    page: int = Query(1, ge=1, description="Номер страницы"),
    limit: int = Query(20, gt=0, le=100, description="Лимит объектов на странице"),
):
    pass


@router.get(
    path="/{remittance_id}",
    summary="Получение информации о переводе денежных средств",
)
async def get_transfer_by_id(customer_id: int):
    pass
