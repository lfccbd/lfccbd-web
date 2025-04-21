from ninja import ModelSchema

from core.testimonies.models import Testimony


class TestimonyCreateSchema(ModelSchema):
	class Config:
		model = Testimony
		model_fields = ['first_name', 'last_name', 'designation', 'title', 'location', 'testimony']


class TestimonySchema(ModelSchema):
	class Config:
		model = Testimony
		model_fields = [
			'id',
			'first_name',
			'last_name',
			'title',
			'designation',
			'testimony',
			'date_received',
		]
		from_attributes = True
