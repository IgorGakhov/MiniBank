import enum


class AccountTypesEnum(enum.Enum):
    debit = "debit"
    credit = "credit"
    salary = "salary"
    invest = "invest"


class CustomerType(enum.Enum):
    individual = "individual"
    business = "business"
