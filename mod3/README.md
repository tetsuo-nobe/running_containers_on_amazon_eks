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
### eksctlによるクラスター作成のサンプル 1

* VPCやサブネットも作成
* マネージドノードグループも作成
  - マネージドノードグループはPublicサブネットに作成 
* ラボ1で使用するものと同等

```
eksctl create cluster \
--name sample1-cluster \
--nodegroup-name sample1-nodes \
--node-type t3.small \
--nodes 3 \
--nodes-min 1 \
--nodes-max 4 \
--managed \
--version 1.31 \
--region ap-northeast-1
```

---

### eksctlによるクラスター作成のサンプル 2

* VPCやサブネットも作成
* AZは指定
* マネージドノードグループも作成
  - マネージドノードグループはPublicサブネットに作成 

```
AWS_REGION=ap-northeast-1
eksctl create cluster \
  --name=sample2-cluster \
  --version 1.31 \
  --nodes=3 --managed \
  --region ${AWS_REGION} --zones ${AWS_REGION}a,${AWS_REGION}c
```
---

### eksctlによるクラスター作成のサンプル 3

* VPCやサブネットは事前に作成しておく
* サブネットIDを指定する
* マネージドノードグループも作成
  - マネージドノードグループはPrivateサブネットに作成 

```
eksctl create cluster \
--name sample3-cluster \
--vpc-public-subnets subnet-1111111,subnet-2222222  \
--vpc-private-subnets subnet-3333333,subnet-4444444 \
--nodegroup-name sample3-nodes \
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

### eksctlによるクラスター作成のサンプル 4

* VPCやサブネットは事前に作成しておく
* サブネットIDを指定する
* マネージドノードグループも作成
  - マネージドノードグループはPrivateサブネットに作成 
  - AMI のタイプを指定 

```
eksctl create cluster \
--name sample4-cluster \
--vpc-public-subnets subnet-1111111,subnet-2222222  \
--vpc-private-subnets subnet-3333333,subnet-4444444 \
--nodegroup-name sample4-nodes \
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

### eksctlによるクラスター作成のサンプル 5

* Auto Mode を使用するクラスターの作成
* VPCやサブネットも作成

```
eksctl create cluster \
--name=sample5-cluster \
--enable-auto-mode     \
--version 1.31         \
--region ap-northeast-1
```

---

### eksctlによるクラスター作成のサンプル 6

* Fargateプロファイルを使用するクラスターの作成
* VPCやサブネットも作成
* この例では、FargateプロファイルのNamespaceとして次のものが適用される
  - `kube-system` と `default` 

```
eksctl create cluster \
--name sample6-cluster \
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

### eksctlによるクラスター作成のサンプル 6

* 構成ファイルを使用したクラスター作成
  - 下記のように `--dry-run` オプションを使用して構成ファイルのテンプレートを生成可能
    - `eksctl create cluster --name temp-cluster  --dry-run`
  - 構成ファイルの例
    - clusterconfig_public.yaml
      - マネージドノードグループをPublicサブネットに配置
    - clusterconfig_private.yaml
      - マネージドノードグループをPrivateサブネットに配置

```
eksctl create cluster -f  clusterconfig-public.yaml
```

---
