import requests
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Car

@csrf_exempt
def cars_list(request):
    if request.method == 'GET':
        cars = Car.objects.all()
        data = {"results": list(cars.values("make", "model"))}
        return JsonResponse(data)
    elif request.method == 'POST':
        make = request.POST.get('make')
        model = request.POST.get('model')
        if car_exists(make, model):
            car = Car(make=make, model=model)
            car.save()
            return HttpResponse('Car sucessfully added!')
        else:
            return HttpResponse('Oops. It looks like this model does not exist.', status=400)

@csrf_exempt
def cars_single(request, id):
    if request.method == 'GET':
        car = get_object_or_404(Car, id=id)
        data = {
            "result": {
                "make": car.make,
                "model": car.model
            }
        }
        return JsonResponse(data)

@csrf_exempt
def cars_rate(request, id):
    car = get_object_or_404(Car, id=id)
    if request.method == 'POST':
        rating = request.POST.get('rating')
        car.rating = rating
        car.rating_count += 1
        car.save()
        return HttpResponse('Sucessfully rated the car!')

def car_exists(make, model):
    makes_with_models = 0
    make_r = requests.get(f'https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMake/{make}?format=json')
    make_dict = make_r.json()
    for make_id in make_dict["Results"]:
        if make_id["Make_Name"] == make and make_id["Model_Name"] == model:
            makes_with_models += 1
    if makes_with_models > 0:
        return True
