FROM ubuntu:rolling AS build

RUN mkdir /app
WORKDIR /app
COPY . /app

#arm64 library specifics
RUN apt update
RUN apt install python3-pip python3-poetry -y
RUN poetry lock --no-cache
RUN poetry build


######
# PROD BUILD
######
FROM ubuntu:rolling
RUN apt update
RUN apt install python3-pip python3-venv python3-poetry -y
RUN mkdir /app
COPY --from=build /app/dist/*.whl /app/
RUN python3 -m venv /app/venv
RUN /app/venv/bin/pip3 install /app/*.whl

CMD ["/app/venv/bin/uvicorn", "jstanek_backend:app", "--reload", "--host", "0.0.0.0"]

