from abc import ABC, abstractmethod
from typing import Any, Dict, Optional

from sqlalchemy import Sequence

from ..engine import Base


class AbstractRepository(ABC):
    @abstractmethod
    async def add(self, obj: Dict) -> Optional[Base]:
        raise NotImplementedError

    @abstractmethod
    async def get_by_id(self, obj_id: int) -> Base:
        raise NotImplementedError

    @abstractmethod
    async def list(self, limit: int, offset: int) -> Sequence[Base]:
        raise NotImplementedError

    @abstractmethod
    async def update(self, obj_id: int, data: Dict[Any, Any]) -> Base:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, obj_id: int) -> None:
        raise NotImplementedError
