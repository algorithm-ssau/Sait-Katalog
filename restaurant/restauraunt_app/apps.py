from django.apps import AppConfig


class RestaurauntAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "restauraunt_app"

    def ready(self):
        import restauraunt_app.signals
