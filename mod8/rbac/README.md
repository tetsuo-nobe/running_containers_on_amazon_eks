# IAM ユーザーを作成して EKS クラスターで管理できる権限を与える

* 前提
  - 対象のEKS クラスター名は demo-cluster 
  - rbac-lookup コマンドをインストールしている

## IAM ユーザーの新規作成

* アクセスキーIDとシークレットアクセスキーを発行
* 下記のポリシーを許可
  ```
  {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "eks:DescribeCluster",
            "Resource": "arn:aws:eks:ap-northeast-1:000000000000:cluster/demo-cluster"
        }
    ]
  }
  ```
  * IAMユーザー作成後、ARNをコピーしておく

## IAMユーザーとRBACグループのマップを定義しているConfigMapを確認

* aws-auth の ConfigMap を確認
  ```
  kubectl describe configmap aws-auth -n kube-system
  ```
* 新規で作成された IAM ユーザーはまだマップされていない。

## aws-auth ConfigMapに新規IAMユーザーのマップを追加
   ```
   eksctl create iamidentitymapping --cluster demo-cluster --arn <作成したIAMユーザーのARN> --group system:masters --username demo-iam-user
   ```

## 再度、IAMユーザーとRBACグループのマップを定義しているConfigMapを確認
* aws-auth の ConfigMap を確認
  ```
  kubectl describe configmap aws-auth -n kube-system
  ```
* 新規で作成された IAM ユーザーがマップされていることを確認。

---

## 作成されたIAM ユーザーが自分のマシンから EKS クラスターに接続する

* kubectl や AWS CLI は利用可能なマシンである前提

* （デモの便宜上、環境変数を使ってユーザーを切り替えたことにする）
  ```
  export AWS_ACCESS_KEY_ID=xxxxxxxxxxxxxxxxx
  export AWS_SECRET_ACCESS_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxx
  aws sts get-caller-identity
  ```
* この段階では、まだEKSクラスタに接続できない
  ``` 
  kubectl get all
  ```
* EKSクラスタに接続するためのクライアント側の構成を実行
  ```
  aws eks --region ap-northeast-1 update-kubeconfig --name demo-cluster
  ```
* 構成内容を確認
  ```
  kubectl config get-contexts
  ```
* 構成ファイルを確認
  ```
  ls -la  ~/.kube
  cat ~/.kube/config
  ```
* EKSクラスタに接続できることを確認
   ```
   kubectl get all
   ```
