from django.apps import AppConfig


class TestimoniesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.testimonies'
    icon = 'fas fa-microphone-alt'
    divider_title = "Apps"
    priority = 2
    hide = False
