# Pokemon

## Process

To Run Airflow with docker, you need to run airflow-init first in the directory airflow (`cd airflow`) with the following command :

```
docker compose up --build airflow-init
```

Then run :

```
docker compose up --build
```

Few time later, the image is built and airflow run in docker. You can access to Airflow webserver at
http://localhost:8080 . Login and password are both **airflow**.
