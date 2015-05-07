from django.conf import settings

# Contact Settings ID
CONTACT_ID = getattr(settings, 'CONTACT_ID', 1)

# Contact form class
CONTACT_FORM = getattr(settings, 'CONTACT_FORM', 'django_contact.forms.ContactForm')

# Templates
CONTACT_FORM_TEMPLATE = getattr(settings, 'CONTACT_FORM_TEMPLATE', 'django_contact/contact.html')