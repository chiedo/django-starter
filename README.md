Django-starter
=========
<img src="https://travis-ci.org/chiedojohn/django-starter.svg?branch=master" />

A framework for a new Django 1.7/python 2.7 project utilizing vagrant or docker for setting up the development environment.

Notes: Docker is much faster and much more forgiving to changes although it has a slight learning curve. Do not have your vagrant vm and boot2docker running at the same time to prevent annoying issues. Vagrant at this point is a second class citizen and may not actively be maintained.

Platform Specific Notes
====================
Docker Notes
--------------
First read: https://gist.github.com/chiedojohn/e7ece910ef4a7e3ce125

You will need to set up a file by the name of .env in the root of your project to store private environments that should not be committed to the git repository. It should have the following contents that you can customize if needed.
```
#DJANGO
DJANGO_ENV=development
DJANGO_SECRET_KEY=None
#MYSQL
MYSQL_DATABASE=app_development
MYSQL_USER=root
MYSQL_PASSWORD=root
# This needs to be set if you are using root as the username
MYSQL_ROOT_PASSWORD=root
# This is using the docker link
MYSQL_HOSTNAME=db
MYSQL_PORT=3306
```

Vagrant Notes
----------------
First read: https://gist.github.com/chiedojohn/c3e37041b829f28c0c78

Local Development Environment
=================
- To start your django project, run the following in your container or vm.
```
python manage.py migrate
python manage.py createsuperuser
```

###Notes:
Run the server by running the following: 
```
python manage.py runserver 0.0.0.0:8000
```

Testing
=====================
The code should be commented pretty thouroughly. If anything is unclear, please let me know. These are not perfect tests nor are they exhaustive. You will want to write beter tests than these that covers more test cases. This is a great start though, and the other test cases should be trivial.

- To have your tests run every time you save a python file, run the following.
```gulp tests```

- To run tests individually, you can just run the following
```python manage.py test app_name```

Testing concept examples
-------------------
- Models
  - apps/people/tests/test_person_model.py
- Views
  - apps/home/tests/test_views.py
  - app/people/tests/test_people_api.py
- Misc classes
  - apps/people/tests/test_example_class.py
- Stubs (pretend)
  - apps/people/tests/test_example_class.py
- Mocks (mock)
  - apps/people/tests/test_example_class.py

Some Helpful External Docs for testing
-----------
- Expects - https://github.com/jaimegildesagredo/expects
- Nosetests - https://nose.readthedocs.org/en/latest/
- Django-nose - https://github.com/django-nose/django-nose
