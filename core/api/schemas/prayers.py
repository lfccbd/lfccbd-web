from ninja import ModelSchema

from core.prayers.models import PrayerRequest


class PrayerCreateSchema(ModelSchema):
	class Config:
		model = PrayerRequest
		model_fields = ['first_name', 'last_name', 'prayer', 'date_received']


class PrayerSchema(ModelSchema):
	class Config:
		model = PrayerRequest
		model_fields = ['date_received']
		from_attributes = True
