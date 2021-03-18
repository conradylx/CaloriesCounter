from django import forms
from .models import Item


class AddItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'category', 'proteins', 'fats', 'carbohydrates']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:150px'}),
            'category': forms.Select(attrs={'class': 'form-control', 'style': 'width:150px'}),
            'calories': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:100px'}),
            'proteins': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:100px'}),
            'fats': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:100px'}),
            'carbohydrates': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:100px'}),
        }
