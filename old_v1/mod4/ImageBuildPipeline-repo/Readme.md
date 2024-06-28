## DockerイメージをビルドしてAmazon ECRにプッシュするCodePipelineのリソース
- buildspec.yml
  - CodeBuildによるビルド処理内容が記述されているファイル
    - dockerのコマンドを発行しコンテナイメージをビルドしてタグ付けを行っている。
    - ビルド後、構築したイメージをAmazon ECRにpushしている。
- Dockerfile
  - Dockerイメージのビルド用
    - Node.jsでWebページを表示するコンテナイメージ

## 処理内容
- Dockerfileとbuildspec.ymlをCodeCommitにpushする。
- CodePipelineがCodeCommitの変更を検知してソースを取り出す。
- CodePipelineによりCodeBuildのプロジェクトが実行され、DockerイメージがビルドされAmazon ECRにpushする。
