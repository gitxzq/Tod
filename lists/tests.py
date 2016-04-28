from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpResponse
from django.http import HttpRequest
from lists.views import home_page
from django.template.loader import render_to_string


class HomePageTest(TestCase):
	"""docstring for SmokeTest"""
	def test_root_url_resolves_to_home_page_view(self):
		found=resolve('/')
		self.assertEqual(found.func,home_page)


	def test_home_page_returns_correct_html(self):
		request=HttpResponse()
		response=home_page(request)
		# self.assertTrue(response.content.startswith(b'<html>'))
		# self.assertIn(b'<title>To-D lists</title>',response.content)
		# self.assertTrue(response.content.strip().endswith(b'</html>'))
		expected_html=render_to_string('home.html')
		self.assertEqual(response.content.decode(),expected_html)

	def test_home_page_save_post_request(self):
		request=HttpRequest()
		request.method='POST'
		request.POST['item_text']='a new list item'

		response=home_page(request)
		self.assertIn('a new list item',response.content.decode())
		expected_html=render_to_string('home.html', {'new_item_text':' a new list item'})
		self.assertEqual(response.content.decode(),expected_html)


