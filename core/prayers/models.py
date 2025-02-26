from django.db import models
from django.utils import timezone
import pgcrypto
from simple_history.models import HistoricalRecords

from core.testimonies.models import generate_custom_id


class PrayerRequest(models.Model):
	id = models.CharField(  # noqa: A003
		default=generate_custom_id, editable=False, unique=True, max_length=20, primary_key=True
	)
	first_name = pgcrypto.EncryptedCharField(max_length=100)
	last_name = pgcrypto.EncryptedCharField(max_length=100)
	prayer = pgcrypto.EncryptedTextField(max_length=2000, help_text='request')
	history = HistoricalRecords()
	date_received = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return f'{self.first_name} prayer request'

	class Meta:
		verbose_name = 'Prayer Request'
		verbose_name_plural = 'Prayer Requests'
		ordering = ['-date_received']
