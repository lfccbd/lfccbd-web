from typing import List

from api.schemas.prayers import PrayerCreateSchema, PrayerSchema
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from ninja.pagination import PageNumberPagination, paginate

from core.contacts.models import Contact
from core.post.models import (
    BookmarkedEpistleOfMonth,
    BookmarkedUpcomingService,
    BookmarkedVerseOfDay,
    BookmarkedWordOfDay,
    EpistleOfMonth,
    SaveForLaterMedia,
    UpcomingService,
    VerseOfDay,
    WordOfDay,
)
from core.prayers.models import PrayerRequest
from core.resources.models import Book, ImageSlider, Media
from core.testimonies.models import Testimony

from .api_router import router
from .schemas.contacts import ContactCreateSchema, ContactSchema
from .schemas.posts import (
    BookmarkedEpistleOfMonthSchema,
    BookmarkedUpcomingServiceSchema,
    BookmarkedVerseOfDaySchema,
    BookmarkedWordOfDaySchema,
    EpistleOfMonthSchema,
    SaveForLaterMediaSchema,
    UpcomingServiceSchema,
    VerseOfDaySchema,
    WordOfDaySchema,
)
from .schemas.resources import (
    BookSchema,
    MediaSchema,
    SliderSchema,
)
from .schemas.testimonies import TestimonyCreateSchema, TestimonySchema
from .search.api_searches import (
    search_books,
    search_epistles,
    search_sermons,
    search_testimonies,
)


@router.get('/resources/sliders/', response=List[SliderSchema])
def get_sliders(request):
    """
    Get a list of image sliders and their text.
    """
    response = ImageSlider.objects.all()
    return response


@router.post('/prayer/', response=List[PrayerSchema])
@ensure_csrf_cookie
@csrf_exempt
def create_prayer_message(request, data: PrayerCreateSchema):
    """
    Send prayer request
    """
    response = PrayerRequest.objects.create(
        first_name=data.first_name,
        last_name=data.last_name,
        prayer=data.prayer,
    )
    return response


@router.post('/contact/', response=List[ContactSchema])
@ensure_csrf_cookie
@csrf_exempt
def create_contact_message(request, data: ContactCreateSchema):
    """
    Create contact message
    """
    response = Contact.objects.create(
        full_name=data.full_name,
        phone=data.phone,
        message=data.message,
    )
    return response


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
    response = Book.objects.all()
    return response


@router.post('/testimony/', response=List[TestimonySchema])
@ensure_csrf_cookie
@csrf_exempt
def create_testimony(request, data: TestimonyCreateSchema):
    """
    Create Testimonies
    """
    response = Testimony.objects.create(
        first_name=data.first_name,
        last_name=data.last_name,
        designation=data.designation,
        tesitmony=data.tesitmony,
    )
    return response


@router.get('/testimonies/', response=List[TestimonySchema])
@paginate(PageNumberPagination, page_size=6)
def get_testimonies(request):
    """
    Get a list of all testtimonies
    """
    testimonies = Testimony.objects.all()
    return testimonies


@router.get('/post/upcoming_service', response=List[UpcomingServiceSchema])
@paginate(PageNumberPagination, page_size=6)
def get_upcoming_service(request):
    """
    Get a list of all upcomming service
    """
    response = UpcomingService.objects.all()
    return response


@router.get('/post/epistles', response=List[EpistleOfMonthSchema])
@paginate(PageNumberPagination, page_size=4)
def get_epistles(request):
    """
    Get a list of all epistles
    """
    response = EpistleOfMonth.objects.all()
    return response


@router.get('/post/word_of_day/all', response=List[WordOfDaySchema])
@paginate(PageNumberPagination, page_size=4)
def get_word_of_day(request):
    """
    Get a list of all word of the day
    """
    response = WordOfDay.objects.all()
    return response


@router.get('/post/verse_of_day/all', response=List[VerseOfDaySchema])
@paginate(PageNumberPagination, page_size=4)
def get_verse_of_day(request):
    """
    Get a list of all verse of the day
    """
    response = VerseOfDay.objects.all()
    return response


@router.get(
    '/bookmarks/upcoming_service/all', response=List[BookmarkedUpcomingServiceSchema]
)
@paginate(PageNumberPagination, page_size=6)
def get_bookmarks_upcoming_service(request):
    """
    Get a list of all bookmarked upcoming services
    """
    response = BookmarkedUpcomingService.objects.all()
    return response


@router.get(
    '/bookmarks/epistle_of_month/all', response=List[BookmarkedEpistleOfMonthSchema]
)
@paginate(PageNumberPagination, page_size=4)
def get_bookmarks_epistle_of_month(request):
    """
    Get a list of all bookmarked epistles of the month
    """
    response = BookmarkedEpistleOfMonth.objects.all()
    return response


@router.get('/bookmarks/word_of_day/all', response=List[BookmarkedWordOfDaySchema])
@paginate(PageNumberPagination, page_size=4)
def get_bookmarks_word_of_day(request):
    """
    Get a list of all bookmarked words of the day
    """
    response = BookmarkedWordOfDay.objects.all()
    return response


@router.get('/bookmarks/verse_of_day/all', response=List[BookmarkedVerseOfDaySchema])
@paginate(PageNumberPagination, page_size=4)
def get_bookmarks_verse_of_day(request):
    """
    Get a list of all bookmarked verses of the day
    """
    response = BookmarkedVerseOfDay.objects.all()
    return response


@router.get('/media/save/later/all', response=List[SaveForLaterMediaSchema])
@paginate(PageNumberPagination, page_size=6)
def get_saved_media(request):
    """
    Get a list of all bookmarked saved medias
    """
    response = SaveForLaterMedia.objects.all()
    return response


@router.get('/search', response=List[dict])
@paginate(PageNumberPagination, page_size=6)
def get_search(request, category: str = '', search: str = ''):
    """
    Get a list of media (audio or video), books, epistles, or testimonies,
    optionally filtered by category and search keywords.

    Query Parameters:
    - **category**: Can be either "media", "books", "epistles", or "testimonies" (case-insensitive).
    - **search**: search keyword (case-insensitive).
    """
    response = {}

    if category != '' and search != '':
        if category == 'media':
            sermons = search_sermons(search)
            response['medias'] = MediaSchema.from_orm_many(sermons).dict()

        elif category == 'books':
            books = search_books(search)
            response['books'] = BookSchema.from_orm_many(books).dict()

        elif category == 'epistles':
            epistles = search_epistles(search)
            response['epistles'] = EpistleOfMonthSchema.from_orm_many(epistles).dict()

        elif category == 'testimonies':
            testimonies = search_testimonies(search)
            response['testimonies'] = TestimonySchema.from_orm_many(testimonies).dict()

        else:
            return {
                'error': "Invalid category. Choose from 'media', 'books', 'epistles' or 'testimonies'."
            }
    else:
        return {
            'error': "Fields cannot be empty. Category choices are 'media', 'books', 'epistles', 'testimonies'."  # noqa: E501
        }

    return response
