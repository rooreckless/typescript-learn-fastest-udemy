# =========================================
# PostgreSQL 開発環境用 Dockerfile
# =========================================

# 公式PostgreSQLイメージを使用（16.11-bookworm）
FROM postgres:16.11-bookworm

# メタデータラベル
LABEL maintainer="TAFP Development Team"
LABEL description="PostgreSQL database for TAFP development environment"

# 環境変数の設定（デフォルト値）
# これらは docker-compose.yml で上書き可能
ENV POSTGRES_DB=tafp_db \
    POSTGRES_USER=tafp_user \
    POSTGRES_PASSWORD=devpassword

# タイムゾーンの設定
ENV TZ=Asia/Tokyo

# 必要なパッケージのインストール（開発用ツール）
RUN apt-get update && apt-get install -y --no-install-recommends \
    # タイムゾーンデータ
    tzdata \
    # PostgreSQL拡張機能のビルドツール
    postgresql-server-dev-16 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# ポート番号の公開
EXPOSE 5432

# データディレクトリのボリューム設定
VOLUME ["/var/lib/postgresql/data"]

# ヘルスチェック設定
# データベースが正常に起動しているか定期的に確認
HEALTHCHECK --interval=10s --timeout=5s --retries=5 \
    CMD pg_isready -U $POSTGRES_USER -d $POSTGRES_DB || exit 1

# デフォルトコマンド（PostgreSQLサーバーの起動）
# alpine版なので postgres ユーザーで実行される
CMD ["postgres"]
