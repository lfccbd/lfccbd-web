import uuid

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from model_bakery import baker

from .models import Testimony


class TestimonyModelTest(TestCase):
	def setUp(self):
		# random UUIDv4
		full_uuid = str(uuid.uuid4()).replace('-', '')
		self.expected_id = full_uuid[:16]

		# create instance
		self.testimony = baker.make(
			Testimony,
			id=self.expected_id,
			first_name='John',
			last_name='Doe',
			designation='Deacon',
			title='',
			testimony='God did it.',
			location='JHB CBD',
			date_received=timezone.now(),
		)

		# create a URL for resources
		self.testimony_url = reverse('testimonies')

	def tearDown(self):
		self.testimony.delete()

	def test_testimony_creation(self):
		self.assertEqual(self.testimony.first_name, 'John')
		self.assertEqual(self.testimony.last_name, 'Doe')
		self.assertEqual(self.testimony.designation, 'Deacon')
		self.assertEqual(self.testimony.testimony, 'God did it.')
		self.assertIsNotNone(self.testimony.date_received)

	def test_testimony_str_method(self):
		expected_str = f'{self.testimony.designation} {self.testimony.first_name} {self.testimony.last_name}'
		self.assertEqual(str(self.testimony), expected_str)

	def test_encrypted_fields(self):
		testimony_from_db = Testimony.objects.get(id=self.testimony.id)

		self.assertEqual(testimony_from_db.first_name, 'John')
		self.assertEqual(testimony_from_db.last_name, 'Doe')
		self.assertEqual(testimony_from_db.designation, 'Deacon')
		self.assertEqual(testimony_from_db.testimony, 'God did it.')

	def test_unique_id(self):
		new_testimony = Testimony.objects.create(
			first_name='Jane',
			last_name='Smith',
			designation='Deaconess',
			testimony='God is awesome.',
			date_received=timezone.now(),
		)
		self.assertNotEqual(self.testimony.id, new_testimony.id)

	def test_uuidv4_id(self):
		self.assertEqual(self.testimony.id, self.expected_id)

	def test_id_field(self):
		self.assertEqual(len(self.testimony.id), 16)

		# check for alphanumeric since UUIDv4 produces hexadecimal digits)
		self.assertTrue(self.testimony.id.isalnum())

		# check new UUID
		new_full_uuid = str(uuid.uuid4()).replace('-', '')
		new_expected_id = new_full_uuid[:16]
		self.assertNotEqual(self.testimony.id, new_expected_id)

	def test_testimony_details(self):
		response = self.client.get(self.testimony_url)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Testimony')
		self.assertTemplateUsed(response, 'testimonies/testimonies.html')
