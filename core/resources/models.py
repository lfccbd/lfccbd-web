from autoslug import AutoSlugField
from django.db import models
from django.utils import timezone
from simple_history.models import HistoricalRecords

from core.testimonies.models import generate_custom_id

sermon_type = [
	('Audio', 'Audio'),
	('Video', 'Video'),
]


class ImageSliders(models.Model):
	id = models.CharField(  # noqa: A003
		default=generate_custom_id, editable=False, unique=True, max_length=20, primary_key=True
	)
	image_1_text = models.CharField(max_length=300)
	image_1 = models.ImageField(upload_to='resources/sliders/', help_text='slider image')
	image_2_text = models.CharField(max_length=300)
	image_2 = models.ImageField(upload_to='resources/sliders/', help_text='slider image')
	image_3_text = models.CharField(max_length=300)
	image_3 = models.ImageField(upload_to='resources/sliders/', help_text='slider image')
	image_4_text = models.CharField(max_length=300)
	image_4 = models.ImageField(upload_to='resources/sliders/', help_text='slider image')
	history = HistoricalRecords()
	date_created = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Site Image Sliders'
		verbose_name_plural = 'Site Image Sliders'
		ordering = ['-date_created']


class Media(models.Model):
	id = models.CharField(  # noqa: A003
		default=generate_custom_id, editable=False, unique=True, max_length=20, primary_key=True
	)
	slug = AutoSlugField(populate_from='title', unique_with=['id'], editable=False)
	file_title = models.CharField(max_length=200)
	category = models.CharField(max_length=50, default='sermons', editable=False)
	sermon_type = models.CharField(max_length=100, choices=sermon_type, default='Audio', help_text='file type')
	service = models.CharField(max_length=200, help_text='service name in which message was preached')
	message_date = models.DateTimeField(help_text='date message was preached')
	reource_file = models.FileField(upload_to='resources/sermons')
	view_count = models.IntegerField(default=0, help_text='number of times message has been listened to')
	publish = models.BooleanField(default=True, help_text='make visible on site')
	history = HistoricalRecords()
	date_created = models.DateTimeField(auto_now_add=True)
	last_updated = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.file_title

	class Meta:
		verbose_name = 'Media'
		verbose_name_plural = 'Media'
		ordering = ['-date_created']


class Books(models.Model):
	id = models.CharField(  # noqa: A003
		default=generate_custom_id, editable=False, unique=True, max_length=20, primary_key=True
	)
	slug = AutoSlugField(populate_from='title', unique_with=['id'], editable=False)
	file_title = models.CharField(max_length=200)
	category = models.CharField(max_length=50, default='books', editable=False)
	author = models.CharField(max_length=200, help_text='service name in which message was preached')
	publish_year = models.IntegerField()
	publisher = models.CharField(max_length=200)
	foreward = models.TextField(max_length=2000)
	isbn = models.CharField(max_length=200, verbose_name='ISBN')
	featured_image = models.ImageField(upload_to='resources/books/', help_text='main image')
	image_1 = models.ImageField(upload_to='resources/books/', help_text='gallery image')
	image_2 = models.ImageField(upload_to='resources/books/', help_text='gallery image')
	view_count = models.IntegerField(default=0, help_text='number of times book has been viewed')
	publish = models.BooleanField(default=True, help_text='make visible on site')
	history = HistoricalRecords()
	date_created = models.DateTimeField(auto_now_add=True)
	last_updated = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.file_title

	class Meta:
		verbose_name = 'Books'
		verbose_name_plural = 'Books'
		ordering = ['-date_created']
