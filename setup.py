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