from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import render, redirect

from core.forms import AddItemForm
from core.models import Item


def index(request):
    first_meal = Item.objects.all().filter(category__in=('Breakfast', 'BreakFast'),)
    second_meal = Item.objects.all().filter(category__in=('2nd Breakfast', '2nd BreakFast'))
    lunch = Item.objects.all().filter(category__in=('Lunch', 'Lunch'))
    snack = Item.objects.all().filter(category__in=('Snack', 'Snack'))
    supper = Item.objects.all().filter(category__in=('Supper', 'Supper'))
    first_meal_kcal = Item.objects\
        .filter(category__in=('Breakfast', 'BreakFast'),)\
        .aggregate(c=Sum('calories'), p=Sum('proteins'), f=Sum('fats'), carb=Sum('carbohydrates'))
    scnd_meal_kcal = Item.objects.filter(category__in=('2nd Breakfast', '2nd BreakFast')) \
        .aggregate(c=Sum('calories'), p=Sum('proteins'), f=Sum('fats'), carb=Sum('carbohydrates'))
    lunch_kcal = Item.objects.filter(category__in=('Lunch', 'Lunch')) \
        .aggregate(c=Sum('calories'), p=Sum('proteins'), f=Sum('fats'), carb=Sum('carbohydrates'))
    snack_kcal = Item.objects.filter(category__in=('Snack', 'Snack')) \
        .aggregate(c=Sum('calories'), p=Sum('proteins'), f=Sum('fats'), carb=Sum('carbohydrates'))
    supper_kcal = Item.objects.filter(category__in=('Supper', 'Supper')) \
        .aggregate(c=Sum('calories'), p=Sum('proteins'), f=Sum('fats'), carb=Sum('carbohydrates'))
    total_kcal_consumed = Item.objects.all().aggregate(Sum('calories'))

    context = {
        'breakfast': first_meal,
        '2nd_breakfast': second_meal,
        'lunch': lunch,
        'snack': snack,
        'supper': supper,
        'total_kcal': total_kcal_consumed['calories__sum'],
        'breakfast_kcal': first_meal_kcal,
        '2nd_breakfast_kcal': scnd_meal_kcal,
        'lunch_kcal': lunch_kcal,
        'snack_kcal': snack_kcal,
        'supper_kcal': supper_kcal,
    }
    return render(request, 'core/index.html', context)


def add_item_to_list(request):
    form = AddItemForm()
    if request.method == 'POST':
        form = AddItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'core/new_item.html', context)
