from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3


class UserLoginForm(forms.Form):
    email = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'user_email',
                'class': 'form-control',
                'placeholder': 'Enter Email Address',
            }
        ),
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'id': 'user_password',
                'class': 'form-control',
                'placeholder': '*****',
            }
        ),
    )

    captcha = ReCaptchaField(widget=ReCaptchaV3())
