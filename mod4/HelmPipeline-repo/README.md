## HelmのチャートをEKSクラスタにデプロイするCodePipelineのリソース
- buildspec.yml
  - CodeBuildによるビルド処理内容が記述されているファイル
    - dockerのコマンドを発行しコンテナイメージをビルドしてタグ付けを行っている。
    - ビルド後、構築したイメージをAmazon ECRにpushしている。
- templates
  - deployment
    - hello-deployment.yaml
  - service
    - hello-service.yaml
- Chart.yaml
  - Helmのアプリケーション情報
- values.yaml
  - Helmのアプリケーションに設定する値
    
## 処理内容
- Helmのチャートとbuildspec.ymlをCodeCommitにpushする。
- CodePipelineがCodeCommitの変更を検知してソースを取り出す。
- CodePipelineによりCodeBuildのプロジェクトが実行され、HelmチャートをEKSクラスターにデプロイする。