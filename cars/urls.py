from django.urls import path
from . import views

urlpatterns = [
    path('cars', views.cars_list, name="Cars List"),
    path('cars/<int:id>', views.cars_single, name="Single Car"),
    path('cars/<int:id>/rate', views.cars_rate, name="Single Car"),
    path
]