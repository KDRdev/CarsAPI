# Cars API
A simple cars API with functionality for adding cars, rating them and reviewing their popularity

 - Built using Django 3.1
 - Works with PostgreSQL
 
 Setting up an application:
 
 1. After cloning the repository, install dependencies using pip install -r requirements.txt.
 2. Configure your DB connection in cars_api/settings.py.
 3. Run 'python manage.py migrate' command to create DB tables.
 4. Your app can now be started using 'python manage.py runserver' command.
 5. Access the app by going to http://127.0.0.1:8000 or http://localhost:8000

For setting up Docker container, from the app root foler, run 'docker-compose up' command
