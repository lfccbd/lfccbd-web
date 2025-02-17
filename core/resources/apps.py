from django.apps import AppConfig


class ResourcesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.resources'
    icon = 'fas fa-photo-video'
    divider_title = "Apps"
    priority = 1
    hide = False
