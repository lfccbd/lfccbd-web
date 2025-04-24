from twilio.rest import Client

from core.project.settings import ENV

account_sid = ENV.config('TWILIO_ACCOUNT_SID')
auth_token = ENV.config('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)


def send_sms(phone_number, sms_message):
	# send sms to only SA numbers
	if phone_number.startswith('+27'):
		client.messages.create(
			body=sms_message,
			from_=ENV.config('TWILIO_PHONE_NUMBER'),
			to=phone_number,
		)
	else:
		pass
