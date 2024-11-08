1) Create virtual env: view -> command palette -> Python: select Interpretor -> create virtual env and select 'Venv' -> I am using python3.11.2
(Make sure you have pip 'sudo apt install python3-pip' on debian)
2) 'python -m pip install django==5.0.4', 'python -m pip install python-decouple==3.8' ( and also run 'python -m pip freeze > requirements.txt' )
3) ...\python_projects\django_pawan> django-admin.exe startproject radheshgypsum   
     Create  \python_projects\django_pawan\radheshgypsum\settings\{base.py, production.py,development.py}. Then add necessary code in here and also make changes to manage.py
4) ...\python_projects\django_pawan\radheshgypsum> python manage.py startapp appmain 
   ...\python_projects\django_pawan\radheshgypsum> python manage.py runserver (and goto url http://127.0.0.1:8000/ )


5) ...\python_projects\django_pawan\radheshgypsum> python manage.py makemigrations
6) ...\python_projects\django_pawan\radheshgypsum> python manage.py createsuperuser

user = admin and p/w=admin


7) Make appropriate changes to appmain/{urls.py,views.py}

8) Go to radheshgypsum/{settings.py,urls.py} and make appropriate changes

9) At the end :
...\django_pawan\radheshgypsum> python manage.py collectstatic
*************************
ISSUE:
1) File "C:\Users\hi\Desktop\projects\python_projects\django_pawan\radheshgypsum\radheshgypsum\settings\development.py", line 1, in <module>
    from base import *
ModuleNotFoundError: No module named 'base'

SOLUTION: use 'from .base import *'
*******************************


##########################################################################
cofigure apache2:
1) add line 
#Following is for radheshgypsum.com
Listen 8000

to the file /etc/apache2/ports.conf
###########################
To see version of debian : lsb_release -a

#############################################################
Now we install packages on debian for python3.11:

1) admin@ip-172-31-32-82:~$  sudo apt install python3.11-venv
2) admin@ip-172-31-32-82:~$ /usr/bin/python3 -m venv .venv/django_pawan  -> this creates .venv/django_pawan dir in ~
3) admin@ip-172-31-32-82:~$ .venv/django_pawan/bin/pip install Django==5.0.4
4) admin@ip-172-31-32-82:~$ .venv/django_pawan/bin/pip install python-decouple==3.8
5) admin@ip-172-31-32-82:~$ .venv/django_pawan/bin/pip install tzdata==2024.1

 Now we activate virtual env:
1) admin@ip-172-31-32-82:~$ source .venv/django_pawan/bin/activate
(django_pawan) admin@ip-172-31-32-82:~$

2) Change manage.py code to reflect production.py settings during production.

3) Run server:
 (django_pawan) admin@ip-172-31-32-82:~/django_pawan/radheshgypsum$ python3 manage.py runserver 0.0.0.0:8000

4) Now goto aws.amazon.com and click on the EC2 instance -> 'security' tab -> click on 'launch-wizard-1' link -> Edit Inbound Rules -> add inbound rule:      Type='Custom TCP' with port='8010' 
   and source='0.0.0.0/0'. 
    Also make sure that under settings.py,  ALLOWED_HOST=['your_ip_address'] or ['*']

   Now if u goto URL 'ip_address:8000', you should see your website.

##############################
PROBLEM: I need to access radheshgypsum.com which is bound to port 80 and not 8000.
Solution:
Now to host the website on port 80 do following:
1) Make sure that ports.conf is:
admin@ip-172-31-32-82:~$ cat /etc/apache2/ports.conf
# If you just change the port or add more ports here, you will likely also
# have to change the VirtualHost statement in
# /etc/apache2/sites-enabled/000-default.conf

#Following was disabled b/c I am running radhesh web site on port 80
#Listen 80

#This needs to be created
Listen 89

#Following is for radheshgypsum.com
#Listen 8000

<IfModule ssl_module>
        Listen 443
</IfModule>

<IfModule mod_gnutls.c>
        Listen 443
</IfModule>
admin@ip-172-31-32-82:~$

2) Change manage.py code to reflect production.py settings during production.
2.1) (django_pawan) admin@ip-172-31-32-82:~/django_pawan/radheshgypsum$ python3 manage.py collectstatic
3) Run server on port 80  and not 8000:
(django_pawan) admin@ip-172-31-32-82:~/django_pawan/radheshgypsum$ sudo nohup /home/admin/.venv/django_pawan/bin/python3  manage.py runserver 0.0.0.0:80 --insecure > /dev/null &

or 

admin@ip-172-31-32-82:~$ sudo nohup /home/admin/.venv/django_pawan/bin/python3  /home/admin/django_pawan/radheshgypsum/manage.py runserver 0.0.0.0:80 --insecure > /dev/null &

###################
To grep and kill a process: "ps -aux | grep nohup" and "sudo kill -9 30025"

