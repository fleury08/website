###########
#BUILD ENV#
###########

FROM node:current AS build

ARG ENV_FRONTEND_API_PATH=/api
ENV ENV_FRONTEND_API_PATH=${ENV_FRONTEND_API_PATH}

ARG ENV_FRONTEND_WS_PATH=/ws
ENV ENV_FRONTEND_WS_PATH=${ENV_FRONTEND_WS_PATH}


WORKDIR /build
COPY ./src ./src
COPY ./components.json .
COPY ./package-lock.json .
COPY ./package.json .
COPY ./tsconfig.json .
COPY ./svelte.config.js .
COPY ./tailwind.config.js .
COPY ./postcss.config.cjs .
COPY ./vite.config.ts .
COPY ./.npmrc .

RUN touch .env
RUN echo "ENV_FRONTEND_API_PATH=${ENV_FRONTEND_API_PATH}" >> .env
RUN echo "ENV_FRONTEND_WS_PATH=${ENV_FRONTEND_WS_PATH}" >> .env

RUN npm install --verbose
RUN npm run build

###############
#BUILD TO PROD#
###############
FROM node:current-slim

RUN mkdir -p /app/
WORKDIR /app
COPY --from=build /build/build .
COPY --from=build /build/package*.json .
COPY --from=build /build/node_modules ./node_modules
COPY --from=build /build/.env ./.env
RUN cat .env

CMD [ "node", "/app/index.js" ]

