# Docker のコンテナを動かしてみよう

## 講師がガイドする環境を使用してください。

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

### 既存のコンテナイメージを使用してコンテナを動作させてみる

1. Apache HTTP Server のコンテナを取得し、ポート 80 を使用してデーモンとして動作させます。
   ```
   docker run --name my-httpd -dit -p 80:80 httpd
   ```

1. コンテナアプリケーションが動作していることを確認します。CONTAINER ID や NAMES が表示されていることを確認します。
   ```
   docker ps
   ```
   
1. コンテナアプリケーションにアクセスします。
   ```
   curl localhost
   ```
   - `<html><body><h1>It works!</h1></body></html>` と表示されることを確認します。

1. コンテナアプリケーションを停止します。
   ```
   docker stop my-httpd
   ```

1. コンテナアプリケーションが動作していないことを確認します。CONTAINER ID や NAMES が表示されていないことを確認します。
   ```
   docker ps
   ```
1. コンテナを削除します。
   ```
   docker ps
   ```

### 新しい コンテナイメージをビルド（構築）して動かしてみよう

1. 
