from datetime import datetime

from pydantic import BaseModel


class ContactCreateSchema(BaseModel):
    full_name: str
    phone: str
    message: str


class ContactSchema(BaseModel):
    date_received: datetime

    class Config:
        from_attributes = True
