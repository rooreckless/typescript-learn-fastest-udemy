# =========================================
# FastAPI 開発環境用 Dockerfile
# =========================================

# Python公式イメージを使用（3.13.1-slim）
FROM python:3.13.1-slim

# メタデータラベル
LABEL maintainer="NAFP Development Team"
LABEL description="FastAPI backend for NAFP development environment"

# 作業ディレクトリの設定
WORKDIR /app

# 環境変数の設定
ENV PYTHONUNBUFFERED=1 \
    # Pythonがpycファイルを作成しないようにする
    PYTHONDONTWRITEBYTECODE=1 \
    # uvのインストールパス
    UV_SYSTEM_PYTHON=1

# システムパッケージの更新と必要なパッケージのインストール
RUN apt-get update && apt-get install -y --no-install-recommends \
    # PostgreSQLクライアントライブラリ
    libpq-dev \
    # Cコンパイラ（一部のPythonパッケージのビルドに必要）
    gcc \
    # ネットワークツール（デバッグ用）
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# uvのインストール（高速なPythonパッケージインストーラー）
# pipを使ってuvをインストール
RUN pip install --no-cache-dir uv

# 依存関係ファイルのコピー
# 先にrequirements.txtだけコピーすることでキャッシュを効率化
COPY fastapi/requirements.txt .

# Pythonパッケージのインストール（uvを使用）
RUN uv pip install --system -r requirements.txt

# アプリケーションコードのコピー
# 開発環境ではボリュームマウントするため、ここでは基本的な構造のみ
COPY fastapi/ .

# ポート番号の公開
EXPOSE 8000

# ヘルスチェック設定
# FastAPIのヘルスチェックエンドポイントを確認
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# 開発用コマンド（ホットリロード有効）
# docker-compose.ymlで上書き可能
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
