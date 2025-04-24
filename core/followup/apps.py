from django.apps import AppConfig


class FollowupConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.followup"
    icon = 'fas fa-broadcast-tower'
    divider_title = 'Kingdom Care'
    priority = 1
    hide = False
