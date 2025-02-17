from django.contrib import admin

from .models import (
    BookmarkedEpistleOfMonth,
    BookmarkedUpcomingService,
    BookmarkedVerseOfDay,
    BookmarkedWordOfDay,
    EpistleOfMonth,
    SaveForLaterMedia,
    UpcomingService,
    VerseOfDay,
    WordOfDay,
)


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


class BookmarkedUpcomingServiceAdmin(admin.ModelAdmin):
    list_display = [
        'bookmark_id',
        'item_bookmarked',
        'publish',
        'date_created',
    ]
    list_display_links = ['bookmark_id', 'item_bookmarked']
    readonly_fields = ['date_created']
    list_filter = ['publish']
    date_hierarchy = 'last_updated'
    list_per_page = 50
    actions_on_top = True
    actions_on_bottom = True
    save_as = True
    save_as_continue = True
    save_on_top = True
    search_fields = ['item_bookmarked__service_theme']
    fields = ['bookmark_id', 'item_bookmarked', 'publish', 'last_updated']


class BookmarkedEpistleOfMonthAdmin(admin.ModelAdmin):
    list_display = ['bookmark_id', 'item_bookmarked', 'publish', 'date_created']
    list_display_links = ['bookmark_id', 'item_bookmarked']
    readonly_fields = ['date_created']
    list_filter = ['publish']
    date_hierarchy = 'last_updated'
    list_per_page = 50
    actions_on_top = True
    actions_on_bottom = True
    save_as = True
    save_as_continue = True
    save_on_top = True
    search_fields = ['item_bookmarked']
    fields = ['bookmark_id', 'item_bookmarked', 'publish', 'last_updated']


class BookmarkedWordOfDayAdmin(admin.ModelAdmin):
    list_display = ['bookmark_id', 'item_bookmarked', 'publish', 'date_created']
    list_display_links = ['bookmark_id', 'item_bookmarked']
    readonly_fields = ['date_created']
    list_filter = ['publish']
    date_hierarchy = 'last_updated'
    list_per_page = 50
    actions_on_top = True
    actions_on_bottom = True
    save_as = True
    save_as_continue = True
    save_on_top = True
    search_fields = ['item_bookmarked']
    fields = ['bookmark_id', 'item_bookmarked', 'publish', 'last_updated']


class BookmarkedVerseOfDayAdmin(admin.ModelAdmin):
    list_display = ['bookmark_id', 'item_bookmarked', 'publish', 'date_created']
    list_display_links = ['bookmark_id', 'item_bookmarked']
    readonly_fields = ['date_created']
    list_filter = ['publish']
    date_hierarchy = 'last_updated'
    list_per_page = 50
    actions_on_top = True
    actions_on_bottom = True
    save_as = True
    save_as_continue = True
    save_on_top = True
    search_fields = ['item_bookmarked']
    fields = ['bookmark_id', 'item_bookmarked', 'publish', 'last_updated']


class SaveForLaterMediaAdmin(admin.ModelAdmin):
    list_display = ['id', 'media_saveded', 'publish', 'date_created']
    list_display_links = ['id', 'media_saveded']
    readonly_fields = ['date_created']
    list_filter = ['publish']
    date_hierarchy = 'last_updated'
    list_per_page = 50
    actions_on_top = True
    actions_on_bottom = True
    save_as = True
    save_as_continue = True
    save_on_top = True
    search_fields = ['media_saveded']
    fields = ['id', 'media_saveded', 'publish', 'last_updated']


admin.site.register(UpcomingService, UpcomingServiceAdmin)
admin.site.register(EpistleOfMonth, EpistleOfMonthAdmin)
admin.site.register(WordOfDay, WordOfDayAdmin)
admin.site.register(VerseOfDay, VerseOfDayAdmin)
admin.site.register(BookmarkedUpcomingService, BookmarkedUpcomingServiceAdmin)
admin.site.register(BookmarkedEpistleOfMonth, BookmarkedEpistleOfMonthAdmin)
admin.site.register(BookmarkedWordOfDay, BookmarkedWordOfDayAdmin)
admin.site.register(BookmarkedVerseOfDay, BookmarkedVerseOfDayAdmin)
admin.site.register(SaveForLaterMedia, SaveForLaterMediaAdmin)
