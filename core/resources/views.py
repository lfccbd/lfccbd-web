from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.http import JsonResponse
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
        media_publish = Media.objects.order_by('-message_date').filter(publish=True)

        # pagination kwargs
        book_page = self.request.GET.get('book_page', None)
        media_page = self.request.GET.get('media_page', None)

        # session check
        # session_exist = self.request.session.get('search_section', None)

        #
        books, media = '', ''

        # filter
        if book_page or media_page:
            if book_page:
                books = books_publish
            if media_page:
                media = media_publish
        else:
            if search_section == 'sermons':
                # filter sermon
                media = media_publish.filter(
                    (
                        Q(file_title__icontains=search_query)
                        | Q(service__icontains=search_query)
                        | Q(sermon_type__icontains=search_query)
                    )
                    & Q(category__icontains=search_section)
                )
                # remain unchanged
                books = books_publish
            elif search_section == 'books':
                # filter books
                books = books_publish.filter(
                    (
                        Q(file_title__icontains=search_query)
                        | Q(gnere__icontains=search_query)
                    )
                    & Q(category__icontains=search_section)
                )

                # remain unchanged
                media = media_publish

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


class MediaContent(View):
    def get(self, request, *args, **kwargs):
        try:
            media_id = self.kwargs.get('id')
            media = Media.objects.get(id=media_id)
            media_content = {
                'format': media.media_format,
                'file_title': media.file_title,
                'service': media.service,
                'message_date': media.message_date.strftime('%d-%m-%Y'),
                'media_source': media.resource_file.url,
            }

            return JsonResponse({'media_content': media_content})

        except Media.DoesNotExist:
            return JsonResponse({'error': 'Media not found'}, status=404)
