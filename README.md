Django-vagrant-starter
=========
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
