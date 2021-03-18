from django.db.models import Sum
from django.shortcuts import render, redirect

from core.forms import AddItemForm
from core.models import Item


def index(request):
    """Lines below downloads meals items"""
    first_meal = Item.objects.all().filter(category__in=('Breakfast', 'BreakFast'),)
    second_meal = Item.objects.all().filter(category__in=('2nd Breakfast', '2nd BreakFast'))
    lunch = Item.objects.all().filter(category__in=('Lunch', 'Lunch'))
    snack = Item.objects.all().filter(category__in=('Snack', 'Snack'))
    supper = Item.objects.all().filter(category__in=('Supper', 'Supper'))
    """
    Lines below are resposible for simple calculations of proteins, fats and carbos. No kcalories are calculated yet."""
    first_meal_kcal = Item.objects\
        .filter(category__in=('Breakfast', 'BreakFast'),)\
        .aggregate(p=Sum('proteins'), f=Sum('fats'), carb=Sum('carbohydrates'))
    scnd_meal_kcal = Item.objects.filter(category__in=('2nd Breakfast', '2nd BreakFast')) \
        .aggregate(p=Sum('proteins'), f=Sum('fats'), carb=Sum('carbohydrates'))
    lunch_kcal = Item.objects.filter(category__in=('Lunch', 'Lunch')) \
        .aggregate(p=Sum('proteins'), f=Sum('fats'), carb=Sum('carbohydrates'))
    snack_kcal = Item.objects.filter(category__in=('Snack', 'Snack')) \
        .aggregate(p=Sum('proteins'), f=Sum('fats'), carb=Sum('carbohydrates'))
    supper_kcal = Item.objects.filter(category__in=('Supper', 'Supper')) \
        .aggregate(p=Sum('proteins'), f=Sum('fats'), carb=Sum('carbohydrates'))
    total_kcal_consumed = Item.objects.all().aggregate(Sum('calories'))
    """
    Lines below is used for model property usage. It counts proteins+fats+carbos as kcalories"""
    breakfast_total_kcal = 0
    for item in first_meal:
        breakfast_total_kcal = breakfast_total_kcal + item.calculate_kcal()
    sec_breakfast_total_kcal = 0
    for item in second_meal:
        sec_breakfast_total_kcal = sec_breakfast_total_kcal + item.calculate_kcal()
    lunch_total_kcal = 0
    for item in lunch:
        lunch_total_kcal = lunch_total_kcal + item.calculate_kcal()
    snack_total_kcal = 0
    for item in snack:
        snack_total_kcal = snack_total_kcal + item.calculate_kcal()
    supper_total_kcal = 0
    for item in supper:
        supper_total_kcal = supper_total_kcal + item.calculate_kcal()

    context = {
        'breakfast': first_meal,
        '2nd_breakfast': second_meal,
        'lunch': lunch,
        'snack': snack,
        'supper': supper,
        'total_kcal': total_kcal_consumed['calories__sum'],
        'breakfast_total_kcal': breakfast_total_kcal,
        'Sec_breakfast_total_kcal': sec_breakfast_total_kcal,
        'lunch_total_kcal': lunch_total_kcal,
        'snack_total_kcal': snack_total_kcal,
        'supper_total_kcal': supper_total_kcal,
        'breakfast_kcal': first_meal_kcal,
        '2nd_breakfast_kcal': scnd_meal_kcal,
        'lunch_kcal': lunch_kcal,
        'snack_kcal': snack_kcal,
        'supper_kcal': supper_kcal,
    }
    return render(request, 'core/index.html', context)


def add_item_to_list(request):
    """Function is responsible for adding new items to table"""
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
