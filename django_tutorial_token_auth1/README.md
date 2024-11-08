# django_tutorial_token_auth1
 I used python3.12

1) ..\APITOKEN> python manage.py createsuperuser --username admin --email admin@example.com

2) ..\APITOKEN> python manage.py drf_create_token admin

Generated token 9a3faecbe7a754de5866d11eeeaf893f55aaa991 for user admin

3) Now add this token inside test_core.py

4) Now run the server: ..\APITOKEN> python manage.py runserver

Now open  another terminal and type : 

..\APITOKEN\core> python.exe .\test_core.py

Response from server: {'token': '9a3faecbe7a754de5866d11eeeaf893f55aaa991'}

token= 9a3faecbe7a754de5866d11eeeaf893f55aaa991

#############################

Response from server: {'message': 'Hello, Token Auth World!'}

###############################
NOTE: If you do NOT provide token, then you will get 
{"detail":"Authentication credentials were not provided."}
