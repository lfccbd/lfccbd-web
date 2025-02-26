from django.contrib import messages
from django.http import HttpResponsePermanentRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .models import PrayerRequest  # type: ignore

from .forms import PrayerRequestForm


class PrayerRequestPage(CreateView):
	model = PrayerRequest
	form_class = PrayerRequestForm
	success_url = 'prayer_request'
	template_name = 'forms/prayer-request.html'

	def get_success_url(self):
		return super().get_success_url()

	def post(self, request, *_args, **kwargs):
		form = PrayerRequestForm(request.POST)

		if form.is_valid():
			# submit form
			super(PrayerRequestPage, self).form_valid(form)

			# message
			messages.success(request, 'Prayer Request sent successfully.')

			return HttpResponsePermanentRedirect(reverse_lazy(self.success_url))

		#  Set object to None, since class-based view expects model record object
		self.object = None

		# message
		messages.error(request, 'Invalid Form Field(s). All fields are required.')
		# Return class-based view form_invalid to generate form with errors
		return self.form_invalid(form)
