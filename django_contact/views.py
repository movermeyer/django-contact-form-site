"""
View which can render and send email from a contact form.
"""
from django.core.urlresolvers import reverse
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic.edit import FormView
from django_contact.models import ContactForm


class ContactFormView(FormView):
    template_name = 'contact_form/contact_form.html'

    def get_contact_instance(self):
        if self.request.POST:
            return get_object_or_404(ContactForm, slug=self.request.POST.get('contact_slug'))
        return None

    def form_valid(self, form):
        form.save()

        # if response type as typed with json
        if self.request.GET.get('dataType') == 'json':
            return JsonResponse(form.cleaned_data)

        return super(ContactFormView, self).form_valid(form)

    def form_invalid(self, form):
        # if response type as typed with json
        if self.request.GET.get('dataType') == 'json':
            response = JsonResponse(form.errors)
        else:
            response = super(ContactFormView, self).form_valid(form)

        response.status_code = 400
        return response

    def get_form_class(self):
        context_instance = self.get_contact_instance()

        if context_instance is not None:
            return context_instance.get_form_class()

    def get_form_kwargs(self):
        # ContactForm instances require instantiation with an
        # HttpRequest.
        kwargs = super(ContactFormView, self).get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

    def get_success_url(self):
        # This is in a method instead of the success_url attribute
        # because doing it as an attribute would involve a
        # module-level call to reverse(), creating a circular
        # dependency between the URLConf (which imports this module)
        # and this module (which would need to access the URLConf to
        # make the reverse() call).
        return reverse('contact_form_sent')
