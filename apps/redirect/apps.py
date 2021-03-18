from django.apps import AppConfig


class RedirectConfig(AppConfig):
    name = 'apps.redirect'

    def ready(self):
        import apps.redirect.signals
