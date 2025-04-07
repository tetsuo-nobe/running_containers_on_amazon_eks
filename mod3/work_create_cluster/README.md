# eksctl ���g�p���� Amazon EKS �N���X�^�[���쐬���Ă݂悤

---

## ���ւ̐ڑ��ɂ���

**���̃��[�N���́A���[�N���{�������̈ꎞ�I�Ȋ��ɂȂ�܂��B**

1. �u�t���w�肷�� AWS �A�J�E���g�AIAM ���[�U�[�A�p�X���[�h���g�p���� AWS �}�l�W�����g�R���\�[���ɃT�C���C�����܂��B
1. Cloud 9 �̃y�[�W��\�����܂��BIAM ���[�U�[���� 1�� Cloud 9 IDE ���p�ӂ���Ă���̂ŁA[**�J��**] ���N���b�N���܂��B

---

## Cloud 9 �̈ꎞ�F�؏��̖�����
1. Cloud 9 ��ʂ̉E��ɂ���**���ԃA�C�R��**���N���b�N���܂��B
1. Preferences �^�u �̍����� **AWS Settings** ���N���b�N���܂��B
1. �E���� **Credentials** �ɂ��� **AWS managed temporary credentials** �g�O���� OFF�ɂ��܂��B
  ![codepipeline-demo-img](https://eks.nobelabo.net/images/mod7-cloud9.png)
1. Preferences �̃^�u����܂��B

---

## ���݂� IAM ���[���̊m�F

1. Cloud 9 �̃^�[�~�i���Ŏ��̃R�}���h�����s���܂��B 
   ```
   aws sts get-caller-identity
   ```
1. �o�͂��ꂽ Arn �ɁA**my-EC2-EKS-DesclibeCluster-Role** �Ƃ����������܂܂�Ă��邱�Ƃ��m�F���܂��B

---
   
## kubectl �̃C���X�g�[��

1. Cloud 9 �̃^�[�~�i���Ŏ��̃R�}���h�����s���܂��B (���L�̃R�}���h�� 1�����s���Ă��������j
   ```
   curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.31.4/2025-01-10/bin/darwin/amd64/kubectl
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
   
1. ���̗�̂悤�ȃo�[�W�������\������邱�Ƃ��m�F���܂��B (�o�[�W�����ԍ��͈قȂ��Ă��Ă���肠��܂���B)
   ```
   Client Version: v1.31.5-eks-43840fb
   ```
---

## eksctl �̃C���X�g�[��


1. Cloud 9 �̃^�[�~�i���Ŏ��̃R�}���h�����s���܂��B (���L�̃R�}���h�� 1�����s���Ă��������j
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
   
1. ���̗�̂悤�ȃo�[�W�������\������邱�Ƃ��m�F���܂��B (�o�[�W�����ԍ��͈قȂ��Ă��Ă���肠��܂���B)
   ```
   Client Version: v1.31.5-eks-43840fb
   ```


---
## Amazon EKS �N���X�^�[�̍쐬

1. ���ϐ� YOUR_NUMBER �ɂ������̔ԍ���ݒ肵�܂��B�����L�͗�ł��B**99 �̕������������̔ԍ��ɕύX���ĉ������B**

    ```
    YOUR_NUMBER=99
    ```

1. eksctl ���g�p���� Amazon EKS �N���X�^�[���쐬���܂��B


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

1. �N���X�^�[�쐬����������܂Ŗ� 20���قǑ҂��܂��B
    Cloud9 �̃y�[�W��^�[�~�i���͂��̂܂܂ɂ��Ă����Ă��������B

1. �N���X�^�[�쐬������A���L�����s���� Amazon EKS �ւ̐ڑ����m�F���܂��B

    ```
    kubectl get node
    ```

    ```
    kubectl get namespace
    ```


---

## ���[�N�̏I��
1. Cloud 9 �̃^�[�~�i���Ŏ��̃R�}���h�����s���� Amazon EKS �N���X�^�[���폜���܂��B
   ```
   eksctl delete cluster --name my-cluster-${YOUR_NUMBER}
   ```
1. Web �u���E�U�� Cloud 9 IDE �̃^�u����܂��B

1. AWS �}�l�W�����g�R���\�[���ŁA�E��ɕ\������Ă��� IAM ���[�U�[�����N���b�N���āA���j���[����T�C���A�E�g���N���b�N���܂��B
* �����l�ł����I
* **���̃��[�N���́A���[�N���{�������̈ꎞ�I�Ȋ��ɂȂ�܂��B**  