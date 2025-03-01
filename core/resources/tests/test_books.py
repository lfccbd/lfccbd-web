from io import BytesIO

from PIL import Image
from django.core.files.storage import default_storage
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from model_bakery import baker

from core.resources.models import Book


class BooksModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a mock image in memory using PIL
        image = Image.new('RGB', (100, 100), color='red')
        img_byte_arr = BytesIO()
        image.save(img_byte_arr, format='JPEG')
        img_byte_arr.seek(0)

        # Create a test image and Books instance
        cls.book_image = SimpleUploadedFile(
            'book_cover.jpg', img_byte_arr.read(), content_type='image/jpeg'
        )
        cls.book = baker.make(
            Book,
            file_title='Book 1',
            slug='book_1',
            author='John Doe',
            publish_year=2022,
            publisher='Book Publisher',
            foreward='This is a sample foreward.',
            isbn='123-456-789',
            featured_image=cls.book_image,
            image_1=cls.book_image,
            image_2=cls.book_image,
        )

        # Create a URL for resources
        cls.resource_url = reverse('resources')

    def tearDown(self):
        # Use default_storage to delete uploaded image files
        if self.book.featured_image:
            if default_storage.exists(self.book.featured_image.name):
                default_storage.delete(self.book.featured_image.name)

        if self.book.image_1:
            if default_storage.exists(self.book.image_1.name):
                default_storage.delete(self.book.image_1.name)

        if self.book.image_2:
            if default_storage.exists(self.book.image_2.name):
                default_storage.delete(self.book.image_2.name)

        # Clean up the model instance
        self.book.delete()

    def test_books_creation(self):
        self.assertEqual(self.book.file_title, 'Book 1')
        self.assertEqual(self.book.author, 'John Doe')
        self.assertEqual(self.book.publish_year, 2022)
        self.assertTrue(self.book.publish)
        self.assertIsNotNone(self.book.date_created)
        self.assertIsNotNone(self.book.last_updated)

    def test_books_str_method(self):
        self.assertEqual(str(self.book), 'Book 1')

    def test_resource_resolves(self):
        response = self.client.get(self.resource_url)
        self.assertEqual(response.status_code, 200)

    def test_resource_details(self):
        response = self.client.get(self.resource_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Book 1')
