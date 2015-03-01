Django-vagrant-starter
=========
<img src="https://travis-ci.org/chiedojohn/django-vagrant-starter.svg?branch=master" />

A framework for a new Django 1.7/python 2.7 project utilizing vagrant for setting up the development environment.

READ THIS FIRST (DO NOT IGNORE): https://gist.github.com/chiedojohn/c3e37041b829f28c0c78
----------

Local Development Environment
----------
- Before anything, be sure to set up your AWS environment variables in ~/.basrc within vagrant. You must set up S3 and all your environemnet variables in vagrant under ~/.bashrc before begginning.
- To start your django project, run the following inside your vagrant VM:
```
cd /vagrant (not cd vagrant)
sudo pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
```

###Notes:
Run the server within vagrant at /vagrant by running the following: 
```
python manage.py runserver 0.0.0.0:8000
```


Testing
=====================
The code should be commented pretty thouroughly. If anything is unclear, please let me know. These are not perfect tests nor are they exhaustive. You will want to write beter tests than these that covers more test cases. This is a great start though, and the other test cases should be trivial.

- You can have your tests auto run with gulp but first, get the necessary node packages installed:
```
sudo npm install gulp -g
npm install
```

- Now run the following so that your tests will run everytime a file changes.
```gulp tests```

- To run tests individually, you can just run the following
```python manage.py test app_name```

Testing concept examples
-------------------
- Models
-- apps/people/tests/test_person_model.py
- Views
-- apps/home/tests/test_views.py
-- app/people/tests/test_people_api.py
- Misc classes
-- apps/people/tests/test_example_class.py
- Stubs (pretend)
-- apps/people/tests/test_example_class.py
- Mocks (mock)
-- apps/people/tests/test_example_class.py

Some Helpful External Docs
-----------
- Expects - https://github.com/jaimegildesagredo/expects
- Nosetests - https://nose.readthedocs.org/en/latest/
- Django-nose - https://github.com/django-nose/django-nose
