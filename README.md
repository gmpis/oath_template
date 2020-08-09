# OAuth_template  
This is a template repository for OAuth pages  

## Installation  
`pip install -r requirements.txt`  

Note: *If you haven't already installed pip/pip3, you can do so by running: `sudo apt install python3-pip`*  

## Database  
(Redis is an open source in memory data structure store that can be used as cache, database, and message broker.)  

To install redis server locally run: `sudo apt install redis`  
To connect to a redis server from a python script, a python client for redis needs to be installed.  

Note: *The python client redis-py is included in the requirements.txt file.*  
Note: To connect to a redis server from the terminal run: `redis-cli -h $DB_HOST -p $DB_PORT -a $DB_PASS`  

## Run the app  
`export FLASK_APP=hello.py`  
`flask run`  

Now you can access the app using a web browser at http://127.0.0.1:5000/

####  Advanced  
`export FLASK_APP=hello.py`  
`export FLASK_RUN_PORT=5005`  
`export FLASK_ENV=development`  

`flask run --host=0.0.0.0 --port=5005`  

## OR run the app using gunicorn:   
`gunicorn -w 1 -b 127.0.0.1:5005 hello:app`  

Note: *During development to auto restart the server when a file gets modified, start gunicorn with  ` --reload`*  

Note: *gunicorn is included in the requirements.txt file.*  