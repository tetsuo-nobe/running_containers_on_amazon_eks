# kubectl を使用して kubernetes のリソースを操作してみよう
* マニフェストの内容や、実行結果を確認しながら進めてみましょう。
* 参考: [Kubernetes ドキュメント](https://kubernetes.io/ja/docs/home/)

## 環境への接続について

* 講師よりガイドいたします。
* **このワーク環境は、ワーク実施時だけの一時的な環境になります。**

## Minikube のインストール
1. ユーザーのホームディレクトリに移動し、Docker がインストールされていることを確認します。
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

1. Pod のマニフェストを確認します。
   - **Pod で指定しているコンテナイメージ httpd は Apache HTTP Server のコンテナイメージです。**
   ```
   cat pod-httpd.yaml
   ```
1. Pod を作成します。
   ```
   kubectl apply -f pod-httpd.yaml
   ```
1. Pod のステータスを確認します。( STATUS が Running になるまで繰り返し実行して下さい。) 
   ```
   kubectl get pods
   kubectl get pods -o wide
   ```
1. Pod の詳細を表示します。
   ```
   kubectl describe pods my-httpd-pod
   ```
1. Pod のコンテナに接続します。`--` の後の引数はコマンドです。
   ```
   kubectl exec -it my-httpd-pod -- /bin/bash
   ```
1. 次のコマンドを実行し、index.html の内容を表示します。
   ```
   cd htdocs
   ```

   ```
   cat index.html
   ```
   
1. Pod のコンテナから exit します。
   ```
   exit
   ```
   
1. Pod を削除します。
   ```
   kubectl delete -f pod-httpd.yaml
   ``` 
1. Pod の削除を確認します。
   ```
   kubectl get pods
   ``` 
---

## ConfigMap の操作

1. alias を使って、キータイプ量を減らすようにします。
   - キータイプの効率を考慮し、以降は k で統一します。

   ```
   alias k=kubectl
   ```

1. ConfigMap のマニフェストを確認します。  
   ```
   cat configmap.yaml
   ```

1. ConfigMap を作成します。
   ```
   k apply -f configmap.yaml
   ```

1. ConfigMap をステータスを確認します。
   ```
   k get configmaps
   ```

1. ConfigMap の詳細を表示します。
   ```
   k describe configmap my-configmap
   ```

1. ConfigMap を使用する Pod のマニフェストを確認します。  
   - **Pod で指定しているコンテナイメージ busybox は Linux コマンドを実行したいときに活用できるコンテナイメージです。**
   - **Pod から Ref や xxx を使用して ConfigMap の値を環境変数として取り込んでいます。**　
   - **Pod は Linux の env コマンドを発行して環境変数を出力しています。**
   ```
   cat pod-configmap.yaml
   ```

1. ConfigMap を使用する Pod を作成します。
   ```
   k apply -f  pod-configmap.yaml
   ```

1. ConfigMap を使用する Pod のステータスを確認します。
   ```
   k get pods
   ```

1. ConfigMap を使用する Pod のログを表示します。
   - **ConfigMap の値が出力されていることを確認しましょう**
   ```
   k logs  my-pod-configmap
   ```
1. ConfigMap を使用する Pod を削除します。
   ```
   k delete -f pod-configmap.yaml
   ```

---

## Secret の操作

1. Secret のマニフェストを確認します。  
   ```
   cat secret.yaml
   ```

1. Secret を作成します。
   ```
   k apply -f secret.yaml
   ```

1. Secret をステータスを確認します。
   ```
   k get secrets
   ```

1. Secret の詳細を表示します。
   - **Secret の値は参照できるでしょうか？**　
   ```
   k describe secret my-secret
   ```

1. Secret を使用する Pod のマニフェストを確認します。  
   ```
   cat pod-secret.yaml
   ```

1. Secret を使用する Pod を作成します。
   ```
   k apply -f  pod-secret.yaml
   ```

1. Secret を使用する Pod のステータスを確認します。
   ```
   k get pods
   ```

1. Secret を使用する Pod のログを表示します。
   ```
   k logs  my-pod-secret
   ```

1. Secret を使用する Pod を削除します。
   ```
   k delete -f pod-secret.yaml
   ```
---

## Namespace の操作

1. Namespace のマニフェストを確認します。  
   ```
   cat namespace.yaml
   ```

1. Namespace を作成します。
   ```
   k apply -f namespace.yaml
   ```

1. Namespace をステータスを確認します。
   ```
   k get namespaces
   ```
1. Namespace を指定している Pod のマニフェストを確認します。
   ```
   cat pod-nginx.yaml
   ```

1. Namespace を指定している Pod を作成します。
   ```
   k apply -f pod-nginx.yaml
   ```
1. Namespace を**指定せず** Pod のステータスを確認します。
   - **Pod の情報は表示されましたか？**
   ```  
   k get pods
   ```
1. Namespace を指定して Pod のステータスを確認します。
   - **Pod の情報は表示されましたか？**
   ```
   k get pods -n dev
   ```

1. Namespace を指定している Pod を削除します。
   ```
   k delete -f pod-nginx.yaml 
   ```
---

## Deployment の操作

1. Deployment のマニフェストを確認します。  
   - **作成する Pod のスペックはどこに記載されていますか？**
   - **作成する Pod の数はどこに記載されていますか？**
   ```
   cat deployment.yaml
   ```

1. Deployment を作成します。 
   ```
   k apply -f deployment.yaml
   ```

1. Deployment のステータスを確認します。
   ```
   k get deployments
   ```

1. ReplicaSet のステータスを確認します。
   ```
   k get replicasets
   ```

1. Pod のステータスを確認します。
   ```
   k get pods
   ```

1. Deployment のレプリカ数を 3 に変更します。
   - (ここでは kubectl scale コマンドを使用していますが、vim を使用できる人はマニフェストで replicas の値を変更して kubectl apply を使用しても OKです。)
   ```
   k scale deployment my-deployment --replicas=3
   ```

1. Deployment のステータスを確認します。
   ```
   k get deployments
   ```

1. ReplicaSet のステータスを確認します。
   ```
   k get replicasets
   ```

1. Pod のステータスを確認します。
   ```
   k get pods
   ```

1. Deployment のレプリカ数を2に変更します。 
   - (ここでは kubectl scale コマンドを使用していますが、vim を使用できる人はマニフェストで replicas の値を変更して kubectl apply を使用しても OKです。)
   ```
   k scale deployment my-deployment --replicas=2
   ```

1. Deployment のステータスを確認します。
   ```
   k get deployments
   ```

1. ReplicaSet のステータスを確認します。
   ```
   k get replicasets
   ```

1. Pod のステータスを確認します。
   ```
   k get pods
   ```

1. Deployment を削除します。
   ```
   k delete -f deployment.yaml
   ```

1. Deployment のステータスを確認します。
   ```
   k get deployments
   ```

1. Pod のステータスを確認します。
   ```
   k get pods
   ```  

---

## Service の操作

1. Deployment を作成します。
   ```
   k apply -f deployment.yaml
   ```

1. Pod のステータスを確認します。
   ```
   k get pods
   ```

1. Service のマニフェストを確認します。  
   - **作成する Service の Type は何ですか？**
   ```
   cat service.yaml
   ```

1. Service を作成します。
   ```
   k apply -f service.yaml
   ```

1. Service のステータスを確認します。
   ```
   k get services
   k get services -o wide
   ```

1. Public IP を取得してメモします。
   ```
   curl http://169.254.169.254/latest/meta-data/public-ipv4
   ```
1. curl コマンドを使用して Service にアクセスします。
   ```
   curl (Public IP):30000
   ```

1. 次のような HTML が出力されることを確認します。
   - **Pod に対して curl コマンドからアクセスできることを確認しましょう**
   ```
   <html><body><h1>It works!</h1></body></html>
   ```

1. Service を削除します。
   ```
   k delete -f service.yaml
   ```

1. Deployment を削除します。
   ```
   k delete -f deployment.yaml
   ```

---

## Kubernetes のリソース名やその短縮名を確認

1. 次のコマンドを実行して確認します。
   ```
   k api-resources
   ```
1. 短縮名を使って情報を表示してみましょう。
   ```
   k apply -f deployment.yaml
   k apply -f service.yaml
   k get deploy
   k get svc
   k get po
   ```
1. 確認後できたら削除します。
   ```
   k delete -f deployment.yaml
   k delete -f service.yaml
   ```
---

## (時間に余裕があれば実施して下さい）Deployment の更新の操作
- このタスクはとばして、[ワークの終了](#ワークの終了) 操作を実施しても OK です！


1. Deployment のマニフェスト (image が nginx:1.22.0) を確認します。  
   ```
   cat deployment-nginx1.22.yaml
   ```

1. Deployment のマニフェスト (image が nginx:1.23.0) を確認します。  
   ```
   cat deployment-nginx1.23.yaml
   ```

1. Deployment (image が nginx:1.22.0) を作成します。 
   ```
   k apply -f deployment-nginx1.22.yaml
   ```

1. Deployment のステータスを確認します。
   ```
   k get deployments -o wide
   ```

1. Pod のステータスを確認します。
   ```
   k get pods
   ```

1. Deployment の image を nginx:1.23.0 に更新します。 
   ```
   k apply -f deployment-nginx1.23.yaml
   ```

1. Pod のステータスを確認します。
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

1. Pod のステータスを確認します。
   ```
   k get pods
   ```

1. Deployment の変更履歴を表示します。 
   ```
   k rollout history deployment nginx-deployment
   ```

1. Deployment を削除します。 
   ```
   k delete -f deployment-nginx1.23.yaml
   ```

## (時間に余裕があれば実施して下さい）Job と CronJob の操作
- このタスクはとばして、[ワークの終了](#ワークの終了) 操作を実施しても OK です！

1. Job のマニフェストを確認します。
   ```
   cat job.yaml
   ```
1. Job を作成します。
   ```
   kubectl apply -f job.yaml
   ```
1. Job により実行されたPodのステータスを確認します。( STATUS が Completed になるまで繰り返し実行して下さい。)
   ```
   kubectl get pods
   ```
1. `kubectl get pods` で表示された Pod の名前をコピーして下記を実行し、Jobの実行結果を確認します。
   ```
   kubectl logs <コピーした Pod 名>
   ```
1. Job を削除します。
   ```
   kubectl delete -f job.yaml
   ``` 
1. CronJob のマニフェストを確認します。(Hello from cronjob というメッセージを表示する Job を 1 分毎に実行します。）
   ```
   cat cronjob.yaml
   ```
1. CronJob を作成します。
   ```
   kubectl apply -f cronjob.yaml
   ```
1. CronJob により実行された Pod のステータスを確認します。( 2～3 分の間に数回実行して Completed になった Pod が増えることを確認します。)
   ```
   kubectl get pods
   ```
1. `kubectl get pods` で表示された Pod のうち、1 つの Pod の名前をコピーして下記を実行し、CronJob による Job 実行結果を確認します。
   ```
   kubectl logs <コピーした Pod名>
   ```
1. CronJob を削除します。
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
