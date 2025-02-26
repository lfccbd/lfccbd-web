from django import forms
from django.conf import settings
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3
import nh3

from .models import Contact  # type: ignore


# custom charfield with nh3 to sanitize input
class Nh3CleanCharField(forms.CharField):
	def __init__(self, *args, **kwargs):
		# allowed tags and attributes
		self.allowed_tags = getattr(settings, 'NH3_ALLOWED_TAGS', {})
		self.allowed_attributes = getattr(settings, 'NH3_ALLOWED_ATTRIBUTES', {})
		super().__init__(*args, **kwargs)

	def clean(self, value):
		# call parrent clean method
		value = super().clean(value)

		# Sanitize the value using nh3
		cleaned_value = nh3.clean(value, tags=self.allowed_tags, attributes=self.allowed_attributes)

		return cleaned_value


class UserContactForm(forms.ModelForm):
	full_name = Nh3CleanCharField(
		required=True, widget=forms.TextInput(attrs={'placeholder': 'Full Name', 'class': 'form-control'})
	)
	phone = forms.IntegerField(
		required=True, widget=forms.TextInput(attrs={'placeholder': 'Phone', 'class': 'form-control'})
	)
	message = Nh3CleanCharField(
		required=True, widget=forms.Textarea(attrs={'placeholder': 'Your Message', 'class': 'form-control', 'row': 8})
	)
	captcha = ReCaptchaField(widget=ReCaptchaV3())

	class Meta:
		model = Contact
		fields = ['full_name', 'phone', 'message']

	def clean_message(self):
		user_message = self.cleaned_data.get('message')

		# Check if the field is empty
		if user_message.strip() == '':
			raise forms.ValidationError('Message can not be empty', code='message')
		elif len(user_message) > 500:
			raise forms.ValidationError('Length must be less than 500 character', code='message')
		return user_message
