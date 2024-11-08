# django_ecomm
 
1) Create folder django_ecomm and then open it in VSCode. Choose interp=python3.12.2
2) create requirements.txt and add 'Django==5.0.4'. Run 'python -m pip install -r .\requirements.txt'.You can verify by 'django-admin --version', it should give 5.0.4
   NOTE: command 'python -m pip freeze > req1.txt' would create req1.txt file that containes all python  dependencies.
3) PS C:\Users\hi\Desktop\projects\python_projects\django_ecomm> django-admin startproject dj_ecomm
4) PS C:\Users\hi\Desktop\projects\python_projects\django_ecomm\dj_ecomm> python .\manage.py startapp store
*********************************************************************

1) PS C:\Users\hi\Desktop\projects\python_projects\django_ecomm\dj_ecomm> python manage.py migrate
2) PS C:\Users\hi\Desktop\projects\python_projects\django_ecomm\dj_ecomm> python manage.py createsuperuser   (u/n=admin, p/w=admin)
   and 'python manage.py runserver 0.0.0.0:8000' or 'python manage.py runserver'. Goto URL 'localhost:8000/admin'

3) create models.py and then run makemigration and migrate command. Then create admin.py file
   Create a user=ash, p/w=ash12345
 NOTE: this invokes post_save() function defined in  models.py
*************************************************************************

1) create .../dj_ecomm/settings/{base.py,developement.py,production.py}
2) Open manage.py and change "os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dj_ecomm.settings')" to
   "os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dj_ecomm.settings.development')"
   
   Now we add our production and development settings in their respective file.
******************************

Now add package 'django-allauth==0.61.1' and add necessary code in  base.py file(change INSTALLED_APPS,
MIDDLEWARE), urls.py. Also run migrations and in admin you will see 3 new tables under 'Social Accounts':
Social accounts, social application tokens, social applications. Also 1 more tables 'Email address' under 'Accounts'

******************************
Now add ../store/urls.py and add necessary code in dj_ecomm/urls.py. Create ../templates/home.html and change
TEMPLATES -> DIRS attribute. In dir ../templates/{home.html,base.html,navbar.html,footer.html,scripts.html}
Also create ../store/templatetags/cart_template_tags.py with necessary code in it.

*******************************
Now run "python manage.py collectstatic". This will create 'static_root' dir that would store all static files for
proper rendering of admin, etc pages...................

***********************
Now we get  django-debug-toolbar-4.3.o working:
1) In settings/development.py change MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ], INSTALLED_APPS += ['debug_toolbar'], and DEBUG_TOOLBAR_PANELS =[...]
2) In urls.py change 'urlpatterns'.
3) run 'python manage.py collectstatic' command

**********************************
ISSUE: At one point I received following error:
django.db.migrations.exceptions.InconsistentMigrationHistory: Migration socialaccount.0001_initial is applied before its dependency sites.0001_initial on database 'default'.
Solution: delete all tables and then run 'python.exe .\manage.py makemigrations' and 
then ' python.exe .\manage.py migrate   '
************************************

Now we get django-crispy-forms:
1) Add 'django-crispy-forms==1.14.0' in requirements.txt and run 'python -m pip install -r .\requirements.txt'
2) in settings/base.py, add 'crispy_forms' to INSTALLED_APPS, add CRISPY_TEMPLATE_PACK = 'bootstrap4'
3) In templates/account/{signup.html,etc}, invoke above by using  {% load crispy_forms_tags %} and append the |crispy filter to your form or formset context variable.

*****************************
ISSUE: TemplateDoesNotExist at /order-summary/
order_summary.html

solution: Since I just created this html file, so restart the server. 
***********************************

