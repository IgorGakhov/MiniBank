from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, field_validator, EmailStr
import phonenumbers


class IndividualCustomerCreate(BaseModel):
    name: str
    patronymic: Optional[str] = None
    surname: str
    email: EmailStr
    phone: str
    taxpayer_id_number: str

    @field_validator("phone")
    def validate_phone(cls, v: str) -> str:
        try:
            parsed_phone = phonenumbers.parse(v, None)
            if not phonenumbers.is_valid_number(parsed_phone):
                raise ValueError("Invalid phone number")
        except phonenumbers.phonenumberutil.NumberParseException:
            raise ValueError("Invalid phone number format")
        return v


class IndividualCustomerPatch(IndividualCustomerCreate):
    id: int


class IndividualCustomer(BaseModel):
    id: int
    name: str
    patronymic: str
    surname: str
    email: str
    phone: str
    taxpayer_id_number: str
    date_create: datetime
    date_modify: datetime


class IndividualCustomerListItem(BaseModel):
    id: int
    full_name: str
    email: str
    phone: str
    taxpayer_id_number: str
    date_create: datetime
    date_modify: datetime


class IndividualCustomersList(BaseModel):
    content: Optional[List[IndividualCustomerListItem]]


class BusinessCustomerCreate(BaseModel):
    name: str
    owner_id: int
    taxpayer_id_number: str
    main_state_reg_number: str


class BusinessCustomerPatch(BusinessCustomerCreate):
    id: int


class BusinessCustomer(BaseModel):
    id: int
    name: str
    owner_id: int
    taxpayer_id_number: str
    main_state_reg_number: str
    date_create: datetime
    date_modify: datetime


class BusinessCustomerListItem(BaseModel):
    id: int
    name: str
    owner_id: int
    taxpayer_id_number: str
    main_state_reg_number: str
    date_create: datetime
    date_modify: datetime


class BusinessCustomersList(BaseModel):
    content: Optional[List[BusinessCustomerListItem]]
