FROM node:latest

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

COPY package.json .
COPY package-lock.json .
COPY tsconfig.json .
RUN npm install --silent

COPY . .

CMD ["npm", "start"]
