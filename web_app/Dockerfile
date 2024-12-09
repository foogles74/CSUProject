FROM node:22.11

WORKDIR /usr/src/app

COPY ./app/package*.json ./
RUN npm ci

COPY ./app ./
RUN npm install

RUN npm run build

EXPOSE 3000
CMD ["node","--env-file=.env", "build"]