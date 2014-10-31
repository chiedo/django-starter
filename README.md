Django-vagrant-starter
=========
A framework for a new Django 1.7/python 2.7 project utilizing vagrant for setting up the development environment.

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
sudo pip install -r requirements.txt
python manage.py migrate
python manage.py createadmin
```

###Notes:
>* If you have an issue with mysql not connecting, you may need to restart mysql by running 'sudo service mysql restart'
>* Be sure to delete the .git folder after cloning this repo if you intend to use it for a completely unrelated project.
>* Because of the nature of vagrant, you will need to run the Django server from your Vagrant VM on port 0.0.0.0 to be able to acces it from your local machine with the following script.
```
python manage.py runserver 0.0.0.0:8000
```

###Notes for elastic beanstalk users:
>* Install Elastic Beanstalk command line tools. If using a mac, you can use homebrew and use the following:
```
brew install aws-elasticbeanstalk
```
>* Before you can push to Elastic Beanstalk for the first time, you will need to navigate to your git repo on your local machine then run the following
```
eb init
```
>* It is recommended that after you run 'eb init', you update the path to your AWS credential file as found in /.elasticbeanstalk/config to /usr/local/AWS/.elasticbeanstalk/ENVIRONMENTNAME_credentials being sure to move the original file to the new path. You will likely have to create that path. This will prevent collisions when you have multiple projects using Elastic Beanstalk on one machine.
>* The Elastic Beanstalk Deployment has not yet been tested due to pure laziness
