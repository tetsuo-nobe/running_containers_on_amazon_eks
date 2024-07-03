# HPA (Horizontal Pod Autoscaler) の設定とデモの手順

* HPA (Horizontal Pod Autoscaler) 設定手順
  - https://docs.aws.amazon.com/ja_jp/eks/latest/userguide/horizontal-pod-autoscaler.html
  - https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/
```
HPA は、Kubernetes の標準 API リソースであり、
動作するには、メトリクスソース (Kubernetes メトリクスサーバーなど) が 
Amazon EKS クラスターにインストールされている必要があります。
アプリケーションのスケーリングを開始するために、
クラスターに Horizontal Pod Autoscaler をデプロイまたはインストールする必要はありません。
```

1. メトリクスサーバーのインストール(kube-system ネームスペース）
  - https://docs.aws.amazon.com/ja_jp/eks/latest/userguide/metrics-server.html

```
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
kubectl get deployment metrics-server -n kube-system
```

2. HPA を試すサンプルアプリの実行
```
kubectl apply -f https://k8s.io/examples/application/php-apache.yaml
```

3. HPA リソースの設定 (コマンドの場合)
```
kubectl autoscale --name hpa-php-apache deployment php-apache --cpu-percent=50 --min=1 --max=10
```

* [参考] マニフェストを使っての HPA リソースの設定も可能です。
    - 例：このREADME.mdと同じフォルダにあるマニフェストを使う場合は下記を実行
    ```
    kubectl apply -f hpa.yaml
    ```

4. HPA の状態取得
```
kubectl get hpa hpa-php-apache
```

5. 負荷をかけて、 OK! という文字が連続で表示されることを確認　（停止時は Ctrl + c)
```
kubectl run -i \
    --tty load-generator \
    --rm --image=busybox \
    --restart=Never \
    -- /bin/sh -c "while sleep 0.01; do wget -q -O- http://php-apache; done"
```

6. 別のターミナルを開いてください。または AWS の Session Manager を使っている場合は、もう一つ接続してください。
7. HPA の状態を確認していきます。
    - 負荷をかけると、Pod 数が増加していく
    - 負荷かけを停止すると、Pod 数は約5分後に1に戻る

```
kubectl get hpa hpa-php-apache
kubectl get deployment php-apache
```

8. OK! と表示されているセッションで Ctrl + c を押下して停止

9. HPA リソースとサンプルアプリケーションの削除
```
kubectl delete deployment.apps/php-apache service/php-apache horizontalpodautoscaler.autoscaling/hpa-php-apache
```
