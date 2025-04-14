# モジュール3 のサンプル


### マネジメントコンソールや AWS CLIでクラスターを作成時に必要なIAMロール
* IAMロールに設定する許可ポリシー
  -  `AmazonEKSClusterPolicy`
* IAMロールに設定する信頼ポリシー: trust-eks.json

---

### マネジメントコンソールや AWS CLIでマネージドノードグループを作成時に必要なIAMロール
* IAMロールに設定する許可ポリシー: 
  - `AmazonEKSWorkerNodePolicy`
  - `AmazonEC2ContainerRegistryReadOnly`
  - `AmazonEKS_CNI_Policy`
* IAMロールに設定する信頼ポリシー: trust-ec2.json
---
### マネジメントコンソールや AWS CLIでFargateプロファイルを作成時に必要なIAMロール
* IAMロールに設定する許可ポリシー:
  - `AmazonEKSFargatePodExecutionRolePolicy`
* IAMロールに設定する信頼ポリシー: trust-eks-fargate-pod.json

---
### eksctlによるクラスター作成のサンプル 

* VPCやサブネットも作成
* マネージドノードグループも作成
  - マネージドノードグループはPublicサブネットに作成 

```
eksctl create cluster \
--name sample-cluster \
--nodegroup-name sample-nodes \
--node-type t3.small \
--nodes 3 \
--nodes-min 1 \
--nodes-max 4 \
--managed \
--version 1.31 \
--region ap-northeast-1
```

---

### eksctlによるクラスター作成のサンプル (AZを指定）

* VPCやサブネットも作成
* AZは指定
* マネージドノードグループも作成
  - マネージドノードグループはPublicサブネットに作成 

```
AWS_REGION=ap-northeast-1
eksctl create cluster \
  --name=sample-cluster \
  --version 1.31 \
  --nodes=3 --managed \
  --region ${AWS_REGION} --zones ${AWS_REGION}a,${AWS_REGION}c
```
---

### eksctlによるクラスター作成のサンプル  (既存の VPC のサブネットを指定）

* VPCやサブネットは事前に作成しておく
* サブネットIDを指定する
* マネージドノードグループも作成
  - マネージドノードグループはPrivateサブネットに作成 

```
eksctl create cluster \
--name sample-cluster \
--vpc-public-subnets subnet-1111111,subnet-2222222  \
--vpc-private-subnets subnet-3333333,subnet-4444444 \
--nodegroup-name sample-nodes \
--node-private-networking \
--node-type t3.small \
--nodes 3 \
--nodes-min 1 \
--nodes-max 4 \
--managed \
--version 1.31 \
--region ap-northeast-1
```
---
### eksctlによるクラスター作成のサンプル (OIDC プロバイダを作成）

* VPCやサブネットは事前に作成しておく
* サブネットIDを指定する
* マネージドノードグループも作成
  - マネージドノードグループはPrivateサブネットに作成
* OIDC プロバイダも作成

```
eksctl create cluster \
--name sample-cluster \
--vpc-public-subnets subnet-1111111,subnet-2222222  \
--vpc-private-subnets subnet-3333333,subnet-4444444 \
--nodegroup-name sample-nodes \
--node-private-networking \
--node-type t3.small \
--nodes 3 \
--nodes-min 1 \
--nodes-max 4 \
--managed \
--version 1.31 \
--region ap-northeast-1 \
--with-oidc
```

---

### eksctlによるクラスター作成のサンプル (AMI タイプを指定）

* VPCやサブネットは事前に作成しておく
* サブネットIDを指定する
* マネージドノードグループも作成
  - マネージドノードグループはPrivateサブネットに作成 
  - AMI のタイプを指定 

```
eksctl create cluster \
--name sample-cluster \
--vpc-public-subnets subnet-1111111,subnet-2222222  \
--vpc-private-subnets subnet-3333333,subnet-4444444 \
--nodegroup-name sample-nodes \
--node-private-networking \
--node-type t3.small \
--nodes 3 \
--nodes-min 1 \
--nodes-max 4 \
--node-ami-family=Bottlerocket \
--managed \
--version 1.31 \
--region ap-northeast-1
```

---

### eksctlによるクラスター作成のサンプル (Auto Mode クラスター作成)

* Auto Mode を使用するクラスターの作成
* VPCやサブネットも作成

```
eksctl create cluster \
--name=sample-cluster \
--enable-auto-mode     \
--version 1.31         \
--region ap-northeast-1
```

### eksctlによるクラスター作成のサンプル (既存の VPC のサブネットを指定して Auto Mode クラスター作成)

```
eksctl create cluster \
--name sample-cluster \
--vpc-public-subnets subnet-1111111,subnet-2222222  \
--vpc-private-subnets subnet-3333333,subnet-4444444 \
--version 1.31 \
--enable-auto-mode \
--region ap-northeast-1
```

---

### eksctlによるクラスター作成のサンプル (Fargate プロファイルのみを使用するクラスタ）

* Fargateプロファイルを使用するクラスターの作成
* VPCやサブネットも作成
* この例では、FargateプロファイルのNamespaceとして次のものが適用される
  - `kube-system` と `default` 

```
eksctl create cluster \
--name sample-cluster \
--version 1.31 \
--region ap-northeast-1 \
--fargate
```
---

### eksctlによるFargateプロファイルの作成のサンプル 

* 既存のクラスター(例ではmy-cluster)にFargateプロファイルを追加作成する
  - EKS クラスターの VPC に Private Subnet が必要
* この例では、FargateプロファイルのNamespaceに `prod` 、ラベルに `blue` を指定。

```
eksctl create fargateprofile \
    --cluster my-cluster \
    --name my-fargate-profile \
    --namespace prod \
    --labels stack=blue
```

---

### eksctlによるクラスター作成のサンプル (構成ファイルを使用)

* 構成ファイルを使用したクラスター作成
  - 下記のように `--dry-run` オプションを使用して構成ファイルのテンプレートを生成可能
    - `eksctl create cluster --name temp-cluster  --dry-run`
  - 構成ファイルの例
    - clusterconfig-public.yaml
      - マネージドノードグループをPublicサブネットに配置
    - clusterconfig-private.yaml
      - マネージドノードグループをPrivateサブネットに配置

```
eksctl create cluster -f  clusterconfig-public.yaml
```

---
