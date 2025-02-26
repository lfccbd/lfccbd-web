from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3

from core.contacts.forms import Nh3CleanCharField

from .models import Testimony  # type: ignore


options = (
	('Mr / Mrs / Deacon / Deaconess', 'Mr / Mrs / Deacon / Deaconess'),
	('Mr', 'Mr'),
	('Mrs', 'Mrs'),
	('Deacon', 'Deacon'),
	('Deaconess', 'Deaconess'),
)


class TestimonyForm(forms.ModelForm):
	first_name = Nh3CleanCharField(
		required=True, widget=forms.TextInput(attrs={'placeholder': 'Your First name', 'class': 'form-control'})
	)
	last_name = Nh3CleanCharField(
		required=True, widget=forms.TextInput(attrs={'placeholder': 'Your last name', 'class': 'form-control'})
	)
	designation = forms.CharField(required=True, widget=forms.Select(choices=options, attrs={'class': 'form-select'}))
	title = Nh3CleanCharField(
		required=True, widget=forms.TextInput(attrs={'placeholder': 'Testimony title', 'class': 'form-control'})
	)
	testimony = Nh3CleanCharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control', 'row': 6}))
	location = Nh3CleanCharField(
		required=True, widget=forms.TextInput(attrs={'placeholder': 'Winner Branch or City ', 'class': 'form-control'})
	)
	captcha = ReCaptchaField(widget=ReCaptchaV3())

	class Meta:
		model = Testimony
		fields = ['first_name', 'last_name', 'designation', 'title', 'testimony', 'location']

	def clean_message(self):
		user_tesitmonies = self.cleaned_data.get('testimony')
		# check if the field is empty or
		# length is less or equal to 800
		if user_tesitmonies.strip() == '':
			raise forms.ValidationError('Message can not be empty', code='testimony')
		elif len(user_tesitmonies) > 800:
			raise forms.ValidationError('Length must be less than 800 character', code='testimony')
		return user_tesitmonies

	def clean_designation(self):
		selected_designation = self.cleaned_data.get('designation')

		if selected_designation == 'Mr / Mrs / Deacon / Deaconess':
			raise forms.ValidationError('Select a valid option', code='designation')
		return selected_designation
