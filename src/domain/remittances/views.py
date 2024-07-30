from fastapi import APIRouter, Depends, Query

from src.domain.base.unit_of_work import AbstractUnitOfWork, SqlAlchemyUnitOfWork
from .services import RemittancesService


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
    objs = await RemittancesService().get_all(limit, page - 1, uow)
    return objs


@router.get(
    path="/{remittance_id}",
    summary="Получение информации о переводе денежных средств",
)
async def get_transfer_by_id(
    remittance_id: int,
    uow: AbstractUnitOfWork = Depends(SqlAlchemyUnitOfWork),
):
    obj = await RemittancesService().get_by_id(remittance_id, uow)
    return obj
