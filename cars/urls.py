from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Index Page"),
    path('cars', views.cars, name="Cars List"),
    path('rate', views.rate, name="Rate A Car"),
    path('popular', views.popular, name="Popular Cars"),
]