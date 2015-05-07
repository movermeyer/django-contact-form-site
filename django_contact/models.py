from django.core.exceptions import ImproperlyConfigured
from django.core.mail import get_connection
from django.db import models
from django.utils.translation import ugettext_lazy as _

from django_contact.secure import MD5Field
from django_contact import settings


class ContactConfig(models.Model):

    sent_url_redirect = models.CharField(
        max_length=255, default="/",
        help_text=_("Redirect page after sending the email. Only to non-ajax requests."))

    # email auth
    auth_email_user = models.EmailField(
        help_text=_("User to authenticate to the SMTP server."))
    auth_email_password = MD5Field(
        max_length=50,
        help_text=_("Password to authenticate to the SMTP server."))
    auth_email_host = models.CharField(
        max_length=50,
        help_text=_("Host SMTP authentication server."))
    auth_email_port = models.PositiveIntegerField(
        default=3306,
        help_text=_("Port SMTP authentication server. Default 3306."))
    auth_email_use_tls = models.BooleanField(
        default=False,
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

    def get_recipient_list(self):
        # normalize and get recipient_list
        recipient_list = self.recipient_list.replace(' ,', ',')
        recipient_list = recipient_list.replace(', ', ',')
        recipient_list = recipient_list.replace(' , ', ',')
        return recipient_list.split(",")

    def get_email_connection(self, fail_silently=False):
        return get_connection(
            username=self.auth_email_user,
            password=self.get_auth_email_password_decrypted(),
            host=self.auth_email_host,
            port=self.auth_email_port,
            use_tls=self.auth_email_use_tls,
            fail_silently=fail_silently)

    class Meta:
        verbose_name = "Contact Config"
        verbose_name_plural = "Contacts Config"


def get_current_contact_config():
    try:
        return ContactConfig.objects.get(pk=settings.CONTACT_ID)
    except ContactConfig.DoesNotExist:
        raise ImproperlyConfigured("Please set the contact settings in Django admin.")