"""
View which can render and send email from a contact form.
"""
from django.http.response import JsonResponse
from django.views.generic.edit import FormView
from django_contact import settings
from django_contact.models import get_current_contact_config
from django_contact.utils import get_contact_form_class


class ContactView(FormView):
    template_name = settings.CONTACT_FORM_TEMPLATE

    def get_form_class(self):
        return get_contact_form_class()

    def form_valid(self, form):
        form.save()
        # if response type as typed with json
        if self.request.GET.get('dataType') == 'json':
            return JsonResponse(form.cleaned_data)
        return super(ContactView, self).form_valid(form)

    def form_invalid(self, form):
        # if response type as typed with json
        if self.request.GET.get('dataType') == 'json':
            response = JsonResponse(form.errors)
        else:
            response = super(ContactView, self).form_invalid(form)

        response.status_code = 400
        return response

    def get_form_kwargs(self):
        # ContactForm instances require instantiation with an
        # HttpRequest.
        kwargs = super(ContactView, self).get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

    def get_success_url(self):
        return get_current_contact_config().sent_url_redirect