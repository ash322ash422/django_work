Here the react JS has 3 different applications:

1) App1.js: Plot a graph based on data and CSV file received from user
   
2) App2.js: Fetch data from django backend to plot, post data, upload / download file to django server

3) App3.js: Here when user presses the button 'submit and plot', the server executes a shell script(main.py) whose output is directed to DB. The output is analysis-data and JSON-figure-data Then output from DB is read. The app has 2 buttons: one for retrieving analysis-data which is then used to render plot, and the other for retrieving JSON-figure-data which is also used to render plot. Note, that figure on frontend can also be generated using JSON-figure-data received from the server. 

################################

1) npm start

This starts the react JS frontend

2) python manage.py runserver

This starts the Django backend server

