from ninja import ModelSchema

from core.resources.models import Book, ImageSlider, Media


# Response schema (output)
class SliderSchema(ModelSchema):
	class Config:
		model = ImageSlider
		model_fields = [
			'image_1_text',
			'image_1',
			'image_2_text',
			'image_2',
			'image_3_text',
			'image_3',
			'image_4_text',
			'image_4',
		]
		from_attributes = True


class MediaSchema(ModelSchema):
	class Config:
		model = Media
		model_fields = [
			'id',
			'slug',
			'file_title',
			'category',
			'service',
			'message_date',
			'resource_file',
			'publish',
			'date_created',
			'last_updated',
		]
		from_attributes = True


# Response schema (output)
class BookSchema(ModelSchema):
	class Config:
		model = Book
		model_fields = [
			'id',
			'slug',
			'file_title',
			'category',
			'author',
			'publish_year',
			'publisher',
			'foreward',
			'isbn',
			'featured_image',
			'image_1',
			'image_2',
			'publish',
			'date_created',
			'last_updated',
		]
		from_attributes = True
