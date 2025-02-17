from datetime import datetime

from pydantic import BaseModel

from core.api.schemas.resources import MediaSchema


class UpcomingServiceSchema(BaseModel):
	id: str  # noqa: A003, E261
	service_theme: str
	service_date_time: datetime
	service_description: str
	service_image: str
	publish: bool
	date_created: datetime
	last_updated: datetime

	class Config:
		from_attributes = True


class EpistleOfMonthSchema(BaseModel):
	id: str  # noqa: A003, E261
	epistle_message_theme: str
	epistle_message_topic: str
	epistle_message: str
	epistle_image: str
	publish: bool
	date_created: datetime
	last_updated: datetime

	class Config:
		from_attributes = True

	@classmethod
	def from_orm(cls, obj):
		# override the from_orm method to handle ORM objects"
		return cls.model_validate(obj)

	@classmethod
	def from_orm_many(cls, objs):
		"""Process a list of ORM objects"""
		return [cls.from_orm(obj) for obj in objs]


class WordOfDaySchema(BaseModel):
	id: str  # noqa: A003, E261
	message_topic: str
	message_for_day: str
	message: str
	message_image: str
	publish: bool
	date_created: datetime
	last_updated: datetime

	class Config:
		from_attributes = True


class VerseOfDaySchema(BaseModel):
	id: str  # noqa: A003, E261
	verse: str
	verse_for_day: str
	message: str
	message_image: str
	publish: bool
	date_created: datetime
	last_updated: datetime

	class Config:
		from_attributes = True


class BookmarkedUpcomingServiceSchema(BaseModel):
	bookmark_id: str  # noqa: A003, E261
	item_bookmarked: UpcomingServiceSchema
	publish: bool
	date_created: datetime
	last_updated: datetime

	class Config:
		from_attributes = True


class BookmarkedEpistleOfMonthSchema(BaseModel):
	bookmark_id: str  # noqa: A003, E261
	item_bookmarked: EpistleOfMonthSchema
	publish: bool
	date_created: datetime
	last_updated: datetime

	class Config:
		from_attributes = True


class BookmarkedWordOfDaySchema(BaseModel):
	bookmark_id: str  # noqa: A003, E261
	item_bookmarked: WordOfDaySchema
	publish: bool
	date_created: datetime
	last_updated: datetime

	class Config:
		from_attributes = True


class BookmarkedVerseOfDaySchema(BaseModel):
	bookmark_id: str  # noqa: A003, E261
	item_bookmarked: VerseOfDaySchema
	publish: bool
	date_created: datetime
	last_updated: datetime

	class Config:
		from_attributes = True


class SaveForLaterMediaSchema(BaseModel):
	id: str  # noqa: A003, E261
	media_saveded: MediaSchema
	publish: bool
	date_created: datetime
	last_updated: datetime

	class Config:
		from_attributes = True
