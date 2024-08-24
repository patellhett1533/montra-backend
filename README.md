# Backend API using Django and Postgresql

This is a backend project for montra flutter app
which is made by django, postgresql, docker

for local setup, you need postgresql in your device and create a .env file

```javascript
SQL_NAME = your_database_name;
SQL_USER = your_username;
SQL_PASSWORD = your_password;
HOST = localhost;
PORT = 5432;
```

then

```javascript
python manage.py makemigrations
```

if above command run successfully then run

```javascript
python manage.py migrate
```

if successfully run above command then you will able to run project

```javascript
python manage.py runserver
```
