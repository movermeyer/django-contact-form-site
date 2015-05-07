# -*- coding: utf-8 -*-
from __future__ import with_statement
from django.template.base import (Node, Library, TemplateSyntaxError)
from django.template.loader import get_template
from django_contact.models import ContactForm
from django_contact.utils import get_object_or_none

import re

register = Library()


kwarg_re = re.compile(r"(?:(\w+)=)?(.+)")


class ShowContactForm(Node):
    def __init__(self, contact_slug, template=None):
        self.contact_slug = contact_slug
        self.template = template or "django_contact/contact_form.html"

    def get_contact_instance(self, context):
        contact_slug = self.contact_slug.resolve(context)
        return get_object_or_none(ContactForm, slug=contact_slug)

    def render(self, context):
        try:
            template = self.template.resolve(context)
        except:
            template = self.template
        c = self.get_context(context)
        t = get_template(template)
        return t.render(c)

    def get_context(self, context):
        if not 'request' in context:
            raise TypeError("Keyword argument 'request' must be supplied")
        request = context['request']
        contact_instance = self.get_contact_instance(context)
        if contact_instance is not None:
            form_class = contact_instance.get_form_class()
            form = form_class(request=request)
            context.update({'form': form})
        return context


@register.tag(name="show_contact_form")
def do_show_contact_form(parser, token):
    bits = token.split_contents()
    if len(bits) < 2:
        raise TemplateSyntaxError("'%s' takes at least one argument"
                                  " (title and url)" % bits[0])

    contact_slug = parser.compile_filter(bits[1])
    bits = bits[1:]

    kwargs = {}

    if len(bits):
        for bit in bits:
            match = kwarg_re.match(bit)
            if not match:
                raise TemplateSyntaxError("Malformed arguments to url tag")
            name, value = match.groups()
            if name:
                kwargs[name] = parser.compile_filter(value)

    template = kwargs.get('template')
    return ShowContactForm(contact_slug, template)