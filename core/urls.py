from django.urls import path

from core import views

urlpatterns = [
    path('', views.index, name="index"),
    path('new-item/', views.add_item_to_list, name='add_item'),
]