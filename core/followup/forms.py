from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3
from twilio.rest import Client

from core.contacts.forms import Nh3CleanCharField
from core.project.settings import ENV

from .models.__choices import (
    calling,
    convert,
    current_memeber_status,
    in_church_ask,
    in_church_check_sunday,
    in_church_check_wenesday,
    membership,
    title,
)
from .models.checkup import FollowUpCheckup  # type: ignore
from .models.membership import MemberFollowUp  # type: ignore
from .models.outreach import FollowUpOutreach  # type: ignore
from .models.vercode import OutreachVerficationCode  # type: ignore

# twilio client
auth_token = ENV.config('TWILIO_AUTH_TOKEN')
account_sid = ENV.config('TWILIO_ACCOUNT_SID')
client = Client(account_sid, auth_token)

# update choices
convert = [('Select type', 'Select type')] + convert
title = [('Select title', 'Select title')] + title
calling = [('Select an option', 'Select an option')] + calling
membership = [('Select an option', 'Select an option')] + membership
in_church_ask = [('Select an option', 'Select an option')] + in_church_ask
current_memeber_status = [
    ('Select member status option', 'Select member status option')
] + current_memeber_status
in_church_check_sunday = [
    ('Select checkup option', 'Select checkup option')
] + in_church_check_sunday
in_church_check_wenesday = [
    ('Select checkup option', 'Select checkup option')
] + in_church_check_wenesday


class FollowUpCheckupForm(forms.ModelForm):
    phone_number = Nh3CleanCharField(
        label='Phone Number *',
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': '+2712345678', 'class': 'form-control'}
        ),
    )
    number_was_called = forms.CharField(
        label='Was Number Called Today *',
        required=True,
        widget=forms.Select(choices=calling, attrs={'class': 'form-select'}),
    )
    in_church_last_sunday = forms.CharField(
        label='Was In Church Last Sunday *',
        required=True,
        widget=forms.Select(
            choices=in_church_check_sunday, attrs={'class': 'form-select'}
        ),
    )
    in_church_last_wenesday = forms.CharField(
        label='Was In Church Last Wenesday *',
        required=True,
        widget=forms.Select(
            choices=in_church_check_wenesday, attrs={'class': 'form-select'}
        ),
    )
    prayer = Nh3CleanCharField(
        label='Prayer Request During Call',
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'row': 6}),
    )
    church_next_sunday = forms.CharField(
        label='Will Be In Church Next Sunday *',
        required=True,
        widget=forms.Select(choices=in_church_ask, attrs={'class': 'form-select'}),
    )
    current_status = forms.CharField(
        label='Current Member Status *',
        required=True,
        widget=forms.Select(
            choices=current_memeber_status, attrs={'class': 'form-select'}
        ),
    )

    class Meta:
        model = FollowUpCheckup
        fields = [
            'phone_number',
            'number_was_called',
            'in_church_last_sunday',
            'in_church_last_wenesday',
            'church_next_sunday',
            'current_status',
            'prayer',
        ]

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')

        if phone_number.startswith('+27'):
            phone_number_check = client.lookups.v2.phone_numbers(phone_number).fetch()

            # if number is valid
            if not phone_number_check.valid:
                raise forms.ValidationError('Invalid phone number', code='phone_number')

            elif not MemberFollowUp.objects.filter(phone_number=phone_number).exists():
                raise forms.ValidationError(
                    'Number not in Followup Records',
                    code='phone_number',
                )
        else:
            raise forms.ValidationError(
                'Invalid phone number. Start with country code eg +27',
                code='phone_number',
            )
        return phone_number

    def clean_number_was_called(self):
        selected_number_was_called = self.cleaned_data.get('number_was_called')

        if selected_number_was_called == 'Select an option':
            raise forms.ValidationError(
                'Select a valid option', code='number_was_called'
            )
        return selected_number_was_called

    def clean_in_church_last_sunday(self):
        selected_in_church_last_sunday = self.cleaned_data.get('in_church_last_sunday')

        if selected_in_church_last_sunday == 'Select checkup option':
            raise forms.ValidationError(
                'Select a valid option', code='in_church_last_sunday'
            )
        return selected_in_church_last_sunday

    def clean_in_church_last_wenesday(self):
        selected_in_church_last_wenesday = self.cleaned_data.get(
            'in_church_last_wenesday'
        )

        if selected_in_church_last_wenesday == 'Select checkup option':
            raise forms.ValidationError(
                'Select a valid option', code='in_church_last_wenesday'
            )
        return selected_in_church_last_wenesday

    def clean_church_next_sunday(self):
        selected_church_next_sunday = self.cleaned_data.get('church_next_sunday')

        if selected_church_next_sunday == 'Select an option':
            raise forms.ValidationError(
                'Select a valid option', code='church_next_sunday'
            )
        return selected_church_next_sunday

    def clean_current_status(self):
        selected_current_status = self.cleaned_data.get('current_status')

        if selected_current_status == 'Select an option':
            raise forms.ValidationError('Select a valid option', code='current_status')
        return selected_current_status


class OutreachForm(forms.ModelForm):
    phone_number = Nh3CleanCharField(
        label='Phone Number *',
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'eg +27...', 'class': 'form-control'}
        ),
    )
    full_name = Nh3CleanCharField(
        label='Full Name *',
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter Invite Full Name', 'class': 'form-control'}
        ),
    )
    verification_code = Nh3CleanCharField(
        label='Verification Code *',
        required=True,
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Enter eight(8) digit verification code',
                'class': 'form-control',
            }
        ),
    )

    class Meta:
        model = FollowUpOutreach
        fields = ['phone_number', 'full_name']

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        phone_number_check = client.lookups.v2.phone_numbers(phone_number).fetch()

        # if number is valid
        if not phone_number.startswith('+27'):
            raise forms.ValidationError(
                'Invalid phone number. Start with country code eg +27',
                code='phone_number',
            )
        elif not phone_number_check.valid:
            raise forms.ValidationError(
                'Invalid phone number. Number is incorrect or do not exist',
                code='phone_number',
            )
        return phone_number

    def clean_verification_code(self):
        verification_code = self.cleaned_data.get('verification_code')

        # if number is valid
        if not OutreachVerficationCode.objects.filter(
            code__exact=verification_code, usability=True
        ).exists():
            raise forms.ValidationError(
                'Invalid verification code. Enter valid code.',
                code='verification_code',
            )

        return verification_code

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')

        if full_name == '' or len(full_name) <= 2:
            raise forms.ValidationError('Enter a valid name', code='full_name')
        return full_name


class FollowUpOutreachForm(forms.ModelForm):
    phone_number = Nh3CleanCharField(
        label='Phone Number *',
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'eg +27...', 'class': 'form-control'}
        ),
    )
    full_name = Nh3CleanCharField(
        label='Full Name *',
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter Invite Full Name', 'class': 'form-control'}
        ),
    )
    captcha = ReCaptchaField(widget=ReCaptchaV3())

    class Meta:
        model = FollowUpOutreach
        fields = ['phone_number', 'full_name']

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        phone_number_check = client.lookups.v2.phone_numbers(phone_number).fetch()

        # if number is valid
        if not phone_number.startswith('+27'):
            raise forms.ValidationError(
                'Invalid phone number. Start with country code eg +27',
                code='phone_number',
            )
        elif not phone_number_check.valid:
            raise forms.ValidationError(
                'Invalid phone number. Number is incorrect or do not exist',
                code='phone_number',
            )
        return phone_number

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')

        if full_name == '' or len(full_name) <= 2:
            raise forms.ValidationError('Enter a valid name', code='full_name')
        return full_name


class FollowUpMembershipForm(forms.ModelForm):
    followup_type = forms.CharField(
        required=True,
        widget=forms.Select(choices=convert, attrs={'class': 'form-select'}),
    )
    title = forms.CharField(
        label='Title *',
        required=True,
        widget=forms.Select(choices=title, attrs={'class': 'form-select'}),
    )
    first_name = Nh3CleanCharField(
        label='First Name *',
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'First Name', 'class': 'form-control'}
        ),
    )
    last_name = Nh3CleanCharField(
        label='Last Name *',
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Last Name', 'class': 'form-control'}
        ),
    )
    email = Nh3CleanCharField(
        label='Email',
        required=False,
        widget=forms.EmailInput(
            attrs={'placeholder': 'user@email.com', 'class': 'form-control'}
        ),
    )
    birthday = Nh3CleanCharField(
        label='Birthday',
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'DD/MM eg. 08/12', 'class': 'form-control'}
        ),
    )
    phone_number = Nh3CleanCharField(
        label='Phone Number *',
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': '+27...', 'class': 'form-control'}
        ),
    )
    address = Nh3CleanCharField(
        label='Address',
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'Address', 'class': 'form-control'}
        ),
    )
    invite_process = Nh3CleanCharField(
        label='How Did You Hear of The Church *',
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control', 'row': 6}),
    )
    inviter = Nh3CleanCharField(
        label='Inviter',
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'Name of Inviter', 'class': 'form-control'}
        ),
    )
    membership = forms.CharField(
        label='Become A Member *',
        required=True,
        widget=forms.Select(choices=membership, attrs={'class': 'form-select'}),
    )
    prayer = Nh3CleanCharField(
        label='Prayer Request',
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'row': 6}),
    )

    class Meta:
        model = MemberFollowUp
        fields = [
            'followup_type',
            'title',
            'first_name',
            'last_name',
            'email',
            'birthday',
            'phone_number',
            'address',
            'invite_process',
            'inviter',
            'membership',
            'prayer',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.label:
                field.label = f'<label for="id_{field_name}" class="form-label">{field.label}</label>'

    def clean_followup_type(self):
        selected_followup_type = self.cleaned_data.get('followup_type')

        if selected_followup_type == 'Select type':
            raise forms.ValidationError('Select a valid option', code='followup_type')
        return selected_followup_type

    def clean_title(self):
        selected_title = self.cleaned_data.get('title')

        if selected_title == 'Select an option':
            raise forms.ValidationError('Select a valid option', code='followup_type')
        return selected_title

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == '' or len(first_name) <= 2:
            raise forms.ValidationError('Enter a valid name', code='first_name')
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')

        if last_name == '' or len(last_name) <= 2:
            raise forms.ValidationError('Enter a valid name', code='last_name')
        return last_name

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        phone_number_check = client.lookups.v2.phone_numbers(phone_number).fetch()

        # if number is valid
        if not phone_number.startswith('+27'):
            raise forms.ValidationError(
                'Invalid phone number. Start with country code eg +27',
                code='phone_number',
            )
        elif not phone_number_check.valid:
            raise forms.ValidationError(
                'Invalid phone number. Number is incorrect or do not exist',
                code='phone_number',
            )

        return phone_number

    def clean_membership(self):
        selected_membership = self.cleaned_data.get('membership')

        if selected_membership == 'Select an option':
            raise forms.ValidationError('Select a valid option', code='membership')
        return selected_membership
