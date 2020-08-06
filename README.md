# OAuth_template  
This is a template repository for OAuth pages  

## Installation  
pip install -r requirements.txt

## Run the app  
export FLASK_APP=hello.py  
flask run

Now you can access the app using a web browser at http://127.0.0.1:5000/

####  Advanced  
export FLASK_APP=hello.py  
export FLASK_RUN_PORT=5005  
export FLASK_ENV=development 

flask run --host=0.0.0.0 --port=5005  

## OR run the app using gunicorn:   
gunicorn -w 1 -b 127.0.0.1:5005 hello:app
