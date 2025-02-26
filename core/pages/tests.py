# tests.py
from django.test import TestCase
from django.urls import reverse


class TestViews(TestCase):
	def test_home_url(self):
		response = self.client.get(reverse('home'))
		self.assertTemplateUsed(response, 'pages/index.html')
		self.assertContains(response, 'CBD')
		self.assertEqual(response.status_code, 200)

	def test_about_url(self):
		response = self.client.get(reverse('about'))
		self.assertTemplateUsed(response, 'pages/about.html')
		self.assertContains(response, 'Winners Chapel International, Johannesburg CBD')
		self.assertEqual(response.status_code, 200)

	def test_ministries_url(self):
		response = self.client.get(reverse('ministries'))
		self.assertTemplateUsed(response, 'ministries/ministries.html')
		self.assertContains(response, 'OUR MINISTRIES')
		self.assertEqual(response.status_code, 200)

	def test_sunday_ministry_url(self):
		response = self.client.get(reverse('sunday_ministry'))
		self.assertTemplateUsed(response, 'ministries/sunday_ministry.html')
		self.assertContains(response, 'Sunday')
		self.assertEqual(response.status_code, 200)

	def test_wenesday_ministry_url(self):
		response = self.client.get(reverse('wenesday_ministry'))
		self.assertTemplateUsed(response, 'ministries/wenesday_ministry.html')
		self.assertContains(response, 'Wenesday')
		self.assertEqual(response.status_code, 200)

	def test_wose_ministry_url(self):
		response = self.client.get(reverse('wose_ministry'))
		self.assertTemplateUsed(response, 'ministries/wose_ministry.html')
		self.assertContains(response, 'Spiritual')
		self.assertEqual(response.status_code, 200)

	def test_chop_ministry_url(self):
		response = self.client.get(reverse('chop_ministry'))
		self.assertTemplateUsed(response, 'ministries/chop_ministry.html')
		self.assertContains(response, 'Covenant Hour of Prayer')
		self.assertEqual(response.status_code, 200)

	def test_wofbi_ministry_url(self):
		response = self.client.get(reverse('wofbi_ministry'))
		self.assertTemplateUsed(response, 'ministries/wofbi_ministry.html')
		self.assertContains(response, 'WOFBI')
		self.assertEqual(response.status_code, 200)

	def test_yaf_ministry_url(self):
		response = self.client.get(reverse('yaf_ministry'))
		self.assertTemplateUsed(response, 'ministries/yaf_ministry.html')
		self.assertContains(response, 'YAF')
		self.assertEqual(response.status_code, 200)

	def test_children_ministry_url(self):
		response = self.client.get(reverse('children_ministry'))
		self.assertTemplateUsed(response, 'ministries/children_ministry.html')
		self.assertContains(response, 'Children')
		self.assertEqual(response.status_code, 200)

	def test_evangelism_ministry_url(self):
		response = self.client.get(reverse('evangelism_ministry'))
		self.assertTemplateUsed(response, 'ministries/evangelism_ministry.html')
		self.assertContains(response, 'Evangelism')
		self.assertEqual(response.status_code, 200)

	def test_sanctuary_ministry_url(self):
		response = self.client.get(reverse('sanctuary_ministry'))
		self.assertTemplateUsed(response, 'ministries/sanctuary_ministry.html')
		self.assertContains(response, 'Sanctuary')
		self.assertEqual(response.status_code, 200)

	def test_followup_ministry_url(self):
		response = self.client.get(reverse('followup_ministry'))
		self.assertTemplateUsed(response, 'ministries/followup_ministry.html')
		self.assertContains(response, 'Followup')
		self.assertEqual(response.status_code, 200)

	def test_hospitality_ministry_url(self):
		response = self.client.get(reverse('hospitality_ministry'))
		self.assertTemplateUsed(response, 'ministries/hospitality_ministry.html')
		self.assertContains(response, 'Hospitality')
		self.assertEqual(response.status_code, 200)
