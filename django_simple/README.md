# django_simple
 PREREQUISITES:

A) To get "python" command working on windows so you  do not have to type the whole python path :
   start -> type "Edit environmental variables..." -> select "Advanced" tab and and
   then click "environmental variables" -> In the "system variables" box "edit" the "PATH" variable -> 
   add 2 "new" PATH= C:\Users\hi\AppData\Local\Programs\Python\Python39\
   and "C:\Users\hi\AppData\Local\Programs\Python\Python39\Scripts\" -> restart.
   
   B) Install 'git' by going to https://git-scm.com/downloads. Choose between Windows/Linux/Mac OS.
   This would get "git" app and you  would be  able to run git from command line.
*****************************************************************************************

1) Make dir 'tutorial' and cd into it:

C:\Users\hi\Desktop>mkdir tutorial

C:\Users\hi\Desktop>cd tutorial

C:\Users\hi\Desktop\tutorial>

2) Make sure you have virtualenv package installed. You can check this by running command 'virtualenv' on terminal.
   
   If you don't have virtualenv package installed then install it by using command "pip install virtualenv"

3) Create a virtual env and activate it. I am using python3.12
   
   C:\Users\hi\Desktop\tutorial> C:\Users\hi\AppData\Local\Programs\Python\Python312\python.exe -m venv .env_django

   C:\Users\hi\Desktop\tutorial> .env_django\Scripts\activate

(.env_django) C:\Users\hi\Desktop\tutorial>

1) Clone 'django_simple' from github to the directory on your local machine.

(.env_django) C:\Users\hi\Desktop\tutorial> git clone https://www.github.com/ash322ash422/django_simple


4) Install django version 4.2.11:
   
   (.env_django) C:\Users\hi\Desktop\tutorial>pip install "Django==4.2.11"

5) Change directory to django_simple\mysite:
   
   (.env_django) C:\Users\hi\Desktop\tutorial>cd django_simple\mysite


6) Start the django server on local machine port number 8000.:
   
  (.env_django) C:\Users\hi\Desktop\tutorial\django_simple\mysite> python manage.py runserver 
  
  OR use following command:

  (.env_django) C:\Users\hi\Desktop\tutorial\django_simple\mysite> python manage.py runserver 0.0.0.0:8000.
  
  
7)  Go to web browser and type '127.0.0.1:8000/notes'. You will see 'notes' welcome page. Congratulations!!!!!
   
8) Go to web browser and type '127.0.0.1:8000/blog'.  You will see 'blog' welcome page.  Congratulations!!!!!

***************************************************************************

