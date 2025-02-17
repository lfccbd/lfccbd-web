from django.contrib import admin

from .models import Books, ImageSliders, Media


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


class MediaMessageAdmin(admin.ModelAdmin):
	list_display = ['file_title', 'service', 'file_title', 'sermon_type', 'view_count', 'message_date']
	list_display_links = ['file_title', 'service', 'file_title', 'view_count']
	list_filter = ['publish']
	date_hierarchy = 'last_updated'
	list_per_page = 50
	actions_on_top = True
	actions_on_bottom = True
	readonly_fields = ['date_created']
	save_as = True
	save_as_continue = True
	save_on_top = True
	search_fields = ['file_title', 'service', 'view_count', 'message_date']
	fields = [
		'file_title',
		'service',
		'reource_file',
		'sermon_type',
		'view_count',
		'message_date',
		'publish',
		'last_updated',
	]


class BooksAdmin(admin.ModelAdmin):
	list_display = ['file_title', 'author', 'publish_year', 'publisher', 'isbn', 'view_count', 'publish']
	list_display_links = ['file_title', 'author', 'publish_year', 'publisher', 'isbn', 'view_count']
	list_filter = ['publish']
	date_hierarchy = 'last_updated'
	list_per_page = 50
	actions_on_top = True
	actions_on_bottom = True
	readonly_fields = ['date_created']
	save_as = True
	save_as_continue = True
	save_on_top = True
	search_fields = ['file_title', 'author', 'publish_year', 'publisher', 'isbn']

	fieldsets = [
		[
			'General Information',
			{
				'classes': ['wide', 'extrapretty'],
				'fields': ['file_title', 'author', 'view_count', 'foreward'],
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


admin.site.register(ImageSliders, ImageSliderAdmin)
admin.site.register(Media, MediaMessageAdmin)
admin.site.register(Books, BooksAdmin)
