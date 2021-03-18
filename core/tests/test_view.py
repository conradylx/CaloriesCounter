from django.test import SimpleTestCase, TestCase
from django.urls import reverse

from core.models import Item


class TestViews(TestCase):
    databases = '__all__'

    def test_index_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        
    # def test_first_meal_returned(self):
    #     response = Item.objects.all().filter(category_id=1)
    #     self.assertQuerysetEqual(response, '<Item: Donut>, <Item: Soup>', ordered=False)
