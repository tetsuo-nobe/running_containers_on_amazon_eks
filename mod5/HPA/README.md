# HPA (Horizontal Pod Autoscaler) の設定とデモ

* HPA (Horizontal Pod Autoscaler) 設定手順
  - https://docs.aws.amazon.com/ja_jp/eks/latest/userguide/horizontal-pod-autoscaler.html
  - https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/
```
HPA は、Kubernetes の標準 API リソースであり、動作するには、メトリクスソース (Kubernetes メトリクスサーバーなど) が Amazon EKS クラスターにインストールされている必要があります。アプリケーションのスケーリングを開始するために、クラスターに Horizontal Pod Autoscaler をデプロイまたはインストールする必要はありません。
```

* メトリクスサーバーのインストール(kube-system ネームスペース）
  - https://docs.aws.amazon.com/ja_jp/eks/latest/userguide/metrics-server.html

```
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
kubectl get deployment metrics-server -n kube-system
```

* HPA を試すサンプルアプリの実行
```
kubectl apply -f https://k8s.io/examples/application/php-apache.yaml
```

* HPA リソースの設定
```
kubectl autoscale deployment php-apache --cpu-percent=50 --min=1 --max=10
```

* HPA の状態取得
```
kubectl get hpa php-apache
```

* 負荷をかける（停止時は Ctrl + c)
```
kubectl run -i \
    --tty load-generator \
    --rm --image=busybox \
    --restart=Never \
    -- /bin/sh -c "while sleep 0.01; do wget -q -O- http://php-apache; done"
```

* 別のターミナルで HPA の状態取得
```
kubectl get hpa php-apache
```

* サンプルアプリケーションの削除
```
kubectl delete deployment.apps/php-apache service/php-apache horizontalpodautoscaler.autoscaling/php-apache
```
