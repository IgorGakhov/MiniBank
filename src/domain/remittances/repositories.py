from src.domain.base.repositories import SqlAlchemyRepository
from .models import Remittance


class RemittancesRepository(SqlAlchemyRepository):
    model = Remittance
