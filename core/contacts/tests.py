import uuid

from django.test import TestCase
from django.urls import reverse
from model_bakery import baker

from .models import Contact


class MessageModelTest(TestCase):
	def setUp(self):
		# Random UUIDv4
		full_uuid = str(uuid.uuid4()).replace('-', '')
		self.expected_id = full_uuid[:16]

		# Generate a test Message instance
		self.message = baker.make(
			Contact,
			id=self.expected_id,
			full_name='John Doe',
			phone='123-456-7890',
			message='Hello, there!!!',
		)

		# Create a URL for resources
		self.contact_url = reverse('contact')

	def tearDown(self):
		self.message.delete()

	def test_id_field(self):
		self.assertEqual(len(self.message.id), 16)

		# Check for alphanumeric since UUIDv4 produces hexadecimal digits)
		self.assertTrue(self.message.id.isalnum())

		# Chec new UUID
		new_full_uuid = str(uuid.uuid4()).replace('-', '')
		new_expected_id = new_full_uuid[:16]
		self.assertNotEqual(self.message.id, new_expected_id)

	def test_message_creation(self):
		self.assertEqual(self.message.full_name, 'John Doe')
		self.assertEqual(self.message.phone, '123-456-7890')
		self.assertEqual(self.message.message, 'Hello, there!!!')
		self.assertFalse(self.message.has_read)
		self.assertIsNotNone(self.message.date_received)

	def test_testimony_details(self):
		response = self.client.get(self.contact_url)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Contact')
		self.assertTemplateUsed(response, 'pages/contact.html')
