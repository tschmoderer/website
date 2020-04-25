from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class HomepageConfig(AppConfig):
    name = 'homepage'
    verbose_name = _('Homapage')

    def ready(self):
        import homepage.signals  # noqa
