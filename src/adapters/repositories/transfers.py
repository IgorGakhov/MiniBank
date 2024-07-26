from .base import SqlAlchemyRepository
from ...db.models import Remittance


class RemittancesRepository(SqlAlchemyRepository):
    model = Remittance
