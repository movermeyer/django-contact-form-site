from django.contrib import admin
from django.utils.translation import ugettext as _
from django_contact.forms import AdminContactForm
from django_contact.models import ContactForm


class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'form']
    list_filter = ['name']
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}
    fieldsets = (
        (None, {'fields': ('name', 'slug', 'recipient_list')}),
        (_('Auth'), {'fields': ('auth_email_host', 'auth_email_user', 'auth_email_password', 'auth_email_port', 'auth_email_use_tls')}),
        (_('Email'), {'fields': ('email_subject', 'email_html_content', 'email_text_content')}),
        (_('Form'), {'fields': ('form',)}),
    )
    form = AdminContactForm

admin.site.register(ContactForm, ContactFormAdmin)