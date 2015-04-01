FROM python:2.7

# Set up the App
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
ADD package.json /code/

RUN apt-get install\
  nodejs \
  npm

#Makes sure npm is the latest version. Ubuntu's version is not the latest
RUN npm install -g npm
RUN pip install -r requirements.txt
