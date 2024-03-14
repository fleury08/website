
ARG BACKEND_URL="http://localhost:3000"


FROM node:18 AS build
ENV ENV_BACKEND_URL=BACKEND_URL
COPY . /build
WORKDIR /build
RUN echo ${ENV_BACKEND_URL}
RUN npm ci && npm run build

FROM node:18-slim

ENV ENV_BACKEND_URL=BACKEND_URL
RUN mkdir -p /app/
WORKDIR /app
COPY --from=build /build/build .
COPY --from=build /build/package*.json .
COPY --from=build /build/node_modules ./node_modules

RUN echo ${ENV_BACKEND_URL}
CMD [ "node", "/app/index.js" ]

