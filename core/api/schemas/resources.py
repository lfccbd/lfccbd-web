from datetime import datetime

from pydantic import BaseModel


# Response schema (output)
class SliderSchema(BaseModel):
	image_1_text: str
	image_1: str
	image_2_text: str
	image_2: str
	image_3_text: str
	image_3: str
	image_4_text: str
	image_4: str

	class Config:
		from_attributes = True


class ContactCreateSchema(BaseModel):
	full_name: str
	phone: str
	message: str


class ContactSchema(BaseModel):
	date_received: datetime

	class Config:
		from_attributes = True


class MediaSchema(BaseModel):
	id: str  # noqa: A003, E261
	slug: str
	file_title: str
	category: str
	service: str
	message_date: str
	reource_file: str
	view_count: str
	publish: bool
	date_created: datetime
	last_updated: datetime

	class Config:
		from_attributes = True

	@classmethod
	def from_orm(cls, obj):
		# override the from_orm method to handle ORM objects"
		return cls.model_validate(obj)


# Response schema (output)
class BookSchema(BaseModel):
	id: str  # noqa: A003, E261
	slug: str
	file_title: str
	category: str
	author: str
	publish_year: int
	publisher: str
	foreward: str
	isbn: str
	featured_image: str
	image_1: str
	image_2: str
	view_count: int
	publish: bool
	date_created: datetime
	last_updated: datetime

	class Config:
		from_attributes = True

	@classmethod
	def from_orm(cls, obj):
		# override the from_orm method to handle ORM objects"
		return cls.model_validate(obj)
