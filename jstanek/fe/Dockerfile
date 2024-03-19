FROM node:18 AS build

ARG ENV_BACKEND_URL=http://localhost:8000
ARG ENV_BACKEND_API_PATH=/
ARG ENV_FRONTEND_API_PATH=/api

ENV ENV_BACKEND_URL=${ENV_BACKEND_URL}
ENV ENV_BACKEND_API_PATH=${ENV_BACKEND_API_PATH}
ENV ENV_FRONTEND_API_PATH=${ENV_FRONTEND_API_PATH}

COPY ./src /build/src
COPY ./*.json /build/
COPY ./*.js /build/
COPY ./*.cjs /build/
COPY ./*.ts /build/
COPY ./.npmrc /build/
WORKDIR /build

RUN touch .env
RUN echo "ENV_BACKEND_URL=${ENV_BACKEND_URL}" >> .env
RUN echo "ENV_BACKEND_API_PATH=${ENV_BACKEND_API_PATH}" >> .env
RUN echo "ENV_FRONTEND_API_PATH=${ENV_FRONTEND_API_PATH}" >> .env

RUN npm ci && npm run build


FROM node:18-slim

RUN mkdir -p /app/
WORKDIR /app
COPY --from=build /build/build .
COPY --from=build /build/package*.json .
COPY --from=build /build/node_modules ./node_modules
COPY --from=build /build/.env ./.env

CMD [ "node", "/app/index.js" ]

