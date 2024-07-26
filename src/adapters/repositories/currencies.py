from .base import SqlAlchemyRepository
from ...db.models import Currency


class CurrenciesRepository(SqlAlchemyRepository):
    model = Currency
