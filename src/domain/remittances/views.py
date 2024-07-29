from fastapi import APIRouter, Depends, Query

from src.domain.base.unit_of_work import AbstractUnitOfWork, SqlAlchemyUnitOfWork


router = APIRouter(prefix="/transfers", tags=["Транзакции"])


@router.get(
    path="",
    summary="Получение списка операций перевода денежных средств",
)
async def get_transfers(
    page: int = Query(1, ge=1, description="Номер страницы"),
    limit: int = Query(20, gt=0, le=100, description="Лимит объектов на странице"),
    uow: AbstractUnitOfWork = Depends(SqlAlchemyUnitOfWork),
):
    async with uow:
        objs = await uow.remittances_repo.list(limit, page - 1)
    return objs


@router.get(
    path="/{remittance_id}",
    summary="Получение информации о переводе денежных средств",
)
async def get_transfer_by_id(
    remittance_id: int,
    uow: AbstractUnitOfWork = Depends(SqlAlchemyUnitOfWork),
):
    async with uow:
        obj = await uow.remittances_repo.get_by_id(remittance_id)
    return obj
