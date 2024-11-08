# django_rest_framework_tutorial1
 Basic tutorial

1) if django not install then use -> pip install django

2) Install django rest framework:
 PS C:\Users\hi\Desktop\projects\python_projects\django_rest_framework_tutorial1> pip install djangorestframework

3) Run following cmds:

PS C:\Users\hi\Desktop\projects\python_projects\django_rest_framework_tutorial1> django-admin startproject fruits 

PS C:\Users\hi\Desktop\projects\python_projects\django_rest_framework_tutorial1> cd .\fruits\

PS C:\Users\hi\Desktop\projects\python_projects\django_rest_framework_tutorial1\fruits> python.exe .\manage.py runserver

4) go to url :  http://127.0.0.1:8000/ and you will see django start page.
   
8)Run migration:

 PS C:\Users\hi\Desktop\projects\python_projects\django_rest_framework_tutorial1\fruits> python.exe .\manage.py migrate

 5) Create superuser:

PS C:\Users\hi\Desktop\projects\python_projects\django_rest_framework_tutorial1\fruits> python.exe .\manage.py createsuperuser
(passowrd=admin)...a lame password

Now go to url: 'http://127.0.0.1:8000/admin' and user=admin and password=admin 

6) Create models.py in the necessary path, then in settings.py append to INSTALLED_APPS 'fruits'.Then execute,

PS C:\Users\hi\Desktop\projects\python_projects\django_rest_framework_tutorial1\fruits> python .\manage.py makemigrations fruits

PS C:\Users\hi\Desktop\projects\python_projects\django_rest_framework_tutorial1\fruits> python .\manage.py migrate   

7) Add admin.py and restart the server, go to admin  page and you  should see this new model. Add serializer.py,views.py file and at
 url http://127.0.0.1:8000/fruits/ or http://127.0.0.1:8000/fruits.json. You should see the json  response.

8) Now we can test if console app can read this JSON data. Install requests( 'pip install requests') and then run read_json_data_from_web.py  