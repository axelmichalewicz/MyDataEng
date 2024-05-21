
FROM apache/airflow:latest
# USER 50000
# RUN apt-get update
# RUN apt-get -y install gcc
# RUN apt-get -y install gosu
COPY requirements.txt .
USER airflow
RUN pip install --no-cache-dir -r requirements.txt

# FROM apache/airflow:latest
# ADD requirements.txt .
# USER airflow
# RUN pip install --no-cache-dir --user -r requirements.txt