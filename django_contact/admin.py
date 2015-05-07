from django.contrib import admin
from django.utils.translation import ugettext as _
from django_contact.forms import ContactConfigForm
from django_contact.models import ContactConfig


class ContactConfigAdmin(admin.ModelAdmin):
    list_display = ['auth_email_host', 'auth_email_user']
    fieldsets = (
        (None, {"fields": ('recipient_list', 'sent_url_redirect',)}),
        (_('Auth'), {'fields': ('auth_email_host', 'auth_email_user', 'auth_email_password', 'auth_email_port', 'auth_email_use_tls')}),
        (_('Email'), {'fields': ('email_subject', 'email_html_content', 'email_text_content')}),
    )
    form = ContactConfigForm

admin.site.register(ContactConfig, ContactConfigAdmin)