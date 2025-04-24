from django.db.models import Q
from django.utils import timezone
from followup.models.membership import MemberFollowUp
from huey import crontab
from huey.contrib.djhuey import db_periodic_task

from core.followup.models.sms import SMSTemplates
from core.followup.utils.twilio_sms import send_sms


# set task
@db_periodic_task(crontab(hour='*/24'))
def members_birthday_task():
	current_day = timezone.now().day
	current_month = timezone.now().month

	# get sms template
	sms_template = SMSTemplates.objects.only('sms_message').get(template='Birthday')
	# member's birthday
	members = MemberFollowUp.objects.only('phone_number', 'title', 'first_name', 'birthday').filter(
		Q(birthday__day=current_day) & Q(birthday__month=current_month)
	)

	for member in members:
		# send sms
		send_sms(
			member.phone_number, f'Happy Birthday, {member.title} {member.first_name}. {sms_template.sms_message}'
		)
