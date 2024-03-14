FROM python:3.12

RUN mkdir /app
COPY ./dist/* /app/
RUN pip install /app/*.whl

CMD ["uvicorn", "jstanek_backend:app", "--reload", "--host", "0.0.0.0"]

