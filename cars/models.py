import requests
from django.db import models
from django.db.models import Avg


class Car(models.Model):
    make = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    car = models.CharField(max_length=128, blank=True) 
    
    def save(self, *args, **kwargs):
        self.car = self.make + ' ' + self.model
        super(Car, self).save(*args, **kwargs)

    def __str__(self):
        return self.car

    def car_exists(make, model):
        makes_with_models = 0
        make_r = requests.get(f'https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMake/{make}?format=json')
        make_dict = make_r.json()
        for make_id in make_dict["Results"]:
            if make_id["Make_Name"] == make and make_id["Model_Name"] == model:
                makes_with_models += 1
        if makes_with_models > 0:
            return True


class Rating(models.Model):
    rating = models.IntegerField(choices=[
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ], default=0)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)