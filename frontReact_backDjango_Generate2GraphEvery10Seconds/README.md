#This app has frontend in react JS that refreshes every 10 sec. It has scatter and line plots whose data is received via the django server. The django server uses rest API framework and has 2 endpoints

- GET http://127.0.0.1:8000/api/data/

- GET http://127.0.0.1:8000/api/data/random_variation/


steps

1) npx create-react-app react_project_name
  
   cd react_project_name

2)  npm install react-plotly.js plotly.js axios