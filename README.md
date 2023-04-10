
# Introduction
This repository is an example of how we can collect changes on our models and query those changes through an api.

For large volumes of data it is better to use a persistence system designed for this use case:
- If you usually look at the logs, Elasticseach with a combination of tier warm for daily writes and another freeze for storage and long term reads for example.
- If data is consumed very infrequently and queries do aggregations/metrics, BigQuery is a good choice.

# Index
<!-- TOC -->
* [Introduction](#introduction)
* [Index](#index)
* [Setup local](#setup-local)
  * [Copy envfile](#copy-envfile)
  * [Dependencies](#dependencies)
  * [Prepare database](#prepare-database)
  * [Create superuser](#create-superuser)
  * [Start local web server](#start-local-web-server)
* [Play](#play)
* [Containers](#containers)
  * [Docker](#docker)
    * [Build](#build-)
  * [Docker Compose](#docker-compose)
    * [Build](#build)
    * [Start all](#start-all)
    * [Run migrations](#run-migrations)
    * [Run tests](#run-tests)
<!-- TOC -->

# Setup local
## Copy envfile

```sh
cp .env.example .env
```
## Dependencies

```sh
pip install -r requirements.txt
```

## Prepare database

```sh
python manage.py migrate 
```

## Create superuser
Follow the instructions in the shell
```sh
python manage.py createsuperuser 
```


## Start local web server
```sh
python manage.py runserver 
```

# Play

For more information about the api, please refer to the automatically generated documentation.
- [Open API](http://localhost:8000/api/schema/open-api.yaml)
- [Swagger](http://localhost:8000/api/schema/swagger/)


# Containers

## Docker
### Build 
```sh
docker build -t auditlog .
```

## Docker Compose
### Build
```sh
docker compose build
```

### Start all
```sh
docker compose build
```

### Run migrations
```sh
docker-compose exec api python manage.py migrate --noinput
```

### Run tests
```sh
docker compose -f docker-compose.yml -f docker-compose.test.yml run api
```
