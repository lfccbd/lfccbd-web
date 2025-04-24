from django.contrib import messages
from django.http import HttpResponsePermanentRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from core.contacts.models import Contact  # type: ignore

from .forms import UserContactForm


class ContactPage(CreateView):
	model = Contact
	form_class = UserContactForm
	success_url = 'contact'
	template_name = 'pages/contact.html'

	def get_success_url(self):
		return super().get_success_url()

	def post(self, request, *_args, **kwargs):
		form = UserContactForm(request.POST)

		if form.is_valid():
			# submit form
			super(ContactPage, self).form_valid(form)

			# message
			messages.success(request, 'Message sent successfully. A representative would reach out to you.')

			return HttpResponsePermanentRedirect(reverse_lazy(self.success_url))

		#  set object to None, since class-based view expects model record object
		self.object = None

		# message
		messages.error(request, 'Invalid Form Field(s). All fields are required.')
		# return class-based view form_invalid
		# to generate form with errors
		return self.form_invalid(form)
