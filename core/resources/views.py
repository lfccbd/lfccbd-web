from django.views.generic.list import ListView

from .models import Books, Media


class ResourcesListView(ListView):
	model = Media
	queryset = Media.objects.filter(publish=True)
	template_name = 'resources.html'
	context_object_name = 'resources'
	paginate_by = 10

	def get_queryset(self):
		queryset = super().get_queryset() | Books.objects.filter(publish=True)
		search_query = self.request.GET.get('search', None)
		search_section = self.request.GET.get('section', None)

		if search_query and search_query != '' and search_section and search_section != '':
			self.request.session['search_query'] = search_query
			self.request.session['search_section'] = search_section
			queryset_filter = queryset.filter(category=search_section)
			queryset = queryset_filter.filter(file_name__icontains=search_query)
		return queryset

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['books'] = Books.objects.filter(publish=True)
		context['media'] = Media.objects.filter(publish=True)
		return context
