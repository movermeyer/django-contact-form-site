from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ContactFormConfig(AppConfig):
    """The default AppConfig for admin which does autodiscovery."""
    name = 'django_contact'
    verbose_name = _("Contact")