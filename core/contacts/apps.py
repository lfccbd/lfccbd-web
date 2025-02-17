from django.apps import AppConfig


class ContactsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.contacts'
    icon = 'fas fa-address-book'
    divider_title = "Apps"
    priority = 0
    hide = False
