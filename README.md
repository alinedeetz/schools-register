[![Build Status](https://img.shields.io/docker/cloud/build/alineem/dice-roll)](https://hub.docker.com/repository/docker/alineem/schools-register/builds) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

# Schools Registrer

This is a Python based system for registering school data. It is possible to register new schools, change and delete data already registered, list all schools and search for them by name.

## How to run

### Docker Hub
In order to run this container you'll need docker installed.

#### Mandatory environment variables

Run the following command:

>$ docker run -e SCHOOLS_REGISTER_DB_USERNAME="username" -e SCHOOLS_REGISTER_DB_PASSWORD="password" -e SCHOOLS_REGISTER_DB_HOSTNAME="hostname" -e SCHOOLS_REGISTER_DB_PORT="port" -e SCHOOLS_REGISTER_DB_NAME="database-name" --rm -p 5000:5000 alineem/schools_register

### PostgreSQL 

You have to connect a PostgreSQL database for this application to work and then execute the "ddl.sql" script on it.

