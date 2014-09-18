Django-vagrant-starter
=========
A framework for a new Django 1.6/python 2.6 project utilizing vagrant for setting up the development environment.

Local Development Environment
----------
> Requirements: Vagrant and Virtual Box

> It will be assumed that you are familiar with vagrant.

> ####Local Mysql port: 5433

> ####Local http port: 3001

> ####Mysql username: root

> ####Mysql password: root

> ####Existing database: django_app_default

- To start your django project, run the following inside your vagrant VM:
```
django-admin startproject project_name
```

###Notes:
>* If you have an issue with mysql not connecting, you may need to restart mysql by running 'sudo service mysql restart'
>* Be sure to delete the .git folder after cloning this repo if you intend to use it for a completely unrelated project.
>* Because of the nature of vagrant, you will need to run the Django server from your Vagrant VM on port 0.0.0.0 to be able to acces it from your local machine with the following script.
```
python manage.py runserver 0.0.0.0:8000
```

###Notes for elastic beanstalk users:
>* Before doing any Elastic Beanstalk interaction, be sure that you have initialized the git repo
>* You should do all of your elastic beanstalk interaction via the vagrant VM. All of your git commands other than 'git aws.push' should be run on your local machine.
>* Before you can push to Elastic Beanstalk for the first time, you will need to navigate to /vagrant then run the following
```
eb init
```
>* After you do this, make sure .elasticbeanstalk/ and .ebextensions/ ARE NOT in .gitignore.

