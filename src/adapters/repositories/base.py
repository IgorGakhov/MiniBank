import abc
from typing import Any, Dict, Optional, Type

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import (
    Sequence,
    insert,
    select,
    update,
)

from ...db.base import Base, get_session


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    async def add(self, obj: Dict) -> Optional[Base]:
        raise NotImplementedError

    @abc.abstractmethod
    async def get_by_id(self, obj_id: int) -> Base:
        raise NotImplementedError

    @abc.abstractmethod
    async def list(self, limit: int, offset: int) -> Sequence[Base]:
        raise NotImplementedError

    @abc.abstractmethod
    async def update(self, obj_id: int, data: Dict[Any, Any]) -> Base:
        raise NotImplementedError

    @abc.abstractmethod
    async def delete(self, obj_id: int) -> None:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    model: Type[Base]

    def __init__(self, session: AsyncSession = get_session()):
        super().__init__()
        self.session = session

    async def add(self, obj: Dict) -> Optional[Base]:
        query = insert(self.model).values(**obj).returning(self.model)
        result = await self.session.execute(query)
        obj = result.scalar_one_or_none()

        return obj

    async def get_by_id(self, obj_id: int) -> Base:
        query = select(self.model).filter_by(id=obj_id).limit(1)
        result = await self.session.execute(query)
        obj = result.unique().scalar_one_or_none()

        return obj

    async def list(self, limit: int, offset: int) -> Sequence[Base]:
        query = (
            select(self.model)
            .order_by(self.model.id.desc())
            .limit(limit)
            .offset(offset * limit)
        )
        result = await self.session.execute(query)
        objs = result.unique().scalars().all()

        return objs

    async def update(self, obj_id: int, data: Dict[Any, Any]) -> Base:
        query = (
            update(self.model)
            .where(
                self.model.__table__.c.id == obj_id,
            )
            .values(
                **data,
            )
            .returning(self.model)
        )
        result = await self.session.execute(query)
        obj = result.unique().scalar_one_or_none()

        return obj

    async def delete(self, obj_id: int) -> None:
        query = select(self.model).filter_by(id=obj_id)
        result = await self.session.execute(query)
        result = result.scalar_one_or_none()
        if not result:
            raise ValueError
        await self.session.delete(result)
