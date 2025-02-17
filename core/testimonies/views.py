from django.contrib import messages
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from .forms import TestimonyForm
from .models import Testimony  # type: ignore


class TestimonyPage(View):
	model = Testimony
	success_url = 'testimony'
	template_name = 'pages/testimony.html'

	def get(self, request, *_args, **kwargs):
		# form
		form = TestimonyForm()

		# set context
		context = {'form': form}

		return render(request, self.template_name, context)

	def post(self, request, *_args, **kwargs):
		form = TestimonyForm(request.POST)

		if form.is_valid():
			# save instance
			self.model.objects.create(**form.cleaned_data)

			# success message
			messages.success(request, 'Testimony sent successfully.')

			return HttpResponsePermanentRedirect(reverse_lazy(self.success_url))

		# error message
		messages.error(request, 'Invalid Form Field(s). Kindly check field(s)')

		# render form message
		return render(request, self.template_name, {'form': form})
