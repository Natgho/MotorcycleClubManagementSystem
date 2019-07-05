# Motorcycle Club Management System

A motorcycle club management system. 

## Installation on Local

Install requirements

```
make install
```

Make database migration

```
make migrations
```

Run project and navigate to
[http://127.0.0.1:8000](http://127.0.0.1:8000)

```
make run
```

## Deployment on Docker

Rename `.env.example` to `.env` and set your environment variables.

**Note**: This file used in **production mode** only.

```
docker-compose up -d --build
```