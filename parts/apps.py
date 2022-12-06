from django.apps import AppConfig


class PartsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'parts'
    
    def ready(self):
        from parts import receivers
