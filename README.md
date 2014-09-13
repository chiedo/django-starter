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

- To start your django project, run the following:
```
django-admin startproject project_name
```

###Notes:
>* If you have an issue with mysql not connecting, you may need to restart mysql by running 'sudo service mysql restart'
>* Be sure to delete the .git folder after cloning this repo if you intend to use it for a completely unrelated project.
