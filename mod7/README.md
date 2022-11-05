# Amazon EKS で Service や Ingress を作成してみよう
* マニフェストの内容や、実行結果を確認しながら進めてみましょう。

## 環境への接続について

* 講師よりガイドいたします。

## Cloud 9 の一時認証情報の無効化
1. Cloud 9 画面の右上にある歯車アイコンをクリックします。

1. Preference の左側で AWS Settings をクリックし、右側の トグルを OFFにします。
   
1. Preference のタブを閉じます。

## 現在の IAM ロールの確認

1. Cloud 9 のターミナルで次のコマンドを実行します。 
   ```
   aws sts get-caller-identity
   ```
1. 出力された Arn に、**my-EC2-EKS-DesclibeCluster-Role** という文字が含まれていることを確認します。

   
## kubectl のインストール

1. Cloud 9 のターミナルで次のコマンドを実行します。 
   ```
   curl -o kubectl https://s3.us-west-2.amazonaws.com/amazon-eks/1.22.6/2022-03-09/bin/linux/amd64/kubectl
   sudo chmod +x ./kubectl
   mkdir -p $HOME/bin && cp ./kubectl $HOME/bin/kubectl && export PATH=$PATH:$HOME/bin
   echo 'export PATH=$PATH:$HOME/bin' >> ~/.bashrc
   kubectl version --short --client
   ```
1. 次の例のようなバージョンが表示されることを確認します。 (バージョン番号は異なっていても問題ありません。)
   ```
   Client Version: v1.22.6-eks-7d68063
   ```

## ハンズオン用の Amazon EKS クラスタへの接続設定

1. Cloud 9 のターミナルで次のコマンドを実行します。 
   ```
   aws eks --region ap-northeast-1 update-kubeconfig --name tgb-cluster
   ```
1. 次の例のようなバージョンが表示されることを確認します。 (arn の内容は異なっていても問題ありません。)
   ```
   Added new context arn:aws:eks:ap-northeast-1:123412341234:cluster/tgb-cluster to /home/ec2-user/.kube/config
   ```

1. Cloud 9 のターミナルで次のコマンドを実行します。 
   ```
   kubectl get all
   ```
1. 次のような出力が表示されることを確認します。 (下記は抜粋した例です。)
   ```
   NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   
   service/kubernetes   ClusterIP   172.20.0.1   <none>        443/TCP 
   ```

## ワーク用リポジトリの取得

1. ワーク用リポジトリをクローンして移動します。
   ```
   git clone https://github.com/tetsuo-nobe/running_containers_on_amazon_eks.git
   cd running_containers_on_amazon_eks/mod7
   ```

---

## ClusterIP タイプの Service の作成

1. Cloud9 画面左側から 下記の Service のマニフェストのファイルをダブルクリックして開きます。
   ```
   running_containers_on_amazon_eks/mod7/service/service-cluster-ip.yaml
   ```
1. マニフェストの中で **namespace の値を自分に割当てられた値に変更**してファイルを保存します。

1. Cloud 9 のターミナルで次のコマンドを実行して Service を作成します。
   ```
   kubectl apply -f service/service-cluster-ip.yaml
   ```
1. Service を表示します。-n の後には自分の Namespace を指定します。**出力から CLUSTER-IP の値をメモしておきます。**
   ```
   kubectl get service -n student99
   ```
1. Serviceにアクセスするために一時的な Pod を起動してそのコンテナに接続します。-n の後には自分の Namespace を指定します。
   ```
   k run bastion --rm -it  -n student99 --image nginx  -- /bin/bash
   ```
1. Pod から curl コマンドを使用して Service にアクセスしてみます。
   ```
   curl  10.100.235.63
   curl my-service-clusterip
   ```
1. 次のような　HTML が表示されることを確認します。
   ```
   <html>
     <title>python-web-ec2</title>
     <head></head>
     <body>
       <H1>Top Page</H1>
       <H3>Python Web App using Flask</H3>
       <H4>Host: ip-192-168-32-186.ap-northeast-1.compute.internal</H4>
       <H4>AZ: ap-northeast-1a</H4>
     </body>
   </html>
   ```
1. 確認後、Pod から exit します。
   ```
   exit
   ```
1. Service を削除します。
   ```
   kubectl delete -f service/service-cluster-ip.yaml 
   ``` 
1. Service の削除を確認します。-n の後には自分の Namespace を指定します。
   ```
   kubectl get service -n student99
   ``` 

---

## NodePort タイプの Service の作成

1. Cloud9 画面左側から 下記の Service のマニフェストのファイルをダブルクリックして開きます。
   ```
   running_containers_on_amazon_eks/mod7/service/service-nodeport.yaml
   ```
1. マニフェストの中で **namespace の値を自分に割当てられた値に変更**してファイルを保存します。

1. Cloud 9 のターミナルで次のコマンドを実行して Service を作成します。
   ```
   kubectl apply -f service/service-nodeport.yaml 
   ```
1. Service を表示します。-n の後には自分の Namespace を指定します。**出力から Node Port の値をメモしておきます。**
   ```
   kubectl get service -n student99
   ```
1. AWS マネジメントコンソールで EC2 のページを表示して、次の名前のインスタンスの**パブリック IPv4 アドレス**の値をメモしておきます。
   ```
   tgb-cluster-tgb-nodes-Node
   ```
1. Webブラウザで新しいタブを開き、次のように URL を指定して **Top Page** という文字を含んだ Web ページが表示されることを確認します。
   ```
   http://<パブリックIPv4アドレス>:<NodePort>
   ```
1. Service を削除します。
   ```
   kubectl delete -f service/service-nodeport.yaml 
   ``` 
1. Service の削除を確認します。-n の後には自分の Namespace を指定します。
   ```
   kubectl get service -n student99

---

## LoadBalancer タイプの Service の作成

1. Cloud9 画面左側から 下記の Service のマニフェストのファイルをダブルクリックして開きます。
   ```
   running_containers_on_amazon_eks/mod7/service/service-loadbalancer.yaml
   ```
1. マニフェストの中で **namespace の値を自分に割当てられた値に変更**してファイルを保存します。

1. Cloud 9 のターミナルで次のコマンドを実行して Service を作成します。
   ```
   kubectl apply -f service/service-loadbalancer.yaml 
   ```
1. Service を表示します。-n の後には自分の Namespace を指定します。**出力から XXXX の値をメモしておきます。** 
   ```
   kubectl get service -n student99
   ```
1. Webブラウザで新しいタブを開き、次のように URL を指定して **Top Page** という文字を含んだ Web ページが表示されることを確認します。**アクセス可能になるまで少し待つ必要があります。** 表示されたら、何回か繰り返してアクセスして、表示される AZ の値が切替わることを確認します。
   ```
   http://XXXX
   ```
1. Service を削除します。
   ```
   kubectl delete -f service/service-loadbalancer.yaml 
   ``` 
1. Service の削除を確認します。-n の後には自分の Namespace を指定します。
   ```
   kubectl get service -n student99
---

## Ingress の作成

1. Cloud9 画面左側から 下記の Service のマニフェストのファイルをダブルクリックして開きます。
   ```
   running_containers_on_amazon_eks/mod7/ingress/ingress-alb-ip.yaml
   ```
1. マニフェストの中で **namespace の値を自分に割当てられた値に変更**してファイルを保存します。

1. Cloud 9 のターミナルで次のコマンドを実行して Ingress を作成します。
   ```
   kubectl apply -f ingress/ingress-alb-ip.yaml
   ```
1. Ingress を表示します。-n の後には自分の Namespace を指定します。**出力から XXXX の値をメモしておきます。** 
   ```
   kubectl get ingress -n student99
   ```
1. Webブラウザで新しいタブを開き、次のように URL を指定して **Top Page** という文字を含んだ Web ページが表示されることを確認します。**アクセス可能になるまで少し待つ必要があります。** 表示されたら、何回か繰り返してアクセスして、表示される AZ の値が切替わることを確認します。
   ```
   http://XXXX
   ```
1. Ingressを削除します。
   ```
   kubectl delete -f service/ingress/ingress-alb-ip.yaml
   ``` 
1. Ingressの削除を確認します。-n の後には自分の Namespace を指定します。
   ```
   kubectl get Ingress -n student99

---

## ワークの終了

1. Web ブラウザで Cloud 9 IDE のタブを閉じます。

1. AWS マネジメントコンソールで、右上に表示されている IAM ユーザー名をクリックして、メニューからサインアウトをクリックします。
* お疲れ様でした！
  
