

FROM node:18 AS build
ARG BACKEND_URL=http://localhost:8000
ENV ENV_BACKEND_URL=${BACKEND_URL}
COPY ./src /build/src
COPY ./*.json /build/
COPY ./*.js /build/
COPY ./*.cjs /build/
COPY ./*.ts /build/
COPY ./.npmrc /build/
WORKDIR /build

RUN touch .env
RUN echo "ENV_BACKEND_URL=${BACKEND_URL}" >> .env

#RUN echo ${ENV_BACKEND_URL}
#RUN echo ${BACKEND_URL}
RUN npm ci && npm run build

FROM node:18-slim
ARG BACKEND_URL=http://localhost:8000
ENV ENV_BACKEND_URL=${BACKEND_URL}
RUN mkdir -p /app/
WORKDIR /app
COPY --from=build /build/build .
COPY --from=build /build/package*.json .
COPY --from=build /build/node_modules ./node_modules
COPY --from=build /build/.env ./.env
#RUN echo ${ENV_BACKEND_URL}
#RUN echo ${BACKEND_URL}

CMD [ "node", "/app/index.js" ]

