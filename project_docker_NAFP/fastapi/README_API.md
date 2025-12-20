# NAFP API - ドメイン駆動設計（DDD）CRUD API

このプロジェクトは、ドメイン駆動設計（Domain-Driven Design: DDD）に基づいて構築されたFastAPI CRUD APIです。

## 🏗️ アーキテクチャ

### DDDレイヤー構造

```
fastapi/
├── domain/              # ドメイン層
│   ├── entities.py     # エンティティ（ビジネスオブジェクト）
│   └── repositories.py # リポジトリインターフェース
├── application/         # アプリケーション層
│   ├── user_service.py    # ユーザーユースケース
│   ├── item_service.py    # 商品ユースケース
│   └── category_service.py # カテゴリユースケース
├── infrastructure/      # インフラストラクチャ層
│   ├── database.py     # データベース接続
│   ├── models.py       # SQLAlchemyモデル
│   ├── user_repository.py      # ユーザーリポジトリ実装
│   ├── item_repository.py      # 商品リポジトリ実装
│   ├── category_repository.py  # カテゴリリポジトリ実装
│   └── item_category_repository.py # 商品カテゴリリポジトリ実装
├── presentation/        # プレゼンテーション層
│   ├── schemas.py      # リクエスト/レスポンススキーマ
│   ├── dependencies.py # 依存性注入
│   ├── user_routes.py     # ユーザーAPIエンドポイント
│   ├── item_routes.py     # 商品APIエンドポイント
│   └── category_routes.py # カテゴリAPIエンドポイント
└── main.py             # アプリケーションエントリーポイント
```

### DDDの原則

1. **ドメイン層（Domain Layer）**
   - ビジネスロジックの中核
   - エンティティと値オブジェクトを定義
   - リポジトリインターフェースを定義（依存性逆転の原則）

2. **アプリケーション層（Application Layer）**
   - ユースケース（アプリケーションサービス）
   - ドメインオブジェクトを調整してビジネスロジックを実行

3. **インフラストラクチャ層（Infrastructure Layer）**
   - 技術的な詳細の実装
   - データベースアクセス、外部APIとの連携
   - リポジトリインターフェースの具体的な実装

4. **プレゼンテーション層（Presentation Layer）**
   - ユーザーインターフェース（APIエンドポイント）
   - リクエスト/レスポンスの処理

## 📊 データベーススキーマ

### テーブル構成

- **users**: ユーザー情報
- **items**: 商品情報
- **categories**: カテゴリ情報
- **item_category**: 商品とカテゴリの関連（多対多）

## 🚀 起動方法

### 前提条件

- Docker
- Docker Compose

### 起動コマンド

```bash
# プロジェクトのルートディレクトリから
docker-compose -f composes/dev.yml up --build
```

### サービス構成

- **PostgreSQL**: ポート 5432
- **FastAPI**: ポート 8000
- **Angular**: ポート 4200
- **Nginx**: ポート 80

## 📚 API ドキュメント

起動後、以下のURLでAPIドキュメントにアクセスできます：

- **Swagger UI**: http://localhost:8000/api/docs
- **ReDoc**: http://localhost:8000/api/redoc

## 🔌 APIエンドポイント

### ユーザー (Users)

| メソッド | エンドポイント | 説明 |
|---------|--------------|------|
| POST | `/api/users` | ユーザーを作成 |
| GET | `/api/users` | 全ユーザーを取得 |
| GET | `/api/users/{user_id}` | 特定のユーザーを取得 |
| PUT | `/api/users/{user_id}` | ユーザーを更新 |
| DELETE | `/api/users/{user_id}` | ユーザーを削除（論理削除） |

### 商品 (Items)

| メソッド | エンドポイント | 説明 |
|---------|--------------|------|
| POST | `/api/items` | 商品を作成 |
| GET | `/api/items` | 全商品を取得 |
| GET | `/api/items/{item_id}` | 特定の商品を取得 |
| GET | `/api/items/{item_id}/with-categories` | カテゴリ付きで商品を取得 |
| PUT | `/api/items/{item_id}` | 商品を更新 |
| DELETE | `/api/items/{item_id}` | 商品を削除（論理削除） |

### カテゴリ (Categories)

| メソッド | エンドポイント | 説明 |
|---------|--------------|------|
| POST | `/api/categories` | カテゴリを作成 |
| GET | `/api/categories` | 全カテゴリを取得 |
| GET | `/api/categories/{category_id}` | 特定のカテゴリを取得 |
| GET | `/api/categories/{category_id}/items` | カテゴリに属する商品を取得 |
| PUT | `/api/categories/{category_id}` | カテゴリを更新 |
| DELETE | `/api/categories/{category_id}` | カテゴリを削除（論理削除） |
| POST | `/api/categories/item-category` | 商品にカテゴリを追加 |
| DELETE | `/api/categories/item-category/{item_id}/{category_id}` | 商品からカテゴリを削除 |

## 💡 使用例

### ユーザーを作成

```bash
curl -X POST "http://localhost:8000/api/users" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "山田太郎",
    "email": "yamada@example.com",
    "password": "securepass123",
    "created_by": "admin"
  }'
```

### 商品を作成

```bash
curl -X POST "http://localhost:8000/api/items" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "ノートPC",
    "description": "高性能なノートパソコン",
    "price": 150000,
    "created_by": "admin"
  }'
```

### カテゴリを作成

```bash
curl -X POST "http://localhost:8000/api/categories" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "電化製品",
    "description": "電子機器やガジェット",
    "created_by": "admin"
  }'
```

### 商品にカテゴリを追加

```bash
curl -X POST "http://localhost:8000/api/categories/item-category" \
  -H "Content-Type: application/json" \
  -d '{
    "item_id": 1,
    "category_id": 1,
    "created_by": "admin"
  }'
```

## 🛠️ 技術スタック

- **FastAPI**: 高性能なPython Webフレームワーク
- **SQLAlchemy**: Python ORM（非同期対応）
- **asyncpg**: PostgreSQL非同期ドライバ
- **Pydantic**: データバリデーション
- **PostgreSQL**: リレーショナルデータベース
- **Docker**: コンテナ化

## 🔐 セキュリティ機能

- パスワードのbcryptハッシュ化
- 論理削除（deleted_at）による安全なデータ削除
- メールアドレスの一意性制約
- バリデーション（Pydantic）

## 📝 開発のポイント

### DDDの利点

1. **関心の分離**: 各層が明確な責任を持つ
2. **テストしやすさ**: インターフェースを通じてモック化が容易
3. **保守性**: ビジネスロジックがインフラから独立
4. **拡張性**: 新機能の追加が容易

### 依存性逆転の原則

ドメイン層でリポジトリインターフェースを定義し、インフラ層で実装することで、ビジネスロジックがデータベースの実装詳細に依存しない設計になっています。

## 🧪 テスト

```bash
# テストの実行（pytest）
docker-compose -f composes/dev.yml exec fastapi pytest
```

## 📖 参考資料

- [FastAPI公式ドキュメント](https://fastapi.tiangolo.com/)
- [ドメイン駆動設計（DDD）](https://www.oreilly.com/library/view/domain-driven-design-tackling/0321125215/)
- [Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
