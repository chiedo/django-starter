FROM python:2.7

# Set up the App
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
ADD package.json /code/

RUN pip install -r requirements.txt
RUN pip install -e git+https://github.com/markfinger/django-node.git#egg=django-node
RUN pip install -e git+https://github.com/markfinger/django-react.git#egg=django-react
