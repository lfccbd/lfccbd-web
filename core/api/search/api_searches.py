from django.db.models import Q

from core.post.models import EpistleOfMonth
from core.resources.models import Books, Media
from core.testimonies.models import Testimony


def search_books(search=None):
	books = Books.objects.all()

	if search:
		books = books.filter(
			(Q(file_title__icontains=search) & Q(author__icontains=search))
			| Q(file_title__icontains=search)
			| Q(author__icontain=search)
		)

	return books


def search_sermons(search=None):
	sermons = Media.objects.all()

	if search:
		sermons = sermons.filter(
			(Q(file_title__icontains=search) & Q(service_icontains=search))
			| Q(file_title__icontains=search)
			| Q(service__icontain=search)
		)

	return sermons


def search_epistles(search=None):
	epistles = EpistleOfMonth.objects.all()

	if search:
		epistles = epistles.filter(
			(Q(epistle_message_theme__icontains=search) & Q(epistle_message_topic_icontains=search))
			| Q(epistle_message_theme__icontains=search)
			| Q(epistle_message_topic_icontains=search)
		)

	return epistles


def search_testimonies(search=None):
	epistles = Testimony.objects.all()

	if search:
		epistles = epistles.filter(tesitmony__icontains=search)

	return epistles
