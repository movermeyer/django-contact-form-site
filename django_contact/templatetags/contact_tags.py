# -*- coding: utf-8 -*-
from __future__ import with_statement
from django.core.exceptions import ImproperlyConfigured
from django.template.base import (Node, Library, TemplateSyntaxError)
from django.template.loader import get_template
from django_contact.utils import get_contact_form_class
from django_contact import settings

import re

register = Library()


kwarg_re = re.compile(r"(?:(\w+)=)?(.+)")


class ShowContactForm(Node):

    def __init__(self, template=None):
        self.template = template or settings.CONTACT_FORM_TEMPLATE

    def render(self, context):
        try:
            template = self.template.resolve(context)
        except:
            template = self.template

        if not 'request' in context:
            raise ImproperlyConfigured("'request' must be supplied")

        self.request = context['request']

        c = self.get_context(context)
        t = get_template(template)
        return t.render(c)

    def get_form_class(self):
        return get_contact_form_class()

    def get_form_kwargs(self):
        return {"request": self.request}

    def get_form(self, form_class):
        return form_class(**self.get_form_kwargs())

    def get_context(self, context):
        context.update({
            "form": self.get_form(self.get_form_class())
        })
        return context


@register.tag(name="show_contact_form")
def do_show_contact_form(parser, token):
    bits = token.split_contents()
    tag = bits.pop(0)
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
    return ShowContactForm(template=template)