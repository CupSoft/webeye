FROM node:14-alpine AS builder
WORKDIR /app
COPY package.json ./
COPY . .
RUN npm install


ARG REACT_APP_API_HOST
ARG REACT_APP_API_PORT

ENV REACT_APP_API_HOST=$REACT_APP_API_HOST
ENV REACT_APP_API_PORT=$REACT_APP_API_PORT

RUN npm run build

FROM nginx:1.19-alpine AS server
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=builder ./app/build /usr/share/nginx/html
