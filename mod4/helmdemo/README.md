# Helmのデモ

* EKSクラスターに接続できる環境を用意

* Helmのインストール 
  - 次の例では Linux にインストールしてバージョンを確認
  ```
  curl -sSL https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | bash
  helm version --short
  ```
* サンプルを取得して移動
  ```
  git clone https://github.com/tetsuo-nobe/running_containers_on_amazon_eks
  cd unning_containers_on_amazon_eks/mod4

  ```
* Chart.yamlの確認
  - このフォルダにあるChart.yamlを参照
* Deploymentの定義ファイルの確認
  - このフォルダにあるtemplates/deployment/hello-deployment.yamlを参照
* values.yamlの確認
  - このフォルダにあるvalues.yamlを参照
  - レプリカ 2、コンテナイメージのバージョン 1を指定している。
* `hello-app`アプリケーションとしてデプロイする前にdry-run実行
  ```
  helm install --debug --dry-run hello-app helmdemo/
  ``` 
* `hello-app`アプリケーションとしてデプロイ
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
* アプリケーションのバージョン1にアクセスできることを確認
* values.yamlの内容を変更してバージョン2のコンテナイメージを指定する
* アプリケーションをバージョン2にアップグレードする
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
* アプリケーションのバージョン2にアクセスできることを確認
* アプリケーションのデプロイ履歴を表示
  ```
  helm history hello-app
  ```
* アプリケーションをバージョン1へロールバック
  ```
  helm rollback hello-app 1
  ```
* アプリケーションがバージョン1に戻っていることを確認
* アプリケーションをアンデプロイ
  ```
  helm uninstall hello-app
  ```