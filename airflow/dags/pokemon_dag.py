import datetime as dt

from pokemon_task import send_message

from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    "owner": "axelm",
    "depends_on_past": False,
    "start_date": dt.datetime(2024, 5, 6, 16, 30, 0),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": dt.timedelta(minutes=5),
}

dag = DAG(
    "Pokemon_dag",
    default_args=default_args,
    description="DAG to collect pokemon",
    schedule_interval=dt.timedelta(minutes=120),
)

with dag:
    run_collect_pokemon = PythonOperator(
        task_id="pokemon_catch",
        python_callable=send_message,
        dag=dag,
    )

    run_collect_pokemon  # noqa
