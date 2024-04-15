FROM public.ecr.aws/lambda/python:3.11

COPY requirements.txt ${LAMBDA_TASK_ROOT}

RUN pip install --no-cache-dir -r requirements.txt

COPY ./recommandations ${LAMBDA_TASK_ROOT}

CMD [ "daily_recommandation.handler" ]
