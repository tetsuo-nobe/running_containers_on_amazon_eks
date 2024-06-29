# Helm でアプリケーションをデプロイしてみよう

* HOME ディレクトリに移動
  ```
  cd  ~
  ```
  
* ワーク用リポジトリを取得して移動
  ```
  git clone https://github.com/tetsuo-nobe/running_containers_on_amazon_eks
  cd running_containers_on_amazon_eks/mod4

  ```
* Chart.yaml の確認
  - helmdemo フォルダ(このフォルダ)にある Chart.yamlを参照
  ```
  cat helmdemo/Chart.yaml
  ```
* Deployment の定義ファイルの確認
  - helmdemo フォルダ(このフォルダ)にある templates/deployment/hello-deployment.yamlを参照
  ```
  cat helmdemo/templates/deployment/hello-deployment.yaml
  ```
* values.yaml の確認
  - helmdemo フォルダ(このフォルダ)にあるvalues.yamlを参照
  - レプリカ 2、コンテナイメージに tnobe/node-web-hello、コンテナイメージのバージョンに 1を指定していることがわかる。
  ```
  cat helmdemo/values.yaml
  ```
* `hello-app` アプリケーションとしてデプロイする前にdry-run実行
  ```
  helm install --debug --dry-run hello-app helmdemo/
  ``` 
* `hello-app` アプリケーションとしてデプロイ
  ```
  helm install hello-app helmdemo/
  ``` 
* アプリケーションのステータスの確認
  ```
  helm status hello-app
  ```
* Pod,Deployment,Serviceの確認
  ```
  kubectl get svc,po,deploy
  ```
* service/my-service の EXTERNAL-IP に http:// をつけ、ブラウザでアクセス。
  - アプリケーションのバージョン 1 にアクセスできることを確認
  - (表示されるまで、しばらく時間がかかる場合があります。)

* helmdemo/values.yaml の内容を変更してバージョン 2 のコンテナイメージを指定する
  - あらかじめ用意されている version に 2 を指定した values.yaml.v2 を適用する 
  ```
  mv helmdemo/values.yaml  helmdemo/values.yaml.v1
  ```

  ```
  mv helmdemo/values.yaml.v2  helmdemo/values.yaml
  ```
  
  - vim を使える方は helmdemo/values.yaml を開き、`version:` の値を `'2'` に変更して保存してもかまいません
  - コンテナイメージのバージョンに 2 を指定していることを確認します。
  ```
  cat helmdemo/values.yaml
  ```

* アプリケーションをバージョン2 にアップグレードする
  ```
  helm upgrade hello-app helmdemo/
  ```
* アプリケーションのステータスの確認
  ```
  helm status hello-app
  ```
* Pod,Deployment,Serviceの確認
  ```
  kubectl get svc,po,deploy
  ```
* service/my-service の EXTERNAL-IP に http:// をつけ、ブラウザでアクセス。
  - アプリケーションのバージョン2 にアクセスできることを確認
* アプリケーションのデプロイ履歴を表示
  ```
  helm history hello-app
  ```
* アプリケーションをバージョン1 へロールバック
  ```
  helm rollback hello-app 1
  ```
* アプリケーションがバージョン1 に戻っていることを確認
* アプリケーションをアンデプロイ
  ```
  helm uninstall hello-app
  ```
