from typing import Any, List, Union

from django.db.models.query import QuerySet
from django.views.decorators.csrf import csrf_exempt
from ninja.errors import HttpError
from ninja.pagination import PageNumberPagination, paginate

from core.api.schemas.prayers import PrayerCreateSchema, PrayerSchema
from core.contacts.models import Contact
from core.post.models import EpistleOfMonth, UpcomingService, VerseOfDay, WordOfDay
from core.prayers.models import PrayerRequest
from core.resources.models import Book, ImageSlider, Media
from core.testimonies.models import Testimony

from .api_router import router
from .schemas.contacts import ContactCreateSchema, ContactSchema
from .schemas.posts import EpistleOfMonthSchema, UpcomingServiceSchema, VerseOfDaySchema, WordOfDaySchema
from .schemas.resources import BookSchema, MediaSchema, SliderSchema
from .schemas.testimonies import TestimonyCreateSchema, TestimonySchema
from .search.api_searches import search_books, search_epistles, search_sermons, search_testimonies

SearchResultItemSchema = Union[MediaSchema, BookSchema, EpistleOfMonthSchema, TestimonySchema]


@router.get('/resources/sliders/', response=List[SliderSchema])
def get_sliders(request):
	"""
	Get a list of image sliders and their text.
	"""
	response = ImageSlider.objects.all()
	return response


@router.post('/prayer/', response=PrayerSchema)
@csrf_exempt
def create_prayer_message(request, data: PrayerCreateSchema):
	"""
	Send prayer request
	"""
	prayer_instance = PrayerRequest.objects.create(
		first_name=data.first_name,
		last_name=data.last_name,
		prayer=data.prayer,
	)
	return prayer_instance


@router.post('/contact/', response=List[ContactSchema])
@csrf_exempt
def create_contact_message(request, data: ContactCreateSchema):
	"""
	Create contact message
	"""
	contact_instance = Contact.objects.create(
		full_name=data.full_name,
		phone=data.phone,
		message=data.message,
	)
	return contact_instance


@router.get('/resources/media/all/', response=List[MediaSchema])
@paginate(PageNumberPagination, page_size=6)
def get_media(request):
	"""
	Get a list of media(videos and audio).
	"""
	response = Media.objects.all()
	return response


@router.get('/resources/books/all/', response=List[BookSchema])
@paginate(PageNumberPagination, page_size=8)
def get_books(request):
	"""
	Get a list of all books
	"""
	return Book.objects.all()


@router.post('/testimony/', response=TestimonySchema)
@csrf_exempt
def create_testimony(request, data: TestimonyCreateSchema):
	"""
	Create Testimonies
	"""
	testimony_instance = Testimony.objects.create(
		first_name=data.first_name,
		last_name=data.last_name,
		designation=data.designation,
		tesitmony=data.tesitmony,
	)
	return testimony_instance


@router.get('/testimonies/', response=List[TestimonySchema])
@paginate(PageNumberPagination, page_size=6)
def get_testimonies(request):
	"""
	Get a list of all testtimonies
	"""
	return Testimony.objects.all()


@router.get('/post/upcoming_service', response=List[UpcomingServiceSchema])
@paginate(PageNumberPagination, page_size=6)
def get_upcoming_service(request):
	"""
	Get a list of all upcomming service
	"""
	return UpcomingService.objects.all()


@router.get('/post/epistles', response=List[EpistleOfMonthSchema])
@paginate(PageNumberPagination, page_size=4)
def get_epistles(request):
	"""
	Get a list of all epistles
	"""
	return EpistleOfMonth.objects.all()


@router.get('/post/word_of_day/all', response=List[WordOfDaySchema])
@paginate(PageNumberPagination, page_size=4)
def get_word_of_day(request):
	"""
	Get a list of all word of the day
	"""
	return WordOfDay.objects.all()


@router.get('/post/verse_of_day/all', response=List[VerseOfDaySchema])
@paginate(PageNumberPagination, page_size=4)
def get_verse_of_day(request):
	"""
	Get a list of all verse of the day
	"""
	return VerseOfDay.objects.all()


@router.get('/search', response=List[SearchResultItemSchema])
@paginate(PageNumberPagination, page_size=6)
def get_search(request, category: str = '', search: str = ''):
	"""
	Get a paginated list of media, books, epistles, or testimonies
	filtered by category and search keywords.

	Query Parameters:
	- **category**: REQUIRED. Can be "media", "books", "epistles", or "testimonies" (case-insensitive).
	- **search**: REQUIRED. Search keyword (case-insensitive).
	"""
	if category == '' or search == '':
		raise HttpError(400, "Both 'category' and 'search' query parameters are required.")

	category = category.lower()
	results: Union[QuerySet, List[Any]]

	if category == 'media':
		results = search_sermons(search)
	elif category == 'books':
		results = search_books(search)
	elif category == 'epistles':
		results = search_epistles(search)
	elif category == 'testimonies':
		results = search_testimonies(search)
	else:
		raise HttpError(400, "Invalid category. Choose from 'media', 'books', 'epistles' or 'testimonies'.")

	return results
