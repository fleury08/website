FROM python:3.12 AS build

RUN mkdir /app
WORKDIR /app
COPY . /app
RUN apt update && apt install rustc -y
RUN pip install poetry
RUN poetry build

FROM python:3.12
RUN apt update && apt install rustc -y
RUN mkdir /app
COPY --from=build /app/dist/*.whl /app/
RUN pip install /app/*.whl

CMD ["uvicorn", "jstanek_backend:app", "--reload", "--host", "0.0.0.0"]

