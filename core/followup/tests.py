from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from django.test import TestCase
from django.urls import reverse

from core.followup.models.vercode import OutreachVerficationCode

User = get_user_model()


class CheckupViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='testuser@gmail.com', password='password') # noqa: S106, E261

        # login user
        self.client.login(email='testuser@gmail.com', password='password')  # noqa: S106
        self.url = reverse('followup')

        # create verification code
        OutreachVerficationCode.objects.create(code=1012345)

        self.post_data = {
            'form_section': 'outreach_form',
            'phone_number': '+27111111111',
            'full_name': 'John Deo',
            'verification_code': 1012345,
        }

    def test_get_request(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forms/followup.html')

    def test_post_invalid_phone_data(self):
        post_data = self.post_data.copy()

        response = self.client.post(self.url, post_data)
        self.assertContains(
            response, 'Invalid phone number. Number is incorrect or do not exist'
        )

    def test_error_message(self):
        response = self.client.post(self.url, self.post_data)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]), 'Invalid Form Field(s). All fields are required.'
        )
