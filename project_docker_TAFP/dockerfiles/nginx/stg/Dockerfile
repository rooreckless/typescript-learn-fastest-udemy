# =========================================
# Nginx stg環境用 Dockerfile
# =========================================

# build用nodeイメージを使用
FROM node:22.12.0-slim AS build

WORKDIR /app
COPY angular/package*.json ./
RUN npm install
RUN npm ci
COPY angular/ ./
RUN npm run build

# -- serve --
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

# カスタム設定ファイルをコピー
# 開発環境ではボリュームマウントで上書きされる
COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY nginx/conf.d/ /etc/nginx/conf.d/
# ビルド成果物をNginxの公開ディレクトリにコピー
COPY --from=build /app/dist/ /usr/share/nginx/html

# ポート番号の公開
EXPOSE 80 443

# ヘルスチェック設定
# Nginxが正常に動作しているか確認
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
    CMD curl -f http://localhost/health || exit 1

# Nginxをフォアグラウンドで起動
CMD ["nginx", "-g", "daemon off;"]
