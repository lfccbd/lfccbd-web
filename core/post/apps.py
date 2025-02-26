from django.apps import AppConfig


class PostConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.post"
    icon = 'fas fa-blog'
    divider_title = "Apps"
    priority = 1
    hide = False
