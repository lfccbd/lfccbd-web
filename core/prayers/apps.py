from django.apps import AppConfig


class PrayersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.prayers"
    icon = 'fas fa-pray'
    priority = 2
    hide = False
