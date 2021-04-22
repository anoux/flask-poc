# My first Flask project

Flask is a python framework used for web app developments. A framework is a code library that make it easier to build web apps. A framework provides **reusable code**. Other python frameworks are Tornado, Django and Pyramid

## API building process

### API for a To-Do List web application where:

- Visitors can register new accounts
- Registered users can log in, log out, see info for their profiles and edit it
- Registered users also can create new task items, see their existing tasks and edit them

These ¿¿**functions**?? are coded on a set of API endpoints. Each backend implement API endpoints along with HTTP methods (VER BIEN ESTO)

- GET /
- POST /accounts
- POST /accounts/login
- POST /accounts/logout
- GET, PUT, DELETE /accounts/<str : username>
- GET, POST /accounts//<str : username>/tasks
- GET, PUT, DELETE /accounts/<str : username>/tasks/<imt : id>

## Flask startup

First, I created a new directory (mkdir **Flask**). Second, I got to that cd and created a virtual enviroment inside it (**zira_env**) and activate it. Third I installed Flask and Flask-sqlalchemy. I did not installed Python although I think I may did it when installed Flask. 

```bash
mkdir Flask
cd Flask
virtualenv zira_env
zira_env/bin/activate
pip install Flask Flask-sqlalchemy
mkdir todo
```

Then I turned the codebase into an installable Python distribution (VER BIEN ESTO) 

I used sublime to code. I started a new project and added this **Flask** directory to it. I created a **setup.py** file in sublime. 

```python
from setuptools import setup, find_packages
requires = [
	'flask',
	'flask-sqlalchemy',
	'psycopg2'
]
# All necessary packages for deloyment are listed in this requires list
setup(
	name='flask_todo',
	version='0.0',
	description='A To-Do List built with Flask',
	author='Anoux',
	author_email='ajadur96@gmail.com',
	keywords='web flask',
	packages=find_packages(),
	include_packafes_data=True,
	install_requires=requires
)
# Setup is .......... ?
```

So I created a **app.py** file inside **todo** and a blank **__Init__.py** file. 