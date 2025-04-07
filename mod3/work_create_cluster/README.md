# eksctl を使用して Amazon EKS クラスターを作成してみよう

---

## 環境への接続について

**このワーク環境は、ワーク実施時だけの一時的な環境になります。**

1. 講師が指定する AWS アカウント、IAM ユーザー、パスワードを使用して AWS マネジメントコンソールにサインインします。
1. 東京リージョンの Cloud 9 のページを表示します。IAM ユーザー毎に 1つの Cloud 9 IDE が用意されているので、[**開く**] をクリックします。

---

## Cloud 9 の一時認証情報の無効化
1. Cloud 9 画面の右上にある**歯車アイコン**をクリックします。
1. Preferences タブ の左側で **AWS Settings** をクリックします。
1. 右側の **Credentials** にある **AWS managed temporary credentials** トグルを OFFにします。
  ![codepipeline-demo-img](https://eks.nobelabo.net/images/mod7-cloud9.png)
1. Preferences のタブを閉じます。

---

## 現在の IAM ロールの確認

1. Cloud 9 のターミナルで次のコマンドを実行します。 
   ```
   aws sts get-caller-identity
   ```
1. 出力された Arn に、**my-EC2-AdminAccess-Role** という文字が含まれていることを確認します。

---
   
## kubectl のインストール

1. Cloud 9 のターミナルで次のコマンドを実行します。 (下記のコマンドを 1つずつ実行してください）
   ```
   curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.31.3/2024-12-12/bin/linux/amd64/kubectl
   ```

   ```
   sudo chmod +x ./kubectl
   ```

   ```
   mkdir -p $HOME/bin && cp ./kubectl $HOME/bin/kubectl && export PATH=$PATH:$HOME/bin
   ```

   ```
   echo 'export PATH=$PATH:$HOME/bin' >> ~/.bashrc
   ```

   ```
   kubectl version --client
   ```
   
1. 次の例のようなバージョンが表示されることを確認します。 (バージョン番号は異なっていても問題ありません。)
   ```
   Client Version: v1.31.3-eks-59bf375
   Kustomize Version: v5.4.2b
   ```
---

## eksctl のインストール


1. Cloud 9 のターミナルで次のコマンドを実行します。 (下記のコマンドを 1つずつ実行してください）
   ```
   ARCH=amd64
   PLATFORM=$(uname -s)_$ARCH
   ```

   ```
   curl -sLO "https://github.com/eksctl-io/eksctl/releases/latest/download/eksctl_$PLATFORM.tar.gz"

   ```

   ```
   tar -xzf eksctl_$PLATFORM.tar.gz -C /tmp && rm eksctl_$PLATFORM.tar.gz
   ```

   ```
   sudo mv /tmp/eksctl /usr/local/bin
   ```

   ```
   eksctl version 
   ```
   
1. 次の例のようなバージョンが表示されることを確認します。 (バージョン番号は異なっていても問題ありません。)
   ```
   0.207.0
   ```


---
## Amazon EKS クラスターの作成

1. 環境変数 YOUR_NUMBER にご自分の番号を設定します。★下記は例です。**99 の部分をご自分の番号に変更して下さい。**

    ```
    YOUR_NUMBER=99
    ```

1. eksctl を使用して Amazon EKS クラスターを作成します。


    ```
    eksctl create cluster \
    --name my-cluster-${YOUR_NUMBER} \
    --nodegroup-name my-nodes \
    --node-type t3.small \
    --nodes 1 \
    --nodes-min 1 \
    --nodes-max 2 \
    --managed \
    --version 1.31 \
    --region ap-northeast-1
    ```

1. クラスター作成が完了するまで約 15分～20分ほど待ちます。
    Cloud9 のページやターミナルはそのままにしておいてください。

1. クラスター作成完了後、下記を実行して Amazon EKS への接続を確認します。

    ```
    kubectl get node
    ```

    ```
    kubectl get namespace
    ```

1. 下記を実行して .kube フォルダの config ファイルを確認します。

    ```
    cd ~/.kube
    ```

    ```
    ls -la
    ```

    ```
    cat config
    ```

    ```
    cd ~/environment/
    ```
---

## ワークの終了
1. Cloud 9 のターミナルで次のコマンドを実行して Amazon EKS クラスターを削除します。
   ```
   eksctl delete cluster --name my-cluster-${YOUR_NUMBER}
   ```
1. Web ブラウザで Cloud 9 IDE のタブを閉じます。

1. AWS マネジメントコンソールで、右上に表示されている IAM ユーザー名をクリックして、メニューからサインアウトをクリックします。
* お疲れ様でした！
* **このワーク環境は、ワーク実施時だけの一時的な環境になります。**  
