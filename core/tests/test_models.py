from django.test import TestCase
from core.models import Item, Category
import pytest


@pytest.mark.django_db
class TestModels:

    def test_category_name(self):
        Category.objects.create(name='Breakfast')
        category_get = Category.objects.get(name='Breakfast')
        assert str(category_get) == 'Breakfast'

    def test_item_content(self):
        category = Category.objects.create(name='TestBreakfast')
        Item.objects.create(
            name="Donut",
            category=category,
            calories=132,
            proteins=12,
            fats=23,
            carbohydrates=56
        )
        item = Item.objects.get(pk=1)
        expected_obj_name = item.name
        expected_obj_category = item.category
        expected_obj_calories = item.calories
        expected_obj_proteins = item.proteins
        expected_obj_fats = item.fats
        expected_obj_carbohydrates = item.carbohydrates
        assert expected_obj_name == 'Donut'
        assert expected_obj_category.name == 'TestBreakfast'
        assert expected_obj_calories == 132
        assert expected_obj_proteins == 12
        assert expected_obj_fats == 23
        assert expected_obj_carbohydrates == 56
        assert str(item) == 'Donut'
