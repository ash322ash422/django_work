# django_tutorial_JWToken2
 
I am using python3.12

0) pip install django djangorestframework djangorestframework_simplejwt

1) Run migrate command, create superuser admin(p/w=admin), runserver and finally run test:

..\JWT2> python manage.py migrate

..\JWT2> python manage.py createsuperuser

..\JWT> python .\manage.py runserver 

..\JWT\mainapp> python .\test_mainapp.py

2) Goto URL and type 'http://127.0.0.1:8000/api/token/' . This would prompt you for username and password. Enter u/n=admin and p/w=admin, that we created above. (NOTE: It would NOT accept username who is not in database). This would give access and refresh token.