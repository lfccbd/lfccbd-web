from django import forms
from django.conf import settings
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3
import nh3

from .models import PrayerRequest  # type: ignore


# custom char field with nh3 to sanitize input
class Nh3CleanCharField(forms.CharField):
	def __init__(self, *args, **kwargs):
		# allowed tags and attributes
		self.allowed_tags = getattr(settings, 'NH3_ALLOWED_TAGS', {})
		self.allowed_attributes = getattr(settings, 'NH3_ALLOWED_ATTRIBUTES', {})
		super().__init__(*args, **kwargs)

	def clean(self, value):
		# call parent clean method
		value = super().clean(value)

		# Sanitize the value using nh3
		cleaned_value = nh3.clean(value, tags=self.allowed_tags, attributes=self.allowed_attributes)

		return cleaned_value


class PrayerRequestForm(forms.ModelForm):
	first_name = Nh3CleanCharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_name = Nh3CleanCharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
	prayer = Nh3CleanCharField(
		required=True, widget=forms.Textarea(attrs={'placeholder': 'Your Prayer Request', 'class': 'form-control', 'row': 12})
	)
	captcha = ReCaptchaField(widget=ReCaptchaV3())

	class Meta:
		model = PrayerRequest
		fields = ['first_name', 'last_name', 'prayer']

	def clean_message(self):
		user_prayer = self.cleaned_data.get('prayer')

		# Check if the field is empty
		if user_prayer.strip() == '':
			raise forms.ValidationError('Message can not be empty', code='message')
		elif len(user_prayer) > 2000:
			raise forms.ValidationError('Length must be less than 2000 character', code='message')
		return user_prayer
