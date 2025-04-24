from django.db.models import Q
from django.utils import timezone
from core.followup.models.membership import MemberFollowUp
from huey import crontab
from huey.contrib.djhuey import db_periodic_task
from core.followup.models.sms import SMSTemplates
from core.followup.utils.twilio_sms import send_sms

from core.followup.models.vercode import OutreachVerficationCode


# set task
@db_periodic_task(crontab(hour='*/24'))
def members_birthday_task():
    current_day = timezone.now().day
    current_month = timezone.now().month

    # get sms template
    sms_template = SMSTemplates.objects.only('sms_message').get(template='Birthday')
    # member's birthday
    members = MemberFollowUp.objects.only(
        'phone_number', 'title', 'first_name', 'birthday'
    ).filter(Q(birthday__day=current_day) & Q(birthday__month=current_month))

    for member in members:
        # send sms
        send_sms(
            member.phone_number,
            f'Happy Birthday, {member.title} {member.first_name}. {sms_template.sms_message}',
        )


# set task
@db_periodic_task(crontab(minute='*/1'))
def outreach_verification_task():
    if OutreachVerficationCode.objects.filter(usability=True).exists():
        ver_code = OutreachVerficationCode.objects.only('expiration', 'usability').get(
            usability=True
        )
        if ver_code.expiration < timezone.now():
            ver_code.usability = False
            ver_code.save(update_fields=['usability'])
