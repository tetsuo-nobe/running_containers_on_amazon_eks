# Amazon EKS で AWS Distro for OpenTelemetry (ADOT) を使用して AWS X-Ray トレースを表示する

* 参考ドキュメント
    - [AWS Distro for OpenTelemetry のドキュメント](https://aws-otel.github.io/docs/introduction)
    - [クラスターのパフォーマンスをモニタリングし、ログを表示する | Amazon EKS ユーザーガイド](https://docs.aws.amazon.com/ja_jp/eks/latest/userguide/eks-observe.html)
    - [AWS Distro for OpenTelemetry を使用したアプリケーションの計測 | Amazon EKS ユーザーガイド](https://docs.aws.amazon.com/ja_jp/xray/latest/devguide/xray-instrumenting-your-app.html#xray-instrumenting-opentel)
    - [AWS Observability Best Practices](https://aws-observability.github.io/observability-best-practices/ja/guides/containers/aws-native/eks/container-tracing-with-aws-xray/)

## 構成手順

0. 事前準備
  - 下記の手順を実施
      - [Requirements for Getting Started with AWS Distro for OpenTelemetry using EKS Add-Ons](https://aws-otel.github.io/docs/getting-started/adot-eks-add-on/requirements)

1. AWS Distro for OpenTelemetry (ADOT) のアドオンをのインストール
  - 下記の手順で Amazon EKS にインストール
      - [Installation of AWS Distro for OpenTelemetry using EKS Add-Ons](https://aws-otel.github.io/docs/getting-started/adot-eks-add-on/installation)

2. Collectorの作成  (参考: [OTLP Ingest Collector Configuration](https://aws-otel.github.io/docs/getting-started/adot-eks-add-on/config-otlp-ingest))
    - 2-1: OIDC 有効化
    ```
    cluster_name=xray-cluster
    eksctl utils associate-iam-oidc-provider --cluster ${cluster_name} --approve
    ```

    - 2-2: IRSA作成
    ```
    eksctl create iamserviceaccount \
    --name adot-col-otlp-ingest \
    --cluster ${cluster_name} \
    --attach-policy-arn arn:aws:iam::aws:policy/AWSXrayWriteOnlyAccess \
    --approve 
    ```

    - 2-3: Collector 作成
        -  このフォルダにある下記のマニフェストを適用する
            - collector-config-xray.yaml : コレクターのマニフェスト
            ```
            kubectl apply -f collector-config-xray.yaml
            ```

3. サンプルアプリの実行　(参考: [Deploy a sample application to test the AWS Distro for OpenTelemetry Collector](https://aws-otel.github.io/docs/getting-started/adot-eks-add-on/sample-app))
    -  このフォルダにある下記のマニフェストを適用する
        - traffic-generator.yaml : サンプルアプリへアクセスを実行
        - sample-app.yaml : コレクターへトレースを送信するサンプルアプリ
    ```
    kubectl apply -f traffic-generator.yaml 

    kubectl apply -f sample-app.yaml 
    ```
    - OTEL_EXPORTER_OTLP_ENDPOINT の値は、コレクターのサービス名であることを確認

4. AWS マネジメントコンソールから Amazon CloudWatch のページでトレースを表示
