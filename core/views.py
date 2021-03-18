from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import render

from core.forms import AddItemForm
from core.models import Item


def index(request):
    first_meal = Item.objects.all().filter(category__in=('Breakfast', 'BreakFast'),)
    second_meal = Item.objects.all().filter(category__in=('2nd Breakfast', '2nd BreakFast'))
    first_meal_kcal = Item.objects\
        .filter(category__in=('Breakfast', 'BreakFast'),)\
        .aggregate(c=Sum('calories'), p=Sum('proteins'), f=Sum('fats'), carb=Sum('carbohydrates'))
    scnd_meal_kcal = Item.objects.filter(category__in=('2nd Breakfast', '2nd BreakFast')) \
        .aggregate(c=Sum('calories'), p=Sum('proteins'), f=Sum('fats'), carb=Sum('carbohydrates'))
    total_kcal_consumed = Item.objects.all().aggregate(Sum('calories'))

    context = {
        'breakfast': first_meal,
        '2nd_breakfast': second_meal,
        'total_kcal': total_kcal_consumed['calories__sum'],
        'breakfast_kcal': first_meal_kcal,
        '2nd_breakfast_kcal': scnd_meal_kcal,
        # 'form': form,
    }
    return render(request, 'core/index.html', context)
