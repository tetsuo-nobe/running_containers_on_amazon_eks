# kubectl を使用して kubernetes のオブジェクトを操作してみよう
* マニフェストの内容や、実行結果を確認しながら進めてみましょう。
* 参考: [Kubernetes ドキュメント](https://kubernetes.io/ja/docs/home/)


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
   ```
   cat pod-configmap.yaml
   ```
   - **Pod で指定しているコンテナイメージ busybox は Linux コマンドを実行したいときに活用できるコンテナイメージです。**
   - **この Pod では、`command: [ "/bin/sh", "-c", "env" ]` と指定されているので、Linux の env コマンドを実行し、環境変数を出力します。**
   - **Pod のマニフェストにある `env:` は `configMapKeyRef:` を使用して `key:` で指定した ConfigMap の値を環境変数として取り込んでいます。**
   - **Pod のマニフェストにある `envFrom:` は `configMapRef:` を使用して 全ての ConfigMap の値を環境変数として取り込んでいます。**

1. ConfigMap を使用する Pod を作成します。
   ```
   k apply -f  pod-configmap.yaml
   ```

1. ConfigMap を使用する Pod のステータスを確認します。今回は `STATUS` が `Completed` になっていることを確認します。
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

1. Namespace `dev` のマニフェストを確認します。  
   ```
   cat namespace.yaml
   ```

1. Namespace `dev` を作成します。
   ```
   k apply -f namespace.yaml
   ```

1. 各 Namespace のステータスを確認します。
   ```
   k get namespaces
   ```
1. Namespace `dev` を指定している Pod のマニフェストを確認します。
   ```
   cat pod-nginx.yaml
   ```

1. Namespace `dev` を指定している Pod を作成します。
   ```
   k apply -f pod-nginx.yaml
   ```
1. Namespace を**指定せず** Pod のステータスを確認します。
   - **Pod の情報は表示されましたか？**
   ```  
   k get pods
   ```
1. Namespace `dev` を指定して Pod のステータスを確認します。
   - **Pod の情報は表示されましたか？**
   ```
   k get pods -n dev
   ```

1. Namespace `dev` を指定している Pod を削除します。
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

1. Service のステータスを確認します。**出力から EXTERNAL-IP の値をメモしておきます。**
   ```
   k get services
   k get services -o wide
   ```

1. Webブラウザで新しいタブを開き、次のように URL を指定して It works! という文字を含んだ Web ページが表示されることを確認します。アクセス可能になるまで数分待つ必要があります。
   ```
   http://<EXTERNAL-IPの値>
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

1. 環境への接続を終了します。
   ```
   exit
   ```
* お疲れ様でした！

