from datetime import datetime

from pydantic import BaseModel


class PrayerCreateSchema(BaseModel):
    first_name: str
    last_name: str
    prayer: str
    date_received: datetime


class PrayerSchema(BaseModel):
    date_received: datetime

    class Config:
        from_attributes = True
