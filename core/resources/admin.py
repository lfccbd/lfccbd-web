from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Book, ImageSlider, Media


class MediaResource(resources.ModelResource):
	class Meta:
		model = Media
		skip_unchanged = True
		report_skipped = True
		exclude = ['id', 'slug', 'date_created', 'history']


class BookResource(resources.ModelResource):
	class Meta:
		model = Book
		skip_unchanged = True
		report_skipped = True
		exclude = ['id', 'slug', 'date_created', 'history']


class ImageSliderAdmin(admin.ModelAdmin):
	list_display = ['id', 'image_1', 'image_2', 'image_3', 'image_4']
	list_display_links = ['id', 'image_1', 'image_2', 'image_3', 'image_4']
	list_per_page = 50
	actions_on_top = True
	actions_on_bottom = True
	save_as = True
	save_as_continue = True
	save_on_top = True
	search_fields = [
		'image_1_text',
		'image_1',
		'image_2_text',
		'image_2',
		'image_3_text',
		'image_3',
		'image_4_text',
		'image_4',
	]
	fieldsets = [
		[
			'Slider One',
			{
				'classes': ['wide', 'extrapretty'],
				'fields': ['image_1_text', 'image_1'],
			},
		],
		[
			'Slider Two Details',
			{
				'classes': ['collapse', 'wide', 'extrapretty'],
				'fields': ['image_2_text', 'image_2'],
			},
		],
		[
			'Slider Three Details',
			{
				'classes': ['collapse', 'wide', 'extrapretty'],
				'fields': ['image_3_text', 'image_3'],
			},
		],
		[
			'Slider Four Details',
			{
				'classes': ['collapse', 'wide', 'extrapretty'],
				'fields': ['image_4_text', 'image_4'],
			},
		],
	]


class MediaMessageAdmin(ImportExportModelAdmin):
	resource_class = MediaResource
	list_display = [
		'file_title',
		'service',
		'file_title',
		'sermon_type',
		'media_format',
		'message_date',
	]
	list_display_links = ['file_title', 'service', 'file_title']
	list_filter = ['publish']
	date_hierarchy = 'last_updated'
	list_per_page = 50
	actions_on_top = True
	actions_on_bottom = True
	readonly_fields = ['date_created']
	save_as = True
	save_as_continue = True
	save_on_top = True
	search_fields = ['file_title', 'service', 'message_date']
	fields = [
		'file_title',
		'service',
		'resource_file',
		'sermon_type',
		'media_format',
		'message_date',
		'publish',
		'last_updated',
	]


class BooksAdmin(ImportExportModelAdmin):
	resource_class = BookResource
	list_display = ['file_title', 'author', 'publish_year', 'publisher', 'isbn', 'publish']
	list_display_links = ['file_title', 'author', 'publish_year', 'publisher', 'isbn']
	list_filter = ['publish']
	date_hierarchy = 'last_updated'
	list_per_page = 50
	actions_on_top = True
	actions_on_bottom = True
	readonly_fields = ['date_created']
	save_as = True
	save_as_continue = True
	save_on_top = True
	search_fields = ['file_title', 'author', 'gnere', 'publish_year', 'publisher', 'isbn']

	fieldsets = [
		[
			'General Information',
			{
				'classes': ['wide', 'extrapretty'],
				'fields': ['file_title', 'author', 'foreward'],
			},
		],
		[
			'Publisher Details',
			{
				'classes': ['collapse', 'wide', 'extrapretty'],
				'fields': ['publisher', 'publish_year', 'isbn'],
			},
		],
		[
			'Images',
			{
				'classes': ['collapse', 'wide', 'extrapretty'],
				'fields': ['featured_image', 'image_1', 'image_2'],
			},
		],
		[
			'Publish Details',
			{
				'classes': ['collapse', 'wide', 'extrapretty'],
				'fields': ['publish', 'last_updated'],
			},
		],
	]


admin.site.register(ImageSlider, ImageSliderAdmin)
admin.site.register(Media, MediaMessageAdmin)
admin.site.register(Book, BooksAdmin)
