from django.apps import AppConfig


class JoinAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'join_app'

    def ready(self):
        import join_app.signals 