# Ready-To-Deploy Django, gunicorn, NGINX, Docker Application

## Credit
This repository is modified from the code created by [Watt Iamsuri](https://github.com/wiamsuri/django-gunicorn-nginx-docker).

## Getting Started
For Ubuntu (remember to login/logout after running command)
```
sudo curl -sSL https://get.docker.com/ | sh
sudo usermod -a -G docker $(whoami)
sudo service docker start
sudo curl -L "https://github.com/docker/compose/releases/download/1.25.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

In the root level of this repository, create a file named `django.env` and add environment variables. For example:
```
MYSITE_SECRET_KEY= put your django app secret key here
DEBUG=True
```

Build code with docker compose
```
docker-compose build
```

Run the built container
```
docker-compose up -d
```
