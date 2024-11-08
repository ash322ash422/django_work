Steps on how to create this simple app:
1) Create a 'django_simple' on your local machine. 
2) Open visual-studio-code and open the above folder.
3) Open  the terminal and at the prompt, type "pip install "Django==4.2.11". This would install django version 4.2.11
4) At the prompt, type "cd django_simple" 
5) At the prompt, type "pip install virtualenv". 
6) At the prompt, type "virtualenv env"
7) At the prompt, type "pip install "Django==4.2.11". This would install django version 4.2.11
8) At the prompt, type " django-admin startproject mysite". This creates a django project called 'mysite'. 90) At the prompt, type "cd mysite". This would take you inside 'mysite' directory.
9) At the prompt, type "python manage.py migrate". This would create some predefined admin apps that are very helpful.
10) At the prompt(in dir mysite), type "django-admin startapp notes". Make appropriate changes to notes/{urls.py,views.py} 
11) At the prompt(in dir mysite), type "django-admin startapp blog". Make appropriate changes to blog/{urls.py, views.py}
12) Go to mysite/settings.py and make appropriate changes
13) Go to mysite/urls.py and make appropriate changes
14) At the prompt, type "python manage.py runserver 0.0.0.0:8000". This would start development server on local machine port number 8000.
15) Go to web browser and type '127.0.0.1:8000/notes'. You will see ''notes' welcome page. Congratulations!!!!!
