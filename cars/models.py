from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    car = models.CharField(max_length=128, blank=True)
    rating = models.IntegerField(choices=[
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ], blank=True)
    rating_count = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.car = self.make + ' ' + self.model
        super(Car, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.car
