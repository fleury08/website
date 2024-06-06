FROM node:current AS build

ARG ENV_FRONTEND_API_PATH=/api
ENV ENV_FRONTEND_API_PATH=${ENV_FRONTEND_API_PATH}

ARG ENV_FRONTEND_WS_PATH=/ws
ENV ENV_FRONTEND_WS_PATH=${ENV_FRONTEND_WS_PATH}


COPY ./src /build/src
COPY ./*.json /build/
COPY ./*.js /build/
COPY ./*.cjs /build/
COPY ./*.ts /build/
COPY ./.npmrc /build/
WORKDIR /build

RUN touch .env
RUN echo "ENV_FRONTEND_API_PATH=${ENV_FRONTEND_API_PATH}" >> .env
RUN echo "ENV_FRONTEND_WS_PATH=${ENV_FRONTEND_WS_PATH}" >> .env

RUN npm ci && npm run build


FROM node:current-slim

RUN mkdir -p /app/
WORKDIR /app
COPY --from=build /build/build .
COPY --from=build /build/package*.json .
COPY --from=build /build/node_modules ./node_modules
COPY --from=build /build/.env ./.env

CMD [ "node", "/app/index.js" ]

