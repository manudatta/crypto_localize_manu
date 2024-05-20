## Overview

This Flask application contains basic login functionaliy and localize api proxy

## Motivation and Approach

Assignment

- Used built in flask-login for user managment 
- Wrote tests for flask-login 
- The tests cover bare minimum api as part of assigment
- No tests to check proper error conditions

## How to Run

In the top-level directory:
Create a new virtual environment:

```sh
$ cd crypto_localize 
$ python3 -m venv venv
```

Activate the virtual environment:

```sh
$ source venv/bin/activate
```

Install the python packages in requirements.txt:

```sh
(venv) $ pip install -r requirements.txt
```

Set the module that contains the Flask application and specify that the development environment should be used:
They are part of .env file
```sh
(venv) $ export FLASK_APP=localizeapp
(venv) $ export FLASK_ENV=development
```

Create db , migrations and apply those migrations 
```sh
(venv) $ flask db init
(venv) $ flask db migrate 
(venv) $ flask db upgrade 

```
Run development server to serve the Flask application:

```sh
(venv) $ source .env 
(venv) $ python manage.py run
```

## Key Python Modules Used

- Flask: micro-framework for web application development
- SQLAlchemy - ORM (Object Relational Mapper)
- Flask-Restful - simplifies rest

This application is written using Python 3.11.5

## Testing

```sh
(venv) $ python -m pytest
```