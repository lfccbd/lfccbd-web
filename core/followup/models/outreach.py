from django.db import models
from django.utils import timezone
import pgcrypto
from simple_history.models import HistoricalRecords

from core.testimonies.models import generate_custom_id


class FollowUpOutreach(models.Model):
    id = models.CharField(  # noqa: A003
        default=generate_custom_id,
        editable=False,
        unique=True,
        max_length=20,
        primary_key=True,
    )

    phone_number = pgcrypto.EncryptedCharField(
        max_length=100, help_text='phone number from the harvest field'
    )
    full_name = pgcrypto.EncryptedCharField(max_length=100)
    history = HistoricalRecords()
    date_received = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(default=timezone.now)
    publish = models.BooleanField(default=True, help_text='make available for followup')

    def __str__(self):
        return f'{self.full_name} followup'

    class Meta:
        verbose_name = 'Follow Up Outreach'
        verbose_name_plural = 'Follow Up Outreach'
        ordering = ['-date_received']
