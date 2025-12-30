# TAFP Stack - Docker Compose 開発環境

(Traefik or Nginx) + Angular + FastAPI + PostgreSQL を使用したフルスタック開発環境です。

## 🏗️ アーキテクチャ

```
[Browser] → [Nginx:80] → [Angular:4200] (Frontend)
                       → [FastAPI:8000] (Backend API)
                       → [PostgreSQL:5432] (Database)
```

## 📋 前提条件

- Docker
- Docker Compose

## 🚀 起動方法

### 開発環境の起動

```bash
cd project_docker_TAFP
docker-compose -f composes/dev.yml --profile dev build --no-cache
docker-compose -f composes/dev.yml --profile dev up
```

または、バックグラウンドで起動:

```bash
docker-compose -f composes/dev.yml --profile dev build --no-cache
docker-compose -f composes/dev.yml --profile dev up -d
```

### 開発環境のサービスへのアクセス

- **Traefik (開発環境用ロードバランサ)** : http://localhost:8880/
- **Angular (フロントエンド)**: http://localhost/
- **FastAPI (バックエンド)**: http://localhost/api
- **FastAPI ドキュメント**: http://localhost/api/docs
- **PostgreSQL**: localhost:5432

- **Nginx (メインエントリーポイント)**: http://localhost

### 開発環境として動いているコンテナにログインする方法

`docker compose`の`exec`かを使用してください。

```bash
# dev.ymlで起動しているとし、そのdev.ymlのangularサービスにログインする場合
docker compose -f composes/dev.ym
l --profile dev exec -it angular /bin/bash
# dev.ymlで起動しているとし、そのdev.ymlのfastapiサービスにログインする場合
docker compose -f composes/dev.ym
l --profile dev exec -it fastapi /bin/bash
```


### 停止方法

```bash
docker-compose -f composes/dev.yml --profile dev down
```

データベースのデータも削除する場合:

```bash
docker-compose -f composes/dev.yml --profile dev down -v
```

#### stg環境の起動用コマンドと停止方法

`--profile`に`stg`を入れることで、stg環境用に起動します。

```bash
cd project_docker_TAFP
docker-compose -f composes/dev.yml --profile stg build --no-cache
docker-compose -f composes/dev.yml --profile stg up -d
```

stg環境ではtraefikとangularサーバーは使用しません。これらの代わりにnginxが使われるようになります。

angularは`build`の段階でビルドされ、`up`でnginxにて静的コンテンツとして配信するようになりつつ、`http://localhost/`でフロントエンドにアクセス可能に、`http://localhost/api`でバックエンドにアクセス可能に」なります。(`http://localhost/api/docs/`も一緒)

### 特定のコンテナの再起動方法

angularサービスの再起動だと以下の要領

```bash
docker-compose -f composes/dev.yml --profile dev restart angular
```

## 📁 ディレクトリ構造

```
project_docker_TAFP/
├── composes/
│   ├── dev.yml              # 開発環境兼stg環境用docker-compose
│   └── prd.yml              # 本番環境用docker-compose（予定）
├── dockerfiles/
│   ├── angular/dev/         # Angular開発用Dockerfile
│   ├── fastapi/dev/         # FastAPI開発用Dockerfile
│   ├── nginx/dev/           # Nginx用Dockerfile(stg環境と本番環境(予定)用)
│   └── postgres/dev/        # PostgreSQL開発用Dockerfile
├── angular/                 # Angularソースコード
├── fastapi/                 # FastAPIソースコード
├── nginx/                   # Nginx設定ファイル
└── postgres/                # PostgreSQL初期化スクリプト
```

## 🔧 開発時の機能

### ホットリロード

- **Angular**: ソースコード変更時に自動的にブラウザがリロードされます
- **FastAPI**: ソースコード変更時に自動的にサーバーが再起動されます

### デバッグ

各サービスのログを確認:

```bash
# すべてのログ
docker-compose -f composes/dev.yml --profile dev logs -f

# 特定のサービスのログ
docker-compose -f composes/dev.yml --profile dev logs -f angular
docker-compose -f composes/dev.yml --profile dev logs -f fastapi
docker-compose -f composes/dev.yml --profile dev logs -f postgres
docker-compose -f composes/dev.yml --profile dev logs -f nginx
```

### VsCodeでのデバッグ

wslに接続している状態もVsCodeで`project_docker_TAFP`ディレクトリを開き、`-f composes/dev.yml --profile dev`でdocker compose upをしてください。

その状態だと、そのVsCodeのデバッグビューから、「実行とデバッグ」で実行すると、ブレークポイントがつかえるようになります。

### データベース接続

コンテナ内からPostgreSQLに接続:

```bash
docker-compose -f composes/dev.yml --profile dev　exec postgres psql -U tafp_user -d tafp_db
```

## 🛠️ 開発ワークフロー

1. **コードの変更**: ホスト側の `angular/` または `fastapi/` ディレクトリ内のファイルを編集
2. **自動反映**: ホットリロードにより変更が自動的にコンテナに反映されます
3. **動作確認**: ブラウザで http://localhost にアクセスして確認

## 📝 環境変数

開発環境用の環境変数は `composes/dev.yml` に定義されています。
必要に応じて変更してください。

## 🔍 トラブルシューティング

### ポートが既に使用されている

他のサービスが80, 4200, 8000, 5432ポートを使用している場合は、
`composes/dev.yml` のポートマッピングを変更してください。

### コンテナが起動しない

```bash
# コンテナの状態確認
docker-compose -f composes/dev.yml ps

# ログの確認
docker-compose -f composes/dev.yml logs
```

### データベースのリセット

```bash
docker-compose -f composes/dev.yml down -v
docker-compose -f composes/dev.yml up --build
```

## 📚 参考リンク

- [Angular Documentation](https://angular.io/docs)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Nginx Documentation](https://nginx.org/en/docs/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)



### スーパーユーザー
postgres/init/tafp_db_ERdiagram01.sqlにより、usersテーブルにはadmin=Trueなユーザーが作成される。

メールアドレスはadmin@example.com,パスワードは「admin123」を暗号化したものが入っている。

(admin123を暗号化した結果を確認するには、`docker exec tafp_fastapi_dev python -c "import bcrypt; print(bcrypt.hashpw(b'admin123', bcrypt.gensalt()).decode('utf-8'))"`のコマンドを使うこと。)