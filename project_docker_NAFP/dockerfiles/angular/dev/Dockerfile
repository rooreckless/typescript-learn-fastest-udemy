# =========================================
# Angular 開発環境用 Dockerfile
# =========================================

# Node.js公式イメージを使用（22.12.0-slim）
FROM node:22.12.0-slim

# メタデータラベル
LABEL maintainer="NAFP Development Team"
LABEL description="Angular frontend for NAFP development environment"

# 作業ディレクトリの設定
WORKDIR /app

# 環境変数の設定
ENV NODE_ENV=development \
    # Angular CLIのキャッシュディレクトリ
    NG_CLI_ANALYTICS=false \
    # npmのキャッシュ設定
    npm_config_cache=/tmp/.npm

# 必要なパッケージのインストール（ヘルスチェック用）
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# グローバルパッケージのインストール
# Angular CLIをバージョン21でインストール
RUN npm install -g @angular/cli@21

# パッケージ定義ファイルのコピー
# 先にpackage.jsonとpackage-lock.jsonだけコピーしてキャッシュを効率化
COPY angular/package*.json ./

# 依存パッケージのインストール
RUN npm install

# アプリケーションコードのコピー
# 開発環境ではボリュームマウントするため、ここでは基本的な構造のみ
COPY angular/ .

# ポート番号の公開
EXPOSE 4200

# ヘルスチェック設定
# Angular開発サーバーが起動しているか確認
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
    CMD wget --no-verbose --tries=1 --spider http://localhost:4200 || exit 1

# 開発用コマンド（ホットリロード有効）
# すべてのネットワークインターフェースからアクセス可能にする
CMD ["npm", "start"]
