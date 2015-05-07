"""
Example URLConf for a contact form.

If all you want is the basic ContactForm with default behavior, just
include this URLConf somewhere in your URL hierarchy (for example, at
``/contact/``)>

"""
from django.conf.urls import patterns
from django.conf.urls import url
from django_contact.views import ContactView

urlpatterns = patterns('',
    url(r'^$', ContactView.as_view(), name='contact_form'),
)
