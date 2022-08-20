# Amazon ECR の Public リポジトリからベースイメージを取得
FROM public.ecr.aws/ubuntu/ubuntu:18.04

# Node.js をインストール
RUN apt update && apt install -y nodejs

# index.js にアプリのコードを記述
RUN echo "console.log('Hello, world')" > index.js

# node index.js を実行
CMD ["node", "index.js"]
