import uuid

from django.core.files.storage import default_storage
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.utils import timezone
from model_bakery import baker

from core.resources.models import Media


class MediaModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Random UUIDv4
        full_uuid = str(uuid.uuid4()).replace('-', '')
        cls.expected_id = full_uuid[:16]

        cls.media_file = SimpleUploadedFile('church_sermon.mp3', b'file_content', content_type='audio/mp3')
        cls.media = baker.make(
            Media,
            id=cls.expected_id,
            slug='sermon_1',
            file_title='Sermon 1',
            service='Sunday Service',
            message_date=timezone.now(),
            resource_file=cls.media_file,
        )

    def tearDown(self):
        if self.media.resource_file:
            if default_storage.exists(self.media.resource_file.name):
                default_storage.delete(self.media.resource_file.name)

        # Clean up the model instance
        self.media.delete()

    def test_media_creation(self):
        self.assertNotEqual(self.media.file_title, 'Sunday Sermon')
        self.assertEqual(self.media.service, 'Sunday Service')
        self.assertTrue(self.media.publish)
        self.assertIsNotNone(self.media.date_created)
        self.assertIsNotNone(self.media.last_updated)

    def test_media_str_method(self):
        self.assertEqual(str(self.media), 'Sermon 1')
