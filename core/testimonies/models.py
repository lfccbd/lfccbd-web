import uuid

from django.db import models
from django.utils import timezone
import pgcrypto
from simple_history.models import HistoricalRecords


def generate_custom_id():
	# generate a UUID and remove hyphens
	full_uuid = str(uuid.uuid4()).replace('-', '')
	# take the first 15 characters of the UUID
	custom_id = full_uuid[:16]
	return custom_id


designation_choices = (
	('Mr', 'Mr'),
	('Mrs', 'Mrs'),
	('Deacon', 'Deacon'),
	('Deaconess', 'Deaconess'),
)


class Testimony(models.Model):
	id = models.CharField(  # noqa: A003
		default=generate_custom_id, editable=False, unique=True, max_length=20, primary_key=True
	)
	first_name = pgcrypto.EncryptedCharField(max_length=100)
	last_name = pgcrypto.EncryptedCharField(max_length=100)
	designation = pgcrypto.EncryptedCharField(max_length=254, choices=designation_choices, default='Mrs')
	title = pgcrypto.EncryptedTextField(max_length=200, null=True, blank=True)
	testimony = pgcrypto.EncryptedTextField(max_length=1000)
	location = pgcrypto.EncryptedCharField(
		max_length=200, null=True, blank=True, verbose_name='Church Branch/Location'
	)
	publish = models.BooleanField(default=True)
	history = HistoricalRecords()
	date_received = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return f'{self.designation} {self.first_name} {self.last_name}'

	class Meta:
		verbose_name = 'Testimony'
		verbose_name_plural = 'Testimonies'
		ordering = ['-date_received']
