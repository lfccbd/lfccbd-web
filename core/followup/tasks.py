from django.utils import timezone
from huey import crontab
from huey.contrib.djhuey import db_periodic_task

from core.followup.models.membership import MemberFollowUp
from core.followup.models.sms import SMSTemplates
from core.followup.models.vercode import OutreachVerficationCode
from core.followup.utils.twilio_sms import send_sms


# set task
@db_periodic_task(crontab(hour='*/24'))
def members_birthday_task():
    current_year = timezone.now().year
    current_day = timezone.now().day
    current_month = timezone.now().month

    # get sms template
    sms_template = SMSTemplates.objects.only('sms_message').get(
        template="Member's Birthday"
    )
    # member's birthday
    members = MemberFollowUp.objects.only(
        'phone_number', 'title', 'first_name', 'birthday'
    )

    for member in members:
        full_date_str = f"{member.birthday}/{current_year}"
        converted_date = timezone.datetime.strptime(full_date_str, "%d/%m/%Y").date()

        # Compare day and month
        if converted_date.day == current_day and converted_date.month == current_month:
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
