# Copyright 2022 Amazon Web Services, Inc. or its affiliates. All rights reserved.
FROM node:12

# アプリケーションディレクトリを作成する
WORKDIR /usr/src/app

# npm install
RUN npm install

# アプリケーションのソースをバンドルする
COPY . .

EXPOSE 8080
CMD [ "node", "server.js" ]
