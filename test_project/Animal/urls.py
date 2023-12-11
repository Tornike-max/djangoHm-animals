from django.urls import path
from . import views

urlpatterns = [
    path('', views.AnimalsView.as_view(), name='selectAnimals'),
    path('add', views.AddAnimalView.as_view(), name='addAnimals'),
    path('delete', views.DeleteAnimalView.as_view(), name='deleteAnimals'),
]
