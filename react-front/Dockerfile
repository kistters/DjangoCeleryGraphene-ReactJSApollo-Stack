FROM node:10-alpine

# set working directory
WORKDIR /usr/src/app

# install and cache app dependencies
COPY package.json package-lock.json* ./
RUN npm install && npm cache clean --force

# add `usr/src/app/node_modules/.bin` to $PATH
ENV PATH /usr/src/app/node_modules/.bin:$PATH

COPY . .

# start app
CMD ["npm", "start"]
