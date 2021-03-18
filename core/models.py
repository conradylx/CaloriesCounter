from django.db import models

meals = (
        ('Breakfast', 'BreakFast'),
        ('2nd Breakfast', '2nd BreakFast'),
        ('Lunch', 'Lunch'),
        ('Snack', 'Snack'),
        ('Supper', 'Supper'),
    )


class Item(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(choices=meals, max_length=13)
    proteins = models.DecimalField(max_digits=5, decimal_places=1, default=0)
    calories = models.IntegerField(default=0)
    fats = models.DecimalField(max_digits=5, decimal_places=1, default=0)
    carbohydrates = models.DecimalField(max_digits=5, decimal_places=1, default=0)

    def __str__(self):
        return self.name

    def calculate_kcal(self):
        proteins_kcal = self.proteins * 4
        carbo_kcal = self.carbohydrates * 4
        fats_kcal = self.fats * 9
        return proteins_kcal + carbo_kcal + fats_kcal

    calories_calculated = property(calculate_kcal)
