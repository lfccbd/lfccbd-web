from django.apps import AppConfig


class ResourcesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.resources'
    icon = 'fas fa-photo-video'
    priority = 3
    hide = False
