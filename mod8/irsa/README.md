# Pod から Amazon S3 バケットにアクセスを可能にする

* 前提
  - 対象のEKS クラスター名は demo-cluster 
  - アクセス対象のバケット名は、tnobe-eks-irsa-demo 

## EKSクラスタのOIDCプロバイダーをIAMに関連付ける
  * 下記を実行
    ```
    eksctl utils associate-iam-oidc-provider --cluster demo-cluster  --approve
    ```

## IAMロールに設定するIAMポリシーの作成

* IAM ポリシーを my-demo-bucket-fullaccess-policy.json に作成 
  ```
  {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": "arn:aws:s3:::tnobe-eks-irsa-demoexit"
        }
    ]
  }
  ```

* IAM ポリシーを作成
  ```
  aws iam create-policy \
    --policy-name my-demo-bucket-fullaccess-policy \
    --policy-document file://my-demo-bucket-fullaccess-policy.json
  ```

## IAMロールと紐づくサービスアカウントの作成

* aws-auth の ConfigMap を確認
  ```
  AWS_ACCOUNT_ID=$(aws sts get-caller-identity --output text --query Account)

  eksctl create iamserviceaccount \;q
    --name my-demo-bucket-fullaccess \
    --role-name my-demo-bucket-fullaccess-role  \
    --cluster demo-cluster \
    --attach-policy-arn arn:aws:iam::${AWS_ACCOUNT_ID}:policy/my-demo-bucket-fullaccess-policy \
    --override-existing-serviceaccounts \
    --approve
  ```

## サービスアカウントの確認
   * describe により、IAM ロールの情報も確認できる
     ```
     kubectl get serviceaccount
     kubectl describe serviceaccount my-demo-bucket-fullaccess
     ```

## サービスアカウントを設定しない Pod から S3 バケットにアクセスしてみる
* このフォルダにある pod-aws-cli.yaml を使用して Pod を作成
  ```
  kubectl apply -f pod-aws-cli.yaml
  ```
* シェルに接続
  ```
  kubectl exec -it my-aws-cli -- /bin/bash
  ```
* S3バケットにアクセスすると権限がなくエラーになることを確認
  ```
  aws s3 ls s3://tnobe-eks-irsa-demo
  ```
* IAM のサブジェクトを確認すると ノードに設定された IAM ロールであることがわかる
  ```
  aws sts get-caller-identity
  exit
  ```

## サービスアカウントを設定している Pod から S3 バケットにアクセスしてみる
* このフォルダにある pod-sa-aws-cli.yaml を使用して Pod を作成
  ```
  kubectl apply -f pod-sa-aws-cli.yaml
  ```
* シェルに接続
  ```
  kubectl exec -it my-sa-aws-cli -- /bin/bash
  ```
* S3バケットにアクセス可能であることを確認
  ```
  aws s3 ls s3://tnobe-eks-irsa-demo
  ```
* IAM のサブジェクトを確認すると サービスアカウントの IAM ロールであることがわかる
  ```
  aws sts get-caller-identity
  exit
  ```

---

## 環境のクリア
  * Pod と サービスアカウントを削除
  ```
  kubectl delete -f pod-aws-cli.yaml
  kubectl delete -f pod-sa-aws-cli.yaml
  eksctl delete iamserviceaccount dynamodb-messages-fullaccess --cluster demo-cluster
  ```
 * その他、必要に応じて IAM ポリシーなども削除
