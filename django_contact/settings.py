from django.conf import settings
from django.utils.translation import ugettext as _

CONTACT_FORM = (
    ('django_contact.forms.ContactForm', _('Default form')),
) + tuple(getattr(settings, 'CONTACT_FORM', tuple()))