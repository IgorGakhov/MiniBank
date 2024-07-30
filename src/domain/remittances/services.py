from src.domain.base.unit_of_work import AbstractUnitOfWork


class RemittancesService:

    async def get_all(
        self,
        limit: int,
        offset: int,
        uow: AbstractUnitOfWork,
    ):
        async with uow:
            objs = await uow.remittances_repo.list(limit, offset)
        return objs

    async def get_by_id(
        currency_id: int,
        uow: AbstractUnitOfWork,
    ):
        async with uow:
            obj = await uow.remittances_repo.get_by_id(currency_id)
        return obj
