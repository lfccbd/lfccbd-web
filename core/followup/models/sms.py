from django.db import models
from django.utils import timezone
from simple_history.models import HistoricalRecords

from core.testimonies.models import generate_custom_id

from .__choices import sms_choices


class SMSTemplates(models.Model):
    id = models.CharField(  # noqa: A003
        default=generate_custom_id,
        editable=False,
        unique=True,
        max_length=20,
        primary_key=True,
    )

    template = models.CharField(
        max_length=100,
        choices=sms_choices,
        default='Was in Church',
        verbose_name='SMS message template to check',
    )
    sms_message = models.TextField(max_length=2000)
    history = HistoricalRecords()
    date_received = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(default=timezone.now)
    publish = models.BooleanField(default=True, help_text='make available for followup')

    def __str__(self):
        return f'{self.template} followup'

    class Meta:
        verbose_name = 'SMS Template'
        verbose_name_plural = 'SMS Template'
        ordering = ['-date_received']
