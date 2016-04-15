from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpResponse
from lists.views import home_page


class HomePageTest(TestCase):
	"""docstring for SmokeTest"""
	def test_root_url_resolves_to_home_page_view(self):
		found=resolve('/')
		self.assertEqual(found.func,home_page)


	def test_home_page_returns_correct_html(self):
		request=HttpResponse()
		response=home_page(request)
		self.assertTrue(response.content.startswith(b'<html>'))
		self.assertIn(b'<title>To-D lists</title>',response.content)
		self.assertTrue(response.content.endswith(b'</html>'))




