from django.db.models.signals import post_save
from django.dispatch import receiver

from core.followup.models.sms import SMSTemplates
from core.followup.utils.twilio_sms import send_sms  # type: ignore

from .models.checkup import FollowUpCheckup
from .models.membership import MemberFollowUp
from .models.outreach import FollowUpOutreach


@receiver(post_save, sender=FollowUpCheckup)
def checkup_sms(sender, instance, created, **kwargs):
	# send sms only on create
	if created:
		# get instance
		call_status = instance.number_was_called
		sunday_checkup = instance.in_church_last_sunday.lower()
		wenesday_checkup = instance.in_church_last_wenesday
		status_checkup = instance.current_status
		first_name = instance.member_profile.first_name
		phone_number = instance.member_profile.phone_number

		#
		if call_status == 'Yes':
			if 'sick' in sunday_checkup or 'sick' in wenesday_checkup or 'sick' in status_checkup:
				# get sms template
				sms_template = SMSTemplates.objects.only('sms_message').get(template='Currently Sick')
				# send sms
				send_sms(phone_number, f'Hi, {first_name}. {sms_template.sms_message}')

			elif 'travel' in sunday_checkup or 'travel' in wenesday_checkup or 'travelled' in status_checkup:
				# get sms template
				sms_template = SMSTemplates.objects.only('sms_message').get(
					template='Travelled, currently out of town'
				)
				# send sms
				send_sms(phone_number, f'Hi, {first_name}. {sms_template.sms_message}')

			elif 'exam' in sunday_checkup or 'exam' in wenesday_checkup or 'exam' in status_checkup:
				# get sms template
				sms_template = SMSTemplates.objects.only('sms_message').get(template='Writing an exam')
				# send sms
				send_sms(phone_number, f'Hi, {first_name}. {sms_template.sms_message}')

			elif 'work' in sunday_checkup or 'work' in wenesday_checkup or 'work' in status_checkup:
				# get sms template
				sms_template = SMSTemplates.objects.only('sms_message').get(template='Busy at work')
				# send sms
				send_sms(phone_number, f'Hi, {first_name}. {sms_template.sms_message}')

			elif 'Yes, was in Church' in wenesday_checkup or 'Yes, was in Church' in sunday_checkup:
				# get sms template
				sms_template = SMSTemplates.objects.only('sms_message').get(template='Was in Church')
				# send sms
				send_sms(phone_number, f'Hi, {first_name}. {sms_template.sms_message}')

		elif call_status == 'No' or call_status == 'Not Reachable':
			# get sms template
			sms_template = SMSTemplates.objects.only('sms_message').get(template='Not reaachable number')
			# send sms
			send_sms(phone_number, f'Hi, {first_name}. {sms_template.sms_message}')

		elif call_status == 'Wrong Number':
			# check if number exist in followup record
			if MemberFollowUp.objects.filter(phone_number=phone_number).exists():
				# delete the record
				MemberFollowUp.objects.filter(phone_number=phone_number).delete()
			else:
				pass


@receiver(post_save, sender=FollowUpOutreach)
def outreach_sms(sender, instance, created, **kwargs):
	# send sms only on create
	if created:
		# get instance
		full_name = instance.full_name
		phone_number = instance.phone_number

		# get sms template
		sms_template = SMSTemplates.objects.only('sms_message').get(template='Outreach')

		# send sms
		send_sms(phone_number, f'A pleasant day, {full_name}. {sms_template.sms_message}')


@receiver(post_save, sender=MemberFollowUp)
def service_followup_sms(sender, instance, created, **kwargs):
	# send sms only on create
	if created:
		# get instance
		title = instance.title
		first_name = instance.first_name
		phone_number = instance.phone_number

		# get sms template
		sms_template = SMSTemplates.objects.only('sms_message').get(template='Sunday Church Service')

		# send sms
		send_sms(phone_number, f'A pleasant day, {title} {first_name}. {sms_template.sms_message}')
