FROM node:16



# Create app directory
WORKDIR /usr/src/app

# install node_modules
ADD package.json /usr/src/app/package.json
RUN npm install

# copy codebase to docker codebase
ADD . /usr/src/app

EXPOSE 8080

CMD [ "npm", "start" ]
