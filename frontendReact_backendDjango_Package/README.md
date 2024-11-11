Here I am using package react-plotly, plotly.js for rendering the graph:

SETUP steps for frontend react:

1) Goto appropriate dir and type:
2) 
..\frontendReact_backendDjango> npx create-react-app frontend 

3) cd frontend 
   

4) ..python_projects\frontendReact_backendDjango\frontend> npm install axios

5) ..python_projects\frontendReact_backendDjango\frontend> npm install dotenv

6) create ..frontend/.env file and put variables in there

7) create ..frontend/src/api.js file and put code in there

8) ..python_projects\frontendReact_backendDjango\frontend> npm start


#######################################################

SETUP steps for backend django:(You should know the basic working for django to understand this). I used python3.11 in virtual env.

1) ..python_projects\frontendReact_backendDjango\backend> python -m pip install django

2) ..python_projects\frontendReact_backendDjango\backend> python -m pip install djangorestframework django-cors-headers


3) ..python_projects\frontendReact_backendDjango\backend> django-admin startproject mybackend 

4) ..python_projects\frontendReact_backendDjango\backend\mybackend> python manage.py startapp api

5) Now add code in settings.py, views.py, api/urls.py, mybackend/urls.py, etc file

6) ..python_projects\frontendReact_backendDjango\backend\mybackend> python manage.py migrate

##############################################

To run 

1) First run django server:

 python_projects\frontendReact_backendDjango\backend\mybackend> python manage.py runserver

2)  Then run npm start:

  ..python_projects\frontendReact_backendDjango\frontend> npm start

3) Now open the browser(if it did not open auto.) and goto http://localhost:3000/ .