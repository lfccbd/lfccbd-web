import secrets

from django.db import models
from django.utils import timezone
import pgcrypto
from simple_history.models import HistoricalRecords

from core.testimonies.models import generate_custom_id


class OutreachVerficationCode(models.Model):
    id = models.CharField(  # noqa: A003
        default=generate_custom_id,
        editable=False,
        unique=True,
        max_length=20,
        primary_key=True,
    )
    code = pgcrypto.EncryptedIntegerField(
        default=0,
        null=True,
        blank=True,
        help_text='verification code will auto generate',
        editable=False,
    )
    history = HistoricalRecords()
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(default=timezone.now)
    usability = models.BooleanField(default=True, help_text='mark code as usable')
    expiration = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Outreach Verification code for {self.date_created.date}'

    class Meta:
        verbose_name = 'Outreach Ver Code'
        verbose_name_plural = 'Outreach Ver Codes'
        ordering = ['-date_created']

    def save(self, *args, **kwargs):
        if self.code == 0:
            self.code = secrets.randbelow(10**8)
        return super().save(self, *args, **kwargs)
