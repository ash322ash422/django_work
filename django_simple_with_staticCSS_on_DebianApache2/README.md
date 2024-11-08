# django_simple_with_staticCSS_on_DebianApache2
 
NOTE: I used virtual env. with python interpreter=python3.11 on VSCode IDE.

Steps on how to create this simple app:
1) Open  the terminal and at the prompt, type "python -m pip install -r .\requirements.txt".
 To freeze -> ..\django_simple_with_staticCSS_on_DebianApache2> python -m pip freeze > requirements.txt

2) At the prompt, type "django-admin startproject mysite". (This creates a django project called 'mysite'.) At the prompt, type "cd mysite". This would take you inside 'mysite' directory.

3) At the prompt, type "python manage.py migrate". This would create some predefined admin apps that are very helpful.

4) At the prompt(in dir mysite), type "django-admin startapp notes".

..\django_simple_with_staticCSS_on_DebianApache2\mysite> django-admin startapp notes

 Make appropriate changes to notes/{urls.py,views.py,/templates/notes/{index.html..}, /static/notes/{css/,img/,js/} }. 

5) At the prompt(in dir mysite), type "django-admin startapp blog".
    Make appropriate changes to blog/{urls.py, views.py, templates/blog/index.html}, etc...

6)  Go to mysite/settings.py and make appropriate changes (i.e. create ../settings/{base.py,production.py,development.py})

7)  Go to mysite/urls.py and make appropriate changes

8) Change manage.py to reflect both development and production environment.

9)  At the prompt, type "python manage.py runserver 0.0.0.0:8010" or "python manage.py runserver localhost:8000". This would start development server on local machine at port 8010. YOU MAY HAVE TO CHANGE manage.py TO SWITCH BETWEEN DEVELOP./PROD. ALSO HAVE TO
  CHANGE wsgi.py file.
 
10) Go to web browser and type '127.0.0.1:8010'. You will see 'notes' welcome page. Congratulations!!!!!

##########################################

Now we take care of the problem where static CSS, js, img, etc are not being displayed because DEBUG=False during production:

11) Now goto settings\{base.py,} and set "STATIC_ROOT = BASE_DIR / 'static_root'" and then goto mysite\urls.py and add

if not settings.DEBUG:
  urlpatterns = urlpatterns + [
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
  ]


12) run 'python manage.py collectstatic':

..\django_simple_with_staticCSS_on_DebianApache2\mysite> python manage.py collectstatic

13) Now run 'python manage.py runserver 0.0.0.0:8010'  without the --insecure option.
################################################

END: 'python -m pip freeze > requirements.txt'

############################################################

#############################################################

#####################################################
Now we set up apache2 on debian on EC2:

1) admin@ip-172-31-32-82:~$ sudo apt install git
   
2) admin@ip-172-31-32-82:~$ git clone https://github.com/ash322ash422/django_simple_with_staticCSS_on_DebianApache2
  
 and then rename dir. "django_simple_with_staticCSS_on_DebianApache2" to "django_simple_proj"

2.1) Now we setup virtual envir:

a) admin@ip-172-31-32-82:~$ /usr/bin/python3 -m venv .venv/django_simple_proj

b) admin@ip-172-31-32-82:~$ source .venv/django_simple_proj/bin/activate

c) (django_simple_proj) admin@ip-172-31-32-82:~/django_simple_proj$ ~/.venv/django_simple_proj/bin/pip install -r requirements.txt

d) Now goto aws.amazon.com and click on the EC2 instance -> 'security' tab -> click on 'launch-wizard-1' link -> Edit Inbound Rules -> add inbound rule: Type='Custom TCP' with port='8010' 
   and source='0.0.0.0/0'. 
   
   Also make sure that under settings.py, ALLOWED_HOST=['your_ip_address'] or ['*']

e) Now run : 'python manage.py runserver 0.0.0.0:8010'

(django_simple_proj) admin@ip-172-31-32-82:~/django_simple_proj/mysite$ python3 manage.py runserver 0.0.0.0:8010

Now if u goto URL 'ip_address:8010', you should see your website.
 Congratulations upto here....

##################
Now comes the tricky part:

3) Make changes to ports.conf:
(django_simple_proj) admin@ip-172-31-32-82:~$ cat /etc/apache2/ports.conf
# If you just change the port or add more ports here, you will likely also
# have to change the VirtualHost statement in
# /etc/apache2/sites-enabled/000-default.conf

#Following was disabled b/c I am running radhesh web site on port 80
#Listen 80
Listen 89

Listen 8000

#Following is for django_simple_proj
Listen 8010

<IfModule ssl_module>
        Listen 443
</IfModule>

<IfModule mod_gnutls.c>
        Listen 443
</IfModule>
(django_simple_proj) admin@ip-172-31-32-82:~$


The original file:
4) Create a new file:
 (django_simple_proj) admin@ip-172-31-32-82:~$ cat /etc/apache2/sites-available/django_simple_proj.conf                                                   <VirtualHost *:8010>

        #ServerAdmin webmaster@localhost
        #DocumentRoot /var/www/html


        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined

        Alias /static /home/admin/django_simple_proj/mysite/mysite/static_root
        <Directory /home/admin/django_simple_proj/mysite/mysite/static_root>
                Require all granted
        </Directory>


        <Directory  /home/admin/django_simple_proj/mysite/mysite>
        <Files wsgi.py>
                Require all granted
        </Files>
        </Directory>

        WSGIDaemonProcess mysite python-home=/home/admin/.venv/django_simple_proj python-path=/home/admin/django_simple_proj/mysite
        WSGIProcessGroup mysite
        WSGIScriptAlias / /home/admin/django_simple_proj/mysite/mysite/wsgi.py


</VirtualHost>
(django_simple_proj) admin@ip-172-31-32-82:~$

5.1) Enable the site by creating a link:
(django_simple_proj) admin@ip-172-31-32-82:/etc/apache2/sites-enabled$ sudo ln -s ../sites-available//django_simple_proj.conf
(django_simple_proj) admin@ip-172-31-32-82:/etc/apache2/sites-enabled$ ll
total 0
lrwxrwxrwx 1 root root 35 Apr 26 14:28 000-default.conf -> ../sites-available/000-default.conf
lrwxrwxrwx 1 root root 43 Apr 30 11:45 django_simple_proj.conf -> ../sites-available//django_simple_proj.conf
(django_simple_proj) admin@ip-172-31-32-82:/etc/apache2/sites-enabled$

(NOTE: To unlink use 'sudo unlink file_name.conf')

5.2) admin@ip-172-31-32-82:~$ sudo apache2ctl configtest



6) admin@ip-172-31-32-82:~$ chmod a+x -R django_simple_proj/
   admin@ip-172-31-32-82:~$ chmod a+w -R django_simple_proj/

7) Check apache2 configurations:
 admin@ip-172-31-32-82:~$ sudo apache2ctl configtest
     
     admin@ip-172-31-32-82:~$ sudo systemctl restart apache2

     admin@ip-172-31-32-82:~$ sudo systemctl status apache2


9) Now goto URL "http://ip_adress:8010/" or "ip_adress:8010". Congratulations.