from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
import pgcrypto
from simple_history.models import HistoricalRecords

from core.testimonies.models import generate_custom_id

from .__choices import convert, membership, title

User = get_user_model()


class MemberFollowUp(models.Model):
	id = models.CharField(  # noqa: A003
		default=generate_custom_id,
		editable=False,
		unique=True,
		max_length=20,
		primary_key=True,
	)
	user = models.ForeignKey(
		User,
		on_delete=models.SET_DEFAULT,
		default='1',
		help_text='follow up team who uploaded record',
	)
	followup_type = pgcrypto.EncryptedCharField(
		max_length=100,
		choices=convert,
		default='Firt Timer',
		verbose_name='Follow up type',
	)
	title = pgcrypto.EncryptedCharField(max_length=100, choices=title, default='Mr.')
	first_name = pgcrypto.EncryptedCharField(max_length=100)
	last_name = pgcrypto.EncryptedCharField(max_length=100)
	email = pgcrypto.EncryptedEmailField(null=True, blank=True)
	birthday = pgcrypto.EncryptedDateField(
		max_length=100, help_text='Birthday (dd/mm) eg. 12/12', null=True, blank=True
	)
	phone_number = pgcrypto.EncryptedCharField(max_length=100)
	address = pgcrypto.EncryptedTextField(max_length=100, null=True, blank=True)
	invite_process = pgcrypto.EncryptedTextField(max_length=500, help_text='How did you hear of Winners Intl JHB CBD')
	inviter = pgcrypto.EncryptedCharField(max_length=100, help_text='Who invited you', null=True, blank=True)
	membership = pgcrypto.EncryptedCharField(max_length=100, choices=membership, help_text='Want to be a member')
	prayer = pgcrypto.EncryptedTextField(max_length=2000, help_text='Prayer request', null=True, blank=True)
	current_status = models.TextField(max_length=600, null=True, blank=True, help_text='Current last welfare check')
	history = HistoricalRecords()
	date_received = models.DateTimeField(auto_now_add=True)
	last_updated = models.DateTimeField(default=timezone.now)
	publish = models.BooleanField(default=True, help_text='Make record available for followup')

	def __str__(self):
		return f'{self.first_name} followup'

	class Meta:
		verbose_name = 'Membership Followu Up'
		verbose_name_plural = 'Membership Follow Up'
		ordering = ['-date_received']
