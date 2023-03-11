# kubectl を使用して kubernetes のリソースを操作してみよう
* マニフェストの内容や、実行結果を確認しながら進めてみましょう。

## 環境への接続について

* 講師よりガイドいたします。
* **このワーク環境は、ワーク実施時だけの一時的な環境になります。**

## Minikube のインストール
1. ユーザーのホームディレクトリに移動し、Dockerがインストールされていることを確認します。
   ```
   cd
   pwd
   docker -v
   ```
1. Minikube をインストールします。
   ```
   curl -LO https://github.com/kubernetes/minikube/releases/download/v1.25.2/minikube-linux-amd64
   sudo install minikube-linux-amd64 /usr/local/bin/minikube
   sudo yum install -y conntrack
   ```

## Minikube の起動

1. Minikube を起動してステータスを確認します。 
   ```
   minikube start --vm-driver=none
   minikube status
   ```
1. シンボリックリンクで kubectl を使えるようにします。
   - 参考: [minikube の handbook の kubectl](https://minikube.sigs.k8s.io/docs/handbook/kubectl/)
   ```
   sudo ln -s $(which minikube) /usr/local/bin/kubectl
   ```

1. kubectl を使用できることを確認します。
   ```
   kubectl version --short --client
   ```
   
## ワーク用リポジトリの取得

1. ワーク用リポジトリをクローンして移動します。
   ```
   git clone https://github.com/tetsuo-nobe/running_containers_on_amazon_eks.git
   cd running_containers_on_amazon_eks/mod1
   ```

---

## Pod の操作

1. Podのマニフェストを確認します。
   ```
   cat pod-httpd.yaml
   ```
1. Podを作成します。
   ```
   kubectl apply -f pod-httpd.yaml
   ```
1. Podのステータスを確認します。( STATUS が Running になるまで繰り返し実行して下さい。)
   ```
   kubectl get pods
   kubectl get pods -o wide
   ```
1. Podの詳細を表示します。
   ```
   kubectl describe pods my-httpd-pod
   ```
1. Podのコンテナに接続します。
   ```
   kubectl exec -it my-httpd-pod -- /bin/bash
   ```
1. 現在のindex.htmlの内容を表示した後、exit します。
   ```
   ls
   cd htdocs
   more index.html
   exit
1. Podを削除します。
   ```
   kubectl delete -f pod-httpd.yaml
   ``` 
1. Podの削除を確認します。
   ```
   kubectl get pods
   ``` 
---

## ConfigMapの操作

1. alias を使って、キータイプ量を減らすようにします。
   - キータイプの効率を考慮し、以降は k で統一します。

   ```
   alias k=kubectl
   ```

1. ConfigMapのマニフェストを確認します。  
   ```
   cat configmap.yaml
   ```

1. ConfigMapを作成します。
   ```
   k apply -f configmap.yaml
   ```

1. ConfigMapをステータスを確認します。
   ```
   k get configmaps
   ```

1. ConfigMapの詳細を表示します。
   ```
   k describe configmap my-configmap
   ```

1. ConfigMapを使用するPodのマニフェストを確認します。  
   ```
   cat pod-configmap.yaml
   ```

1. ConfigMapを使用するPodを作成します。
   ```
   k apply -f  pod-configmap.yaml
   ```

1. ConfigMapを使用するPodのステータスを確認します。
   ```
   k get pods
   ```

1. ConfigMapを使用するPodのログを表示します。
   ```
   k logs  my-pod-configmap
   ```

1. ConfigMapを使用するPodを削除します。
   ```
   k delete -f pod-configmap.yaml
   ```

---

## Secretの操作

1. Secretのマニフェストを確認します。  
   ```
   cat secret.yaml
   ```

1. Secretを作成します。
   ```
   k apply -f secret.yaml
   ```

1. Secretをステータスを確認します。
   ```
   k get secrets
   ```

1. Secretの詳細を表示します。
   ```
   k describe secret my-secret
   ```

1. Secretを使用するPodのマニフェストを確認します。  
   ```
   cat pod-secret.yaml
   ```

1. Secretを使用するPodを作成します。
   ```
   k apply -f  pod-secret.yaml
   ```

1. Secretを使用するPodのステータスを確認します。
   ```
   k get pods
   ```

1. Secretを使用するPodのログを表示します。
   ```
   k logs  my-pod-secret
   ```

1. Secretを使用するPodを削除します。
   ```
   k delete -f pod-secret.yaml
   ```
---

## Namespaceの操作

1. Namespaceのマニフェストを確認します。  
   ```
   cat namespace.yaml
   ```

1. Namespaceを作成します。
   ```
   k apply -f namespace.yaml
   ```

1. Namespaceをステータスを確認します。
   ```
   k get namespaces
   ```
1. Namespaceを指定しているPodのマニフェストを確認します。
   ```
   cat pod-nginx.yaml
   ```

1. Namespaceを指定しているPodを作成します。
   ```
   k apply -f pod-nginx.yaml
   ```
1. Namespaceを**指定せず** Podのステータスを確認します。
   ```  
   k get pods
   ```
1. Namespaceを指定して Podのステータスを確認します。
   ```
   k get pods -n dev
   ```

1. Namespaceを指定しているPodを削除します。
   ```
   k delete -f pod-nginx.yaml 
   ```
---

## Deploymentの操作

1. Deploymentのマニフェストを確認します。  
   ```
   cat deployment.yaml
   ```

1. Deploymentを作成します。 
   ```
   k apply -f deployment.yaml
   ```

1. Deploymentのステータスを確認します。
   ```
   k get deployments
   ```

1. ReplicaSetのステータスを確認します。
   ```
   k get replicasets
   ```

1. Podのステータスを確認します。
   ```
   k get pods
   ```

1. Deploymentのレプリカ数を3に変更します。
   - (ここでは kubectl scale コマンドを使用していますが、vim を使用できる人はマニフェストで replicas の値を変更して kubectl apply を使用しても OKです。)
   ```
   k scale deployment my-deployment --replicas=3
   ```

1. Deploymentのステータスを確認します。
   ```
   k get deployments
   ```

1. ReplicaSetのステータスを確認します。
   ```
   k get replicasets
   ```

1. Podのステータスを確認します。
   ```
   k get pods
   ```

1. Deploymentのレプリカ数を2に変更します。 
   - (ここでは kubectl scale コマンドを使用していますが、vim を使用できる人はマニフェストで replicas の値を変更して kubectl apply を使用しても OKです。)
   ```
   k scale deployment my-deployment --replicas=2
   ```

1. Deploymentのステータスを確認します。
   ```
   k get deployments
   ```

1. ReplicaSetのステータスを確認します。
   ```
   k get replicasets
   ```

1. Podのステータスを確認します。
   ```
   k get pods
   ```

1. Deploymentを削除します。
   ```
   k delete -f deployment.yaml
   ```

1. Deploymentのステータスを確認します。
   ```
   k get deployments
   ```

1. Podのステータスを確認します。
   ```
   k get pods
   ```  

---

## Serviceの操作

1. Deploymentを作成します。
   ```
   k apply -f deployment.yaml
   ```

1. Podのステータスを確認します。
   ```
   k get pods
   ```

1. Serviceのマニフェストを確認します。  
   ```
   cat service.yaml
   ```

1. Serviceを作成します。
   ```
   k apply -f service.yaml
   ```

1. Serviceのステータスを確認します。
   ```
   k get services
   k get services -o wide
   ```

1. Public IPを取得してメモします。
   ```
   curl http://169.254.169.254/latest/meta-data/public-ipv4
   ```
1. curl コマンドを使用してServiceにアクセスします。
   ```
   curl (Public IP):30000
   ```

1. 次のようなHTMLが出力されることを確認します。
   ```
   <html><body><h1>It works!</h1></body></html>
   ```

1. Serviceを削除します。
   ```
   k delete -f service.yaml
   ```

1. Deploymentを削除します。
   ```
   k delete -f deployment.yaml
   ```

---

## Kubernetes のリソース名やその短縮名を確認

1. 次のコマンドを実行して確認します。
   ```
   k api-resources
   ```

---

## (時間に余裕があれば実施して下さい）Deploymentの更新の操作
- このタスクはとばして、[ワークの終了](#ワークの終了) 操作を実施しても OK です！


1. Deploymentのマニフェスト (image が nginx:1.22.0) を確認します。  
   ```
   cat deployment-nginx1.22.yaml
   ```

1. Deploymentのマニフェスト (image が nginx:1.23.0) を確認します。  
   ```
   cat deployment-nginx1.23.yaml
   ```

1. Deployment (image が nginx:1.22.0) を作成します。 
   ```
   k apply -f deployment-nginx1.22.yaml
   ```

1. Deploymentのステータスを確認します。
   ```
   k get deployments -o wide
   ```

1. Podのステータスを確認します。
   ```
   k get pods
   ```

1. Deployment の image を nginx:1.23.0 に更新します。 
   ```
   k apply -f deployment-nginx1.23.yaml
   ```

1. Podのステータスを確認します。
   ```
   k get pods
   ```

1. Deployment 変更履歴を表示します。 
   ```
   k rollout history deployment nginx-deployment
   ```

1. Deployment の image を nginx:1.22.0 にロールバックします。 
   ```
   k rollout undo deployment nginx-deployment  --to-revision 1
   ```

1. Podのステータスを確認します。
   ```
   k get pods
   ```

1. Deploymentの変更履歴を表示します。 
   ```
   k rollout history deployment nginx-deployment
   ```

1. Deploymentを削除します。 
   ```
   k delete -f deployment-nginx1.23.yaml
   ```

## (時間に余裕があれば実施して下さい）Job と CronJob の操作
- このタスクはとばして、[ワークの終了](#ワークの終了) 操作を実施しても OK です！

1. Jobのマニフェストを確認します。
   ```
   cat job.yaml
   ```
1. Jobを作成します。
   ```
   kubectl apply -f job.yaml
   ```
1. Jobにより実行されたPodのステータスを確認します。( STATUS が Completed になるまで繰り返し実行して下さい。)
   ```
   kubectl get pods
   ```
1. `kubectl get pods` で表示された Pod の名前をコピーして下記を実行し、Jobの実行結果を確認します。
   ```
   kubectl logs <コピーした Pod名>
   ```
1. Jobを削除します。
   ```
   kubectl delete -f job.yaml
   ``` 
1. CronJobのマニフェストを確認します。
   ```
   cat cronjob.yaml
   ```
1. CronJobを作成します。
   ```
   kubectl apply -f cronjob.yaml
   ```
1. CronJobにより実行されたPodのステータスを確認します。( 2～3分の間に数回実行してCompletedになったPodが増えることを確認します。)
   ```
   kubectl get pods
   ```
1. `kubectl get pods` で表示された Pod のうち、1つのPodの名前をコピーして下記を実行し、CronJobによるJob実行結果を確認します。
   ```
   kubectl logs <コピーした Pod名>
   ```
1. CronJobを削除します。
   ```
   kubectl delete -f cronjob.yaml
   ``` 
---

## ワークの終了

1. Minikube を停止します。
   ```
   minikube stop
   ```
1. 環境への接続を終了します。
   ```
   exit
   ```
* お疲れ様でした！
* **このワーク環境は、ワーク実施時だけの一時的な環境になります。**
