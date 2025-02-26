import uuid

from django.test import TestCase
from django.urls import reverse
from model_bakery import baker

from .models import PrayerRequest


class MessageModelTest(TestCase):
	def setUp(self):
		# Random UUIDv4
		full_uuid = str(uuid.uuid4()).replace('-', '')
		self.expected_id = full_uuid[:16]

		# Generate a test Message instance
		self.prayer = baker.make(
			PrayerRequest,
			id=self.expected_id,
			first_name='John',
			last_name='Deo',
			prayer='Thank you Lord.',
		)

		# Create a URL for resources
		self.prayer_url = reverse('prayer_request')

	def tearDown(self):
		self.prayer.delete()

	def test_id_field(self):
		self.assertEqual(len(self.prayer.id), 16)

		# Check for alphanumeric since UUIDv4 produces hexadecimal digits)
		self.assertTrue(self.prayer.id.isalnum())

		# Chec new UUID
		new_full_uuid = str(uuid.uuid4()).replace('-', '')
		new_expected_id = new_full_uuid[:16]
		self.assertNotEqual(self.prayer.id, new_expected_id)

	def test_message_creation(self):
		self.assertEqual(self.prayer.first_name, 'John')
		self.assertEqual(self.prayer.last_name, 'Deo')
		self.assertEqual(self.prayer.prayer, 'Thank you Lord.')
		self.assertIsNotNone(self.prayer.date_received)

	def test_testimony_details(self):
		response = self.client.get(self.prayer_url)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Prayer')
		self.assertTemplateUsed(response, 'forms/prayer-request.html')
