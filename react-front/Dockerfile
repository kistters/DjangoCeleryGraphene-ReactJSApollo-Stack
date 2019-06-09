FROM node:10-alpine

# set working directory
WORKDIR /usr/src/app

RUN npm i npm@latest -g && chown node:node /usr/src/app

# install and cache app dependencies
COPY package.json package-lock.json* ./
RUN npm install --no-optional && npm cache clean --force

# add `usr/src/app/node_modules/.bin` to $PATH
ENV PATH /usr/src/app/node_modules/.bin:$PATH

COPY . .

# start app
CMD ["npm", "start"]
