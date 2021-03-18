from django.test import SimpleTestCase
from django.urls import reverse, resolve


class TestUrls(SimpleTestCase):

    def test_index_url(self):
        path = reverse('index')
        assert resolve(path).view_name == 'index'
