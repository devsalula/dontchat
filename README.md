# Dontchat
Dontchat is a simple chat with rooms and capacity to save the yours messages and send to your email. 

***Dontchat doesn't have privacy, not being recommended to private talks and to save your sensible datas.***

This project was built with Flask, SocketIO, MongoDB.

## Run Dontchat
For run this project, is necessary to install [docker](https://docs.docker.com/get-docker/) and [docker compose](https://docs.docker.com/compose/install/).

After installing the Docker tools. Run this command:
```
docker-compose -f docker-compose.yml up --build
```

This command going to build every our server, downloading the docker images and after run the Dontchat.

**Important:** Make sure that, you have a ```local.env``` file with the enviroment variables. In repository has ```local-default.env``` as an example to fill the your ```local.env```.

### Emails Impediments
Dontchat uses the Gmail Server to your send emails. But it has a restrict, the Google limit access of third to protect G Suite Accounts.

In [site of Twilio](https://www.twilio.com/blog/2018/03/send-email-programmatically-with-gmail-python-and-flask.html) has tips to using Gmail Server with your Gmail Account.

