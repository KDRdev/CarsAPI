import json
from django.db import models
from django.db.models import Avg, Count
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Car, Rating

def index(request):
    return HttpResponse(
        "Welcome to the Cars API.\
        For viewing cars, go to /cars.\
        To add a rating, use /rate endpoint and pass it 'car_id' and 'rating' values.\
        For viewing popular cars, go to /popular.")

@csrf_exempt
def cars(request):
    if request.method == 'GET':
        cars = Car.objects.annotate(avg_rate=Avg('rating__rating'))
        data = {
            "Cars": list(cars.values("id", "make", "model", "avg_rate"))
        }
        return JsonResponse(data)
    elif request.method == 'POST':
        r_data = json.loads(request.body)
        make = r_data['make']
        model = r_data['model']
        if Car.car_exists(make, model):
            car = Car(make=make, model=model)
            car.save()
            return HttpResponse('Car sucessfully added!')
        else:
            return HttpResponse('Oops. It looks like this model does not exist.', status=400)

def popular(request):
    if request.method == 'GET':
        cars = Car.objects.annotate(rate_count=Count('rating__rating')).order_by('-rate_count')
        data = {
            "The Most Popular Cars": list(cars.values("id", "make", "model", "rate_count"))
        }
        return JsonResponse(data)

@csrf_exempt
def rate(request):
    if request.method == 'GET':
        return HttpResponse('Oops. It looks like you used GET request.\
            You need to pass "car_id" and "rating" in a POST request here.')
    if request.method == 'POST':
        r_data = json.loads(request.body)
        car_id = r_data['car_id']
        data = {
            "rate": r_data['rating'],
            "car_id": Car.objects.get(id=car_id),
        }
        rating = Rating(rating=data['rate'], car_id=data['car_id'])
        rating.save()
        return HttpResponse('Sucessfully rated the car!')