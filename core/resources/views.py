from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.shortcuts import render
from django.views import View

from .models import Book, Media


class ResourcesListView(View):
	template_name = 'resources/resources.html'

	def get(self, request, *args, **kwargs):  # noqa: C901
		# search queries
		search_query = self.request.GET.get('search', '')
		search_section = self.request.GET.get('section', '')

		if search_query != '' and search_section != '':
			self.request.session['search_query'] = search_query
			self.request.session['search_section'] = search_section

		# model
		books_publish = Book.objects.filter(publish=True)
		media_publish = Media.objects.filter(publish=True)

		# pagination kwargs
		book_page = self.request.GET.get('book_page', None)
		media_page = self.request.GET.get('media_page', None)

		# session check
		session_exist = self.request.session.get('search_section', None)

		#
		books, media = '', ''

		# filter
		if book_page or media_page:
			if session_exist and book_page:
				books = books_publish.filter(
					Q(
						file_title__icontains=self.request.session['search_query']
						| Q(gnere__icontains=self.request.session['search_query'])
					)
					& Q(category=self.request.session.get('search_section'))
				)
			elif session_exist and media_page:
				media = media_publish.filter(
					Q(
						file_title__icontains=self.request.session['search_query']
						| Q(service__icontains=self.request.session['search_query'])
					)
					& Q(category=self.request.session.get('search_section'))
				)
		else:
			if search_section == 'sermons':
				media = media_publish.filter(
					(Q(file_title__icontains=search_query) | Q(service__icontains=search_query))
					& Q(category=search_section)
				)
			elif search_section == 'books':
				books = books_publish.filter(
					(Q(file_title__icontains=search_query) | Q(gnere__icontains=search_query))
					& Q(category=search_section)
				)
			elif search_query and search_query:
				media = media_publish.filter(
					Q(file_title__icontains=search_query) | Q(service__icontains=search_query)
				)
				books = books_publish.filter(Q(file_title__icontains=search_query) | Q(gnere__icontains=search_query))

			else:
				media = media_publish
				books = books_publish

		# books pagination
		book_paginator = Paginator(books, 4)
		try:
			book_page_obj = book_paginator.get_page(book_page)
		except PageNotAnInteger:
			book_page_obj = book_paginator.get_page(1)
		except EmptyPage:
			book_page_obj = book_paginator.get_page(book_paginator.num_pages)

		# media pagination
		media_paginator = Paginator(media, 10)
		try:
			media_page_obj = media_paginator.get_page(media_page)
		except PageNotAnInteger:
			media_page_obj = media_paginator.get_page(1)
		except EmptyPage:
			media_page_obj = media_paginator.get_page(media_paginator.num_pages)

		context = {
			'book_page_obj': book_page_obj,
			'media_page_obj': media_page_obj,
			'book_is_paginated': book_page_obj.has_other_pages(),
			'media_is_paginated': media_page_obj.has_other_pages(),
			'unpaginated_books': Book.objects.filter(publish=True),
		}
		return render(request, self.template_name, context)
