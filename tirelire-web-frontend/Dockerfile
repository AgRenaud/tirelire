FROM node:14.17.4-alpine3.14 as develop-stage
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .

FROM develop-stage as build-stage
WORKDIR /app
RUN npm run build

FROM nginx:1.23.0-alpine as production-stage
ENV NGINX_HOST=localhost\
    NGINX_PORT_HTTP=80
COPY --from=build-stage /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
