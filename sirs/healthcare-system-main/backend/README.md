# Healthcare Backend

This is the backend for the Healthcare project. It is a Spring Boot application that uses JPA to connect to a database and manage entities. It provides a REST API for the frontend to use.

## Configuring

Before being able to run the backend application, you must provide a `application.properties` file in the `src/main/resources` directory. An example file is provided, so:

```bash
cp src/main/resources/application.properties.example src/main/resources/application.properties
```

Then, edit the file to provide the correct database connection information.

## Running

To run the backend application, run:

```bash
mvn spring-boot:run
```

in this folder. Please make sure you have maven installed through your favorite package manger.
