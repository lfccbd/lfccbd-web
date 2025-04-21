from ninja import ModelSchema

from core.contacts.models import Contact


class ContactCreateSchema(ModelSchema):
	class Config:
		model = Contact
		model_fields = ['full_name', 'phone', 'message']


class ContactSchema(ModelSchema):
	class Config:
		model = Contact
		model_fields = ['date_received']
		from_attributes = True
