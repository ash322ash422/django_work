# Vendor_Management_System_with_Performance_Metrics
 
 I used python3.11 for this project running on WINDOWS.

1) Get a clone of the project(make sure you have 'git' installed on  windows):

and then go into the project directory:

C:\Users\hi> git clone https://github.com/ash322ash422/Vendor_Management_System_with_Performance_Metrics my_project

C:\Users\hi> cd my_project

2) Create a virtual env. using python3.11 and activate it as shown in steps below:

C:\Users\hi\my_project> C:\Users\hi\AppData\Local\Programs\Python\Python311\python.exe -m venv venv   <-NOTE: I am using python3.11

C:\Users\hi\my_project> venv\Scripts\activate

(venv) C:\Users\hi\my_project>

3) Install all required packages:

(venv) C:\Users\hi\my_project> pip install -r requirements.txt

4) Go into VMS directory, and enter migrations commands:

(venv) C:\Users\hi\my_project> cd VMS

(venv) C:\Users\hi\my_project\VMS> python manage.py makemigrations

(venv) C:\Users\hi\my_project\VMS> python manage.py migrate 

5) I already have created superuser='admin' with password='admin'. So following command may not be useful to you:

(venv) C:\Users\hi\my_project\VMS> python manage.py createsuperuser

6) Now run the server: 

(venv) C:\Users\hi\my_project\VMS> python manage.py runserver

Now if you goto URL 'http://127.0.0.1:8000', you would see all endpoints. Keep the server running.

***********************************************

7) Now open another terminal(a.k.a. command line) and perform individual test as described below:

NOTE: Make sure you are in virtual env. as described below.

*******************
The following commands are on a brand new terminal :

C:\Users\hi> cd my_project

C:\Users\hi\my_project> venv\Scripts\activate

(venv) C:\Users\hi\my_project>

******************

Now go inside 'VMS\api' directory and run test to verify functionality of endpoints as described below:

(venv) C:\Users\hi\my_project> cd VMS\api

(venv) C:\Users\hi\my_project\VMS\api> python test/test_api1_vendors.py

This checks following endpoints:

POST /api/vendors/

GET /api/vendors/

GET /api/vendors/{vendor_id}/

PUT /api/vendors/{vendor_id}/

DELETE /api/vendors/{vendor_id}/

(venv) C:\Users\hi\my_project\VMS\api> python test/test_api2_purchase_orders.py

This checks following endpoints:

POST /api/purchase_orders/

GET /api/purchase_orders/

GET /api/purchase_orders/{po_id}/

PUT /api/purchase_orders/{po_id}/

DELETE /api/purchase_orders/{po_id}/

(venv) C:\Users\hi\my_project\VMS\api> python test/test_api3_backend_logic.py

This checks following endpoints:

GET /api/vendors/{vendor_id}/performance/

PUT /api/purchase_orders/{po_id}/acknowledge/

-OR- you can run all of the above 3 test and other tests by going up 1 directory and simply typing:

(venv) C:\Users\hi\my_project\VMS> python.exe manage.py test -v 2 api/test/

8) I performed above test and output is given in file test_output.txt

If you have any further questions, email me: ash322.ash422@gmail.com