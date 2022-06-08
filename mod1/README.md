# kubectl を使用して kubernetes のリソースを操作してみよう

## 環境への接続について

* 講師よりガイドいたします。

## 事前準備

* ユーザーのホームディレクトリに移動して、git をインストールします。
  ```
  cd
  pwd
  sudo yum install git -y
  ```

## Minnikube の起動

* Minikube を起動してステータスを確認します。 
  ```
  minikube start --vm-driver=none
  minikube status
  ```

## ワーク用リポジトリの取得

* ワーク用リポジトリをクローンして移動します。
  ```
  git clone https://github.com/tetsuo-nobe/running_containers_on_amazon_eks.git
  cd running_containers_on_amazon_eks/mod1
  ```

---

## Pod の操作

* Podのマニフェストを確認します。
  ```
  cat pod-httpd.yaml
  ```
* Podを作成します。
  ```
  kubectl create -f pod-httpd.yaml
  ```
* Podのステータスを確認します。
  ```
  kubectl get pods
  kubectl get pods -o wide
  ```
* Podの詳細を表示します。
  ```
  kubectl describe pods my-httpd-pod
  ```
* Podのコンテナに接続します。
  ```
  kubectl exec -it my-httpd-pod -- /bin/bash
  ```
* 現在のindex.htmlの内容を表示した後、exit します。
  ```
  ls
  cd htdocs
  more index.html
  exit
* Podを削除します。
  ```
  kubectl delete -f pod-httpd.yaml
  ``` 
* Podの削除を確認します。
  ```
  kubectl get pods
  ``` 
---

## ConfigMapの操作

* alias を使って、キータイプ量を減らす
  - キータイプの効率を考慮し、以降は k で統一します。

  ```
  alias k=kubectl
  ```

* ConfigMapのマニフェストを確認します。  
  ```
  cat configmap.yaml
  ```

* ConfigMapを作成します。
  ```
  k create -f configmap.yaml
  ```

* ConfigMapをステータスを確認します。
  ```
  k get configmaps
  ```

* ConfigMapの詳細を表示します。
  ```
  k describe configmap my-configmap
  ```

* ConfigMapを使用するPodのマニフェストを確認します。  
  ```
  cat pod-configmap.yaml
  ```

* ConfigMapを使用するPodを作成します。
  ```
  k create -f  pod-configmap.yaml
  ```

* ConfigMapを使用するPodのステータスを確認します。
  ```
  k get pods
  ```

* ConfigMapを使用するPodのログを表示します。
  ```
  k logs  my-pod-configmap
  ```

* ConfigMapを使用するPodを削除します。
  ```
  k delete -f pod-configmap.yaml
  ```

---

## Secretの操作

* Secretのマニフェストを確認します。  
  ```
  cat secret.yaml
  ```

* Secretを作成します。
  ```
  k create -f secret.yaml
  ```

* Secretをステータスを確認します。
  ```
  k get secrets
  ```

* Secretの詳細を表示します。
  ```
  k describe secret my-secret
  ```

* Secretを使用するPodのマニフェストを確認します。  
  ```
  cat pod-secret.yaml
  ```

* Secretを使用するPodを作成します。
  ```
  k create -f  pod-secret.yaml
  ```

* Secretを使用するPodのステータスを確認します。
  ```
  k get pods
  ```

* Secretを使用するPodのログを表示します。
  ```
  k logs  my-pod-secret
  ```

* Secretを使用するPodを削除します。
  ```
  k delete -f pod-secret.yaml
  ```
---

## Namespaceの操作

* Namespaceのマニフェストを確認します。  
  ```
  cat secret.yaml
  ```

* Namespaceを作成します。
  ```
  k create -f secret.yaml
  ```

* Namespaceをステータスを確認します。
  ```
  k get secrets
  ```
* Namespaceを指定しているPodのマニフェストを確認します。
  ```
  cat pod-nginx.yaml
  ```

* Namespaceを指定しているPodを作成します。
  ```
  k create -f pod-nginx.yaml
  ```
* Namespaceを**指定せず** Podのステータスを確認します。
  ```  
  k get pods
  ```
* Namespaceを指定して Podのステータスを確認します。
  ```
  k get pods -n dev
  ```

* Namespaceを指定しているPodを削除します。
  ```
  k delete -f pod-nginx.yaml 
  ```

---

## Deploymentの操作

* Deploymentのマニフェストを確認します。  
  ```
  cat deployment.yaml
  ```

* Deploymentを作成します。 
  ```
  k create -f deployment.yaml
  ```

* Deploymentのステータスを確認します。
  ```
  k get deployments
  ```

* Podのステータスを確認します。
  ```
  k get pods
  ```

* Deploymentのレプリカ数を3に変更します。
  ```
  k scale deployment my-deployment --replicas=3
  ```

* Deploymentのステータスを確認します。
  ```
  k get deployments
  ```

* Podのステータスを確認します。
  ```
  k get pods
  ```

* Deploymentのレプリカ数を2に変更します。 
  ```
  k scale deployment my-deployment --replicas=2
  ```

* Deploymentのステータスを確認します。
  ```
  k get deployments
  ```

* Podのステータスを確認します。
  ```
  k get pods
  ```

* Deploymentを削除します。
  ```
  k delete -f deployment.yaml
  ```

* Deploymentのステータスを確認します。
  ```
  k get deployments
  ```

* Podのステータスを確認します。
  ```
  k get pods
  ```  

---

## Serviceの操作

* Deploymentを作成します。
  ```
  k create -f deployment.yaml
  ```

* Podのステータスを確認します。
  ```
  k get pods
  ```

* Serviceのマニフェストを確認します。  
  ```
  cat service.yaml
  ```

* Serviceを作成します。
  ```
  k create -f service.yaml
  ```

* Serviceのステータスを確認します。
  ```
  k get services
  k get services -o wide
  ```

* Public IPを取得してメモします。
  ```
  curl http://169.254.169.254/latest/meta-data/public-ipv4
  ```
* curl コマンドを使用してServiceにアクセスします。
  ```
  curl (Public IP):30000
  ```

* 次のようなHTMLが出力されることを確認します。
  ```
  <html><body><h1>It works!</h1></body></html>
  ```

* Serviceを削除します。
  ```
  k delete -f service.yaml
  ```

* Deploymentを削除します。
  ```
  k delete -f deployment.yamlexit
  ```

---

## ワークの修了

* Minikube を停止します。
  ```
  minikube stop
  ```

  
