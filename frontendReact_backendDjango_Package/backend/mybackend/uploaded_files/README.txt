1) PS C:\Users\hi\Desktop\projects\python_projects\docker_odoo15_postgresql_hospital> docker-compose build --no-cache
2) PS C:\Users\hi\Desktop\projects\python_projects\docker_odoo15_postgresql_hospital> docker-compose up

###################
I entered following during 1st time login when it asked to create database:

master password=mfkm-dse8-vgqx
database name = db_test
Email=admin
Password=admin
############
Issue: Not able to activate developer mode, nor able to see update, etc
Solution: Install any app. I installed Contacts.
###########
At one point I rcvd error:
initdb: error: directory "/var/lib/postgresql/data" exists but is not empty
mydb-1  | initdb: hint: If you want to create a new database system, either remove or empty the directory "/var/lib/postgresql/data" or run initdb with an argument other than "/var/lib/postgresql/data".

Solution: