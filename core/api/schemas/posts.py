from ninja import ModelSchema

from core.post.models import (
    EpistleOfMonth,
    UpcomingService,
    VerseOfDay,
    WordOfDay,
)


class UpcomingServiceSchema(ModelSchema):
    class Config:
        model = UpcomingService
        model_fields = [
            'id',
            'service_theme',
            'service_date_time',
            'service_description',
            'service_image',
            'publish',
            'date_created',
            'last_updated',
        ]
        from_attributes = True


class EpistleOfMonthSchema(ModelSchema):
    class Config:
        model = EpistleOfMonth
        model_fields = [
            'id',
            'epistle_message_theme',
            'epistle_message_topic',
            'epistle_message',
            'epistle_image',
            'publish',
            'date_created',
            'last_updated',
        ]
        from_attributes = True


class WordOfDaySchema(ModelSchema):
    class Config:
        model = WordOfDay
        model_fields = [
            'id',
            'message_topic',
            'message_for_day',
            'message',
            'message_image',
            'publish',
            'date_created',
            'last_updated',
        ]
        from_attributes = True


class VerseOfDaySchema(ModelSchema):
    class Config:
        model = VerseOfDay
        model_fields = [
            'id',
            'verse',
            'verse_for_day',
            'message',
            'message_image',
            'publish',
            'date_created',
            'last_updated',
        ]
        from_attributes = True
