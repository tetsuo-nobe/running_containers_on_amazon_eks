# Docker のコンテナを動かしてみよう

## 講師がガイドする環境を使用してください。
   - Architecting on AWS の場合
       - ラボ 1 の EC2 インスタンス **Command Host** に Session Manager で接続してください。
   - Running Containers on Amazon EKS の場合
       - ラボ 2 の EC2 インスタンス Bastion Host に Session Manager で接続してください。

### このワークの目的は、コンテナをアプリケーションとしてビルド・実行するための基本的な手順を体感することです。

### 準備

1. Docker がインストールされていることを確認します。
   ```
   docker -v
   ```

1. 現在の OS ユーザーを docker グループに所属させます。
   ```
   sudo usermod -a -G docker ssm-user
   ```

1. 下記コマンドでいったん Session Manager を終えます。
   ```
   exit
   ```
   
1. 再度、Session Manager に接続します。

### 既存のコンテナイメージを使用してコンテナを実行する

1. Apache HTTP Server(httpd) のコンテナを取得し、ポート 80 を使用してデーモンとして実行させます。`httpd:2.4.59` のうち、`:` の後はタグの値です。
   ```
   docker run --name my-httpd -dit -p 80:80 httpd:2.4.59
   ```

1. http コンテナが動作していることを確認します。CONTAINER ID や NAMES が表示されていることを確認します。
   ```
   docker ps
   ```
   
1. http コンテナにアクセスします。
   ```
   curl localhost
   ```
   - `<html><body><h1>It works!</h1></body></html>` と表示されることを確認します。

1. http コンテナを停止します。
   ```
   docker stop my-httpd
   ```

1. http コンテナが動作していないことを確認します。CONTAINER ID や NAMES が表示されていないことを確認します。
   ```
   docker ps
   ```
1. http コンテナを削除します。
   ```
   docker rm my-httpd
   ```

### Web アプリケーションのコンテナイメージをビルド（構築）して実行する

1. サンプルの Git リポジトリを取得して今回使用するサンプルのフォルダに移動します。
   ```
   git clone https://github.com/tetsuo-nobe/running_containers_on_amazon_eks.git
   ```

   ```
   cd running_containers_on_amazon_eks/docker_basic
   ```
   
1. サンプルの アプリケーションのコードを確認します。(Python で Flask という Webアプリケーションフレームワークを使用しています。）
   ```
   cat app/app.py
   ```   

1. サンプルアプリケーションのコンテナイメージをビルドするための Dockerfile を確認します。
   ```
   cat Dockerfile
   ```   

1. サンプルアプリケーションのコンテナイメージをビルドします。
   ```
   docker build -t myflask:1 . 
   ```   

1. サンプルアプリケーションのコンテナを実行します。
   ```
   docker run --name myflask1 -dit -p 80:8080 myflask:1
   ```   

1. サンプルアプリケーションのコンテナが動作していることを確認します。CONTAINER ID や NAMES が表示されていることを確認します。
   ```
   docker ps
   ```
   
1. サンプルアプリケーションのコンテナにアクセスします。
   ```
   curl localhost
   ```
   - `<h1>Hello, Flask!</h1>` と表示されることを確認します。

1. サンプルアプリケーションのコンテナを停止します。
   ```
   docker stop myflask1
   ```
   
1. サンプルアプリケーションのコンテナを削除します。
   ```
   docker rm myflask1
   ```

1. サンプルアプリケーションのコンテナイメージを削除します。
   ```
   docker image rm myflask:1
   ```

1. 以上で終了です。
   
### お疲れさまでした！

1. ワーク環境が不要になったら、下記のコマンドで Session Manager を終えてマネジメントコンソールからサインアウトしてください。
   ```
   exit
   ```

