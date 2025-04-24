from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
import pgcrypto
from simple_history.models import HistoricalRecords

from core.followup.models.membership import MemberFollowUp
from core.testimonies.models import generate_custom_id

from .__choices import (
    calling,
    current_memeber_status,
    in_church_ask,
    in_church_check_sunday,
    in_church_check_wenesday,
)

User = get_user_model()


class FollowUpCheckup(models.Model):
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
    member_profile = models.ForeignKey(MemberFollowUp, on_delete=models.CASCADE)
    number_was_called = pgcrypto.EncryptedCharField(
        max_length=100, choices=calling, default='Yes', verbose_name='Was number called'
    )
    in_church_last_sunday = pgcrypto.EncryptedCharField(
        max_length=100,
        choices=in_church_check_sunday,
        default='Yes, was in Church last Sunday',
        verbose_name='Was in Church last Sunday',
    )
    in_church_last_wenesday = pgcrypto.EncryptedCharField(
        max_length=100,
        choices=in_church_check_wenesday,
        default='Yes, was in Church last Wenesday',
        verbose_name='Was in Church last Wenesday',
    )
    church_next_sunday = pgcrypto.EncryptedCharField(
        max_length=100,
        choices=in_church_ask,
        default='Yes',
        verbose_name='Will be in Church coming Sunday',
    )
    current_status = pgcrypto.EncryptedCharField(
        max_length=200, choices=current_memeber_status, default='Hail and healthy'
    )
    prayer = pgcrypto.EncryptedTextField(max_length=500, null=True, blank=True, help_text='Prayer request')
    history = HistoricalRecords()
    date_received = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(default=timezone.now)
    publish = models.BooleanField(default=True, help_text='make available for followup')

    def __str__(self):
        return f'{self.member_profile.first_name} Followed Up'

    class Meta:
        verbose_name = 'Follow Up Check'
        verbose_name_plural = 'Follow Up Check'
        ordering = ['-date_received']
