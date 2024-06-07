FROM ubuntu:rolling AS build

RUN mkdir /app
WORKDIR /app
COPY . /app

#arm64 library specifics
RUN apt update
RUN apt install rustc python3-pip -y
RUN pip install poetry
RUN poetry lock --no-cache
RUN poetry build

FROM ubuntu:rolling
RUN apt update
RUN apt install rustc -y
RUN mkdir /app
COPY --from=build /app/dist/*.whl /app/
RUN pip install --upgrade pip setuptools wheel
RUN pip install /app/*.whl

CMD ["uvicorn", "jstanek_backend:app", "--reload", "--host", "0.0.0.0"]

