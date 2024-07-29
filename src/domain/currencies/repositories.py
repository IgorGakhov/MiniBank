from src.domain.base.repositories import SqlAlchemyRepository
from .models import Currency


class CurrenciesRepository(SqlAlchemyRepository):
    model = Currency
