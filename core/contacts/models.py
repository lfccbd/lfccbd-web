from django.db import models
from django.utils import timezone
import pgcrypto
from simple_history.models import HistoricalRecords

from core.testimonies.models import generate_custom_id


class Contact(models.Model):
	id = models.CharField(  # noqa: A003
		default=generate_custom_id, editable=False, unique=True, max_length=20, primary_key=True
	)
	full_name = pgcrypto.EncryptedCharField(max_length=100)
	phone = pgcrypto.EncryptedCharField(max_length=254)
	message = pgcrypto.EncryptedTextField(max_length=500)
	has_read = models.BooleanField(default=False, help_text='admin has read message')
	history = HistoricalRecords()
	date_received = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.full_name

	class Meta:
		verbose_name = 'Contact'
		verbose_name_plural = 'Contacts'
		ordering = ['-date_received']
