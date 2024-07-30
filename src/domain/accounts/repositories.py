from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.database.engine import Base, get_session
from src.domain.base.repositories import SqlAlchemyRepository
from .models import IndividualAccount, BusinessAccount


class BaseAccountsRepository(SqlAlchemyRepository):

    async def get_by_number(self, obj_number: str) -> Base:
        query = select(self.model).filter_by(number=obj_number).limit(1)
        result = await self.session.execute(query)
        obj = result.unique().scalar_one_or_none()

        return obj


class IndividualAccountsRepository(BaseAccountsRepository):
    model = IndividualAccount


class BusinessAccountsRepository(BaseAccountsRepository):
    model = BusinessAccount
