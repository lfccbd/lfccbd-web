from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView

from .forms import TestimonyForm
from .models import Testimony  # type: ignore


class TestimonyPage(ListView):
	model = Testimony
	queryset = Testimony.objects.filter(publish=True)
	context_object_name = 'testimonies'
	paginate_by = 6
	template_name = 'testimonies/testimonies.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['form'] = TestimonyForm()
		return context

	def post(self, request, *_args, **kwargs):
		form = TestimonyForm(request.POST)

		if form.is_valid():
			# save instance
			cleaned_form = form.cleaned_data
			cleaned_form.pop('captcha')
			self.model.objects.create(**cleaned_form)

			# success message
			messages.success(request, 'Testimony sent successfully.')

			return HttpResponsePermanentRedirect(reverse_lazy('testimonies'))

		# error message
		messages.error(request, 'Invalid Form Field(s). Kindly check field(s)')

		# get testimonies again
		testimonies = Testimony.objects.filter(publish=True)

		# manually handle pagination
		paginator = Paginator(testimonies, self.paginate_by)
		page_number = request.GET.get('page', 1)
		page_obj = paginator.get_page(page_number)

		# add pagination to context
		context = self.get_context_data(object_list=page_obj)
		context['form'] = form

		# render form message
		return render(request, self.template_name, context)
