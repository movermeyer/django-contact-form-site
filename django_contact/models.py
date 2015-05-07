from django.core.mail import get_connection
from django.db import models
from django.conf import settings as django_settings
from django.utils.translation import ugettext as _

from django_contact.secure import MD5Field
from django_contact.settings import CONTACT_FORM
from django_contact.utils import import_form_class


class ContactForm(models.Model):
    name = models.CharField(
        max_length=100,
        help_text=_("Name to identify the contact form."))
    slug = models.SlugField(
        max_length=100, unique=True,
        help_text=_("Unique name to retrieve the form in rendering the tag 'show_contact_form'."))

    form = models.CharField(
        max_length=255, choices=CONTACT_FORM,
        default='django_contact.forms.ContactForm',
        help_text=_("Form the class path to be used when sending contact."))

    # email auth
    auth_email_user = models.EmailField(
        default=getattr(django_settings, 'EMAIL_HOST_USER', None),
        help_text=_("User to authenticate to the SMTP server."))
    auth_email_password = MD5Field(
        max_length=50,
        help_text=_("Password to authenticate to the SMTP server."))
    auth_email_host = models.CharField(
        max_length=50,
        help_text=_("Host SMTP authentication server."))
    auth_email_port = models.PositiveIntegerField(
        default=getattr(django_settings, 'EMAIL_PORT', 3306),
        help_text=_("Port SMTP authentication server. Default 3306."))
    auth_email_use_tls = models.BooleanField(
        default=getattr(django_settings, 'EMAIL_USE_TLS', False),
        help_text=_("The SMTP server uses TLS (Transport Layer Security)."))

    recipient_list = models.CharField(
        max_length=2048,
        help_text=_("E-mail list that will receive the contact. Separated by ','."))

    # templates
    email_subject = models.CharField(
        max_length=255,
        help_text=("Title the email that will be sent."))
    email_html_content = models.TextField(help_text=_("HTML content of the email being sent."))
    email_text_content = models.TextField(help_text=_("Plain Text content of the email being sent."))

    def get_email_connection(self, fail_silently=False):
        return get_connection(
            username=self.auth_email_user,
            password=self.get_auth_email_password_decrypted(),
            host=self.auth_email_host,
            port=self.auth_email_port,
            use_tls=self.auth_email_use_tls,
            fail_silently=fail_silently)

    def get_form_class(self):
        form_class = import_form_class(self.form)
        # bind with this model
        setattr(form_class, 'contact_instance', self)
        return form_class