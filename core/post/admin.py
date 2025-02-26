from django.contrib import admin

from .models import EpistleOfMonth, UpcomingEvent, UpcomingService, VerseOfDay, WordOfDay


class UpcomingServiceAdmin(admin.ModelAdmin):
	list_display = ['id', 'service_theme', 'service_date_time', 'date_created']
	list_display_links = ['id', 'service_theme', 'service_date_time']
	readonly_fields = ['date_created']
	list_filter = ['publish']
	date_hierarchy = 'last_updated'
	list_per_page = 50
	actions_on_top = True
	actions_on_bottom = True
	save_as = True
	save_as_continue = True
	save_on_top = True
	search_fields = ['service_theme', 'service_description']
	fields = [
		'service_theme',
		'service_date_time',
		'service_description',
		'service_image',
		'publish',
		'last_updated',
	]


class EpistleOfMonthAdmin(admin.ModelAdmin):
	list_display = ['epistle_message_theme', 'epistle_message_topic', 'date_created']
	list_display_links = ['epistle_message_theme', 'epistle_message_topic']
	readonly_fields = ['date_created']
	list_filter = ['publish']
	date_hierarchy = 'last_updated'
	list_per_page = 50
	actions_on_top = True
	actions_on_bottom = True
	save_as = True
	save_as_continue = True
	save_on_top = True
	search_fields = ['epistle_message_theme', 'epistle_message_topic']
	fields = [
		'epistle_message_theme',
		'epistle_message_topic',
		'epistle_message',
		'epistle_image',
		'publish',
		'last_updated',
	]


class WordOfDayAdmin(admin.ModelAdmin):
	list_display = ['message_topic', 'message_for_day', 'date_created']
	list_display_links = ['message_topic', 'message_for_day']
	readonly_fields = ['date_created']
	list_filter = ['publish']
	date_hierarchy = 'last_updated'
	list_per_page = 50
	actions_on_top = True
	actions_on_bottom = True
	save_as = True
	save_as_continue = True
	save_on_top = True
	search_fields = ['message_topic', 'message_for_day']
	fields = [
		'message_topic',
		'message_for_day',
		'message',
		'message_image',
		'publish',
		'last_updated',
	]


class VerseOfDayAdmin(admin.ModelAdmin):
	list_display = ['verse', 'verse_for_day', 'date_created']
	list_display_links = ['verse', 'verse_for_day']
	readonly_fields = ['date_created']
	list_filter = ['publish']
	date_hierarchy = 'last_updated'
	list_per_page = 50
	actions_on_top = True
	actions_on_bottom = True
	save_as = True
	save_as_continue = True
	save_on_top = True
	search_fields = ['message_topic', 'message_for_day']
	fields = [
		'verse',
		'verse_for_day',
		'message',
		'message_image',
		'publish',
		'last_updated',
	]


class UpcomingEventeAdmin(admin.ModelAdmin):
	list_display = ['id', 'event_theme', 'event_date_time', 'date_created']
	list_display_links = ['id', 'event_theme', 'event_date_time']
	readonly_fields = ['date_created']
	list_filter = ['publish']
	date_hierarchy = 'last_updated'
	list_per_page = 50
	actions_on_top = True
	actions_on_bottom = True
	save_as = True
	save_as_continue = True
	save_on_top = True
	search_fields = ['event_theme', 'event_description']
	fields = [
		'event_theme',
		'event_date_time',
		'event_description',
		'event_link',
		'publish',
		'last_updated',
	]


admin.site.register(UpcomingService, UpcomingServiceAdmin)
admin.site.register(EpistleOfMonth, EpistleOfMonthAdmin)
admin.site.register(WordOfDay, WordOfDayAdmin)
admin.site.register(VerseOfDay, VerseOfDayAdmin)
admin.site.register(UpcomingEvent, UpcomingEventeAdmin)
