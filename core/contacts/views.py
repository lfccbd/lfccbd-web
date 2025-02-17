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
			# submit form based on either contact or consultation
			super(ContactPage, self).form_valid(form)

			# message
			messages.success(request, 'Message sent successfully. A representative would respond to your message.')

			return HttpResponsePermanentRedirect(reverse_lazy(self.success_url))

		#  Set object to None, since class-based view expects model record object
		self.object = None

		# message
		messages.error(request, 'Invalid Form Field(s). Kindly check field(s) and try again; all fields are required.')
		# Return class-based view form_invalid to generate form with errors
		return self.form_invalid(form)
