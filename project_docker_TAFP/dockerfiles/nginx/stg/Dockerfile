# =========================================
# Nginx stg環境用 Dockerfile
# ================================
# STG: Angular をビルドして nginx で配信する
# ================================
# 目的:
# - dev は Angular の開発サーバ(4200)を使うが、
#   stg は「模擬本番」なので、ビルド済み静的ファイルを nginx で配信したい。
# - これにより、(本番で想定する) CDN/S3 配信に近い条件で動作確認できる。
# - コンテナ起動後にビルドしないので、起動が速く、内容が再現性ある。

# --------------------------------
# Stage 1: Angular build
# --------------------------------
# build用nodeイメージを使用
FROM node:22.12.0-slim AS build
# 作業ディレクトリ
WORKDIR /app
# 依存解決の再現性を高めるため、まず package 系だけコピーする。
# ここが変わらない限り npm install のレイヤがキャッシュされるので高速。
COPY angular/package*.json ./
# stg は「確実に動く」ことが優先なので npm install を利用
# （理想は package-lock.json をコミットして npm ci に寄せる）
RUN npm install
# RUN npm ci

# アプリ本体をコピーしてビルド
# Angular の本番ビルド（dist/ に成果物が出る）
COPY angular/ ./
RUN npm run build

# --------------------------------
# Stage 2: nginx serve
# --------------------------------
# Nginx安定版のBookwormベースイメージを使用
FROM nginx:stable-bookworm

# メタデータラベル
LABEL maintainer="TAFP Development Team"
LABEL description="Nginx reverse proxy for TAFP staging environment"

# タイムゾーンの設定
ENV TZ=Asia/Tokyo

# 必要なパッケージのインストール
RUN apt-get update && apt-get install -y --no-install-recommends \
    # タイムゾーンデータ
    tzdata \
    # デバッグ用ツール
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# デフォルトのNginx設定を削除
RUN rm /etc/nginx/conf.d/default.conf

# nginx の基本設定と conf を配置
# - nginx.conf: 全体設定（gzip等）
# - default.conf: ルーティング(conf.d/stg内にある)（SPA配信 + /api を FastAPI へ）
COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY nginx/conf.d/ /etc/nginx/conf.d/

# Angular のビルド成果物を nginx の公開ディレクトリにコピー
# ※ dist の配下ディレクトリ名は Angular の設定で変わるので、
#   実際のプロジェクトに合わせてパスを調整する。
# 例: dist/tafp-angular/ → /usr/share/nginx/html/tafp-angular/
# --from=buildとは、Stage 1のビルド成果物を参照する指定。そこの/app/dist/の内容をStage 2のnginxの/usr/share/nginx/htmlにコピーする。
COPY --from=build /app/dist/ /usr/share/nginx/html

# ポート番号の公開
EXPOSE 80 443

# ヘルスチェック設定
# Nginxが正常に動作しているか確認
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
    CMD curl -f http://localhost/health || exit 1

# Nginxをフォアグラウンドで起動
CMD ["nginx", "-g", "daemon off;"]
