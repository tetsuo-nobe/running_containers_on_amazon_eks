# ベースイメージの指定
FROM python:3.6

# 作業ディレクトリの指定
WORKDIR /app

# カレントディレクトリのファイルをコンテナの/app にコピー
ADD . /app

# Flask, boto3, X-Rayをインストール
RUN pip install Flask && pip install boto3 && pip install aws-xray-sdk

# 外部公開用ポートの指定
EXPOSE 8000

# コンテナ起動時のコマンドの指定
CMD ["python", "app.py"]