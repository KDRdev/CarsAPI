from django.test import Client, TestCase
from .models import Car


class CarsApiTest(TestCase):

    client = Client()
    
    def test_cars(self):
        cars_response = self.client.get('/cars')
        self.assertEqual(cars_response.status_code, 200)

    def test_post_cars_existing(self):
        cars_post_response = self.client.post('/cars', 
            content_type='application/json', data={"make": "BMW", "model": "X4"})
        self.assertEqual(cars_post_response.status_code, 200)

    def test_post_cars_nonexisting(self):
        cars_post_response = self.client.post('/cars', 
            content_type='application/json', data={"make": "Unknown", "model": "Whatever"})
        self.assertEqual(cars_post_response.status_code, 400)

    def test_post_rate(self):
        car = Car(id=1, make="BMW", model="Z3")
        car.save()
        rate_post_response = self.client.post('/rate',
            content_type='application/json', data={"car_id": "1", "rating": "5"})
        self.assertEqual(rate_post_response.status_code, 200)

    def test_popular(self):
        popular_response = self.client.get('/popular')
        self.assertEqual(popular_response.status_code, 200)
