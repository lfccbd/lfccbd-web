from datetime import datetime

from pydantic import BaseModel


class TestimonyCreateSchema(BaseModel):
	first_name: str
	last_name: str
	designation: str
	tesitmony: str


class TestimonySchema(BaseModel):
	id: str  # noqa: A003, E261
	first_name: str
	last_name: str
	designation: str
	tesitmony: str
	date_received: datetime

	class Config:
		from_attributes = True

	@classmethod
	def from_orm(cls, obj):
		# override the from_orm method to handle ORM objects"
		return cls.model_validate(obj)
