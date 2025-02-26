from autoslug import AutoSlugField
from django.db import models
from django.utils import timezone
from django_prose_editor.fields import ProseEditorField
from simple_history.models import HistoricalRecords

from core.resources.models import Media
from core.testimonies.models import generate_custom_id


class UpcomingService(models.Model):
	id = models.CharField(  # noqa: A003
		default=generate_custom_id,
		editable=False,
		unique=True,
		max_length=20,
		primary_key=True,
	)
	slug = AutoSlugField(populate_from='service_theme', unique_with=['id'], editable=False)
	service_theme = models.CharField(max_length=300)
	service_date_time = models.DateTimeField()
	service_description = ProseEditorField(max_length=2000)
	service_image = models.ImageField(upload_to='resources/service/', help_text='upcoming service image')
	history = HistoricalRecords()
	publish = models.BooleanField(default=True, help_text='make visible on site')
	date_created = models.DateTimeField(auto_now_add=True)
	last_updated = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.service_theme

	class Meta:
		verbose_name = 'Upcoming Service'
		verbose_name_plural = 'Upcoming Service'
		ordering = ['-date_created']


class EpistleOfMonth(models.Model):
	id = models.CharField(  # noqa: A003
		default=generate_custom_id,
		editable=False,
		unique=True,
		max_length=20,
		primary_key=True,
	)
	slug = AutoSlugField(populate_from='epistle_message_theme', unique_with=['id'], editable=False)
	epistle_message_theme = models.CharField(max_length=300)
	epistle_message_topic = models.CharField(max_length=300)
	epistle_message = ProseEditorField(max_length=5000)
	epistle_image = models.ImageField(upload_to='resources/epistle/', help_text='epistle image')
	history = HistoricalRecords()
	publish = models.BooleanField(default=True, help_text='make visible on site')
	date_created = models.DateTimeField(auto_now_add=True)
	last_updated = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.epistle_message_theme

	class Meta:
		verbose_name = 'Epistle Of The Month'
		verbose_name_plural = 'Epistle Of The Month'
		ordering = ['-date_created']


class WordOfDay(models.Model):
	id = models.CharField(  # noqa: A003
		default=generate_custom_id,
		editable=False,
		unique=True,
		max_length=20,
		primary_key=True,
	)
	slug = AutoSlugField(populate_from='message_topic', unique_with=['id'], editable=False)
	message_topic = models.CharField(max_length=300)
	message_for_day = models.DateField(default=timezone.now)
	message = ProseEditorField(max_length=5000)
	message_image = models.ImageField(upload_to='resources/WOD/', help_text='message image')
	history = HistoricalRecords()
	publish = models.BooleanField(default=True, help_text='make visible on site')
	date_created = models.DateTimeField(auto_now_add=True)
	last_updated = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.message_topic

	class Meta:
		verbose_name = 'Word Of The Day'
		verbose_name_plural = 'Word Of The Day'
		ordering = ['-date_created']


class VerseOfDay(models.Model):
	id = models.CharField(  # noqa: A003
		default=generate_custom_id,
		editable=False,
		unique=True,
		max_length=20,
		primary_key=True,
	)
	slug = AutoSlugField(populate_from='verse', unique_with=['id'], editable=False)
	verse = models.CharField(max_length=300)
	verse_for_day = models.DateField(default=timezone.now)
	message = ProseEditorField(max_length=5000)
	message_image = models.ImageField(upload_to='resources/VOD/', help_text='verse image')
	history = HistoricalRecords()
	publish = models.BooleanField(default=True, help_text='make visible on site')
	date_created = models.DateTimeField(auto_now_add=True)
	last_updated = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return f'Verse: {self.verse}'

	class Meta:
		verbose_name = 'Verse Of The Day'
		verbose_name_plural = 'Verse Of The Day'
		ordering = ['-date_created']


class BookmarkedUpcomingService(models.Model):
	bookmark_id = models.CharField(  # noqa: A003
		default=generate_custom_id,
		editable=False,
		unique=True,
		max_length=20,
		primary_key=True,
	)
	item_bookmarked = models.ForeignKey('UpcomingService', on_delete=models.CASCADE)
	history = HistoricalRecords()
	publish = models.BooleanField(default=True, help_text='make visible on site')
	date_created = models.DateTimeField(auto_now_add=True)
	last_updated = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.item_bookmarked.service_theme

	class Meta:
		verbose_name = 'Bookmarked Upcoming Service'
		verbose_name_plural = 'Bookmarked Upcoming Service'
		ordering = ['-date_created']


class BookmarkedEpistleOfMonth(models.Model):
	bookmark_id = models.CharField(  # noqa: A003
		default=generate_custom_id,
		editable=False,
		unique=True,
		max_length=20,
		primary_key=True,
	)
	item_bookmarked = models.ForeignKey('EpistleOfMonth', on_delete=models.CASCADE)
	history = HistoricalRecords()
	publish = models.BooleanField(default=True, help_text='make visible on site')
	date_created = models.DateTimeField(auto_now_add=True)
	last_updated = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.item_bookmarked.epistle_message_theme

	class Meta:
		verbose_name = 'Bookmarked Epistle Of The Month'
		verbose_name_plural = 'Bookmarked Epistle Of The Month'
		ordering = ['-date_created']


class BookmarkedWordOfDay(models.Model):
	bookmark_id = models.CharField(  # noqa: A003
		default=generate_custom_id,
		editable=False,
		unique=True,
		max_length=20,
		primary_key=True,
	)
	item_bookmarked = models.ForeignKey('WordOfDay', on_delete=models.CASCADE)
	history = HistoricalRecords()
	publish = models.BooleanField(default=True, help_text='make visible on site')
	date_created = models.DateTimeField(auto_now_add=True)
	last_updated = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.item_bookmarked.message_topic

	class Meta:
		verbose_name = 'Bookmarked Word Of The Day'
		verbose_name_plural = 'Bookmarked Word Of The Day'
		ordering = ['-date_created']


class BookmarkedVerseOfDay(models.Model):
	bookmark_id = models.CharField(  # noqa: A003
		default=generate_custom_id,
		editable=False,
		unique=True,
		max_length=20,
		primary_key=True,
	)
	item_bookmarked = models.ForeignKey('WordOfDay', on_delete=models.CASCADE)
	history = HistoricalRecords()
	publish = models.BooleanField(default=True, help_text='make visible on site')
	date_created = models.DateTimeField(auto_now_add=True)
	last_updated = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.item_bookmarked.verse

	class Meta:
		verbose_name = 'Bookmarked Verse Of The Day'
		verbose_name_plural = 'Bookmarked Verse Of The Day'
		ordering = ['-date_created']


class SaveForLaterMedia(models.Model):
	id = models.CharField(  # noqa: A003
		default=generate_custom_id,
		editable=False,
		unique=True,
		max_length=20,
		primary_key=True,
	)
	media_saveded = models.ForeignKey(Media, on_delete=models.CASCADE)
	history = HistoricalRecords()
	publish = models.BooleanField(default=True, help_text='make visible on site')
	date_created = models.DateTimeField(auto_now_add=True)
	last_updated = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.item_bookmarked.file_title

	class Meta:
		verbose_name = 'Saved Media'
		verbose_name_plural = 'Saved Media'
		ordering = ['-date_created']


class UpcomingEvent(models.Model):
	id = models.CharField(  # noqa: A003
		default=generate_custom_id, editable=False, unique=True, max_length=20, primary_key=True
	)
	slug = AutoSlugField(populate_from='event_theme', unique_with=['id'], editable=False)
	event_theme = models.CharField(max_length=100)
	event_date_time = models.DateTimeField()
	event_description = ProseEditorField(max_length=340)
	event_link = models.URLField(null=True, blank=True)
	history = HistoricalRecords()
	publish = models.BooleanField(default=True, help_text='make visible on site')
	date_created = models.DateTimeField(auto_now_add=True)
	last_updated = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.event_theme

	class Meta:
		verbose_name = 'Upcoming Event'
		verbose_name_plural = 'Upcoming Event'
		ordering = ['-date_created']
