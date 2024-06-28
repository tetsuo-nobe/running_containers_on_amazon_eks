# CodePipelineのパイプラインからHelmチャートをデプロイするデモ

* CodeCommit の Git リポジトリでHelmチャートを管理している前提

* Helmチャートを更新して、CodeCommit に push することでCodePipelineが自動的にパイプラインを実行

* パイプラインが CodeCommit から Helm チャートを取得し、CodeBuild のビルドプロジェクトを実行

* CodeBuild のビルド処理の中で Helmチャートをデプロイ




