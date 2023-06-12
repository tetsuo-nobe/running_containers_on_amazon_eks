# Amazon ECR にコンテナイメージをpushする

* 下記が使用できる環境が必要
 - docker コマンド
 - AWS CLI 
 - 対象リポジトリへの push が許可されている IAM の認証情報

* レジストリに対して Docker クライアントを認証
  - 次の例では AWS アカウント ID が 000000000000 で 東京リージョンのレジストリに対して認証
  ```
  aws ecr get-login-password --region ap-northeast-1 | docker login --username AWS --password-stdin 000000000000.dkr.ecr.ap-northeast-1.amazonaws.com
  ```
* Docker イメージ をビルド
  - 次の例では hellodemo をタグとして指定してビルド
  ```
  docker build -t hellodemo .

  ```
* ビルド完了後、リポジトリにイメージをプッシュできるように、イメージにタグを付け
  ```
  docker tag hellodemo:latest 000000000000.dkr.ecr.ap-northeast-1.amazonaws.com/hellodemo:latest

  ```
* リポジトリにこのイメージをプッシュ
  ```
  docker push 000000000000.dkr.ecr.ap-northeast-1.amazonaws.com/hellodemo:latest

  ```  
