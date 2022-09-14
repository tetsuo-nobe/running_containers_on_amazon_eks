# Kustomizeのデモ

* EKSクラスターに接続できる環境を用意

* サンプルを取得して移動
  ```
  git clone https://github.com/tetsuo-nobe/running_containers_on_amazon_eks
  cd running_containers_on_amazon_eks/mod4/kustomizedemo

  ```
* kubectl のバージョン確認 (1.14 以降であることを確認）
  ```
  kubectl version --short --client

  ```
* base フォルダの my-deployment.yaml の内容を確認

* overlays フォルダ配下の dev, stage, prod フォルダ内の kustomization.yaml の内容を確認

* 次のコマンドで生成されるマニフェストを確認
  ```
  kubectl kustomize -f ./overlay/dev

  ```
  - stage や prod についても同様に確認
* 次のコマンドでdev環境用の Deploymentを作成
  ```
  kubectl create -k ./overlay/dev

  ```
  - stage や prod についても同様に作成
* 作成された Deployment や Pod を確認
  ```
  kubectl get pods,deployments

* 次のコマンドでdev環境用の Deploymentを削除
  ```
  kubectl delete -k ./overlay/dev

  ```
  - stage や prod についても同様に削除
  


