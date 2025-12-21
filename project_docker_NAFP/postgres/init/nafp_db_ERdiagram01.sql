CREATE TABLE IF NOT EXISTS "users" (
	"id" SERIAL,
	"name" VARCHAR(45) NOT NULL,
	"password_hash" VARCHAR(255) NOT NULL,
	"email" VARCHAR(255) NOT NULL,
	"admin" BOOLEAN NOT NULL DEFAULT FALSE,
	"created_by" VARCHAR(45) NOT NULL,
	"created_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	"updated_by" VARCHAR(45) NOT NULL,
	"updated_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	"deleted_at" TIMESTAMP,
	PRIMARY KEY("id")
);

COMMENT ON TABLE "users" IS 'ユーザー情報テーブル';


CREATE TABLE IF NOT EXISTS "items" (
	"id" SERIAL,
	"name" VARCHAR(100) NOT NULL,
	"description" VARCHAR(200) NOT NULL,
	"price" INTEGER NOT NULL,
	"created_by" VARCHAR(45) NOT NULL,
	"created_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	"updated_by" VARCHAR(45) NOT NULL,
	"updated_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	"deleted_at" TIMESTAMP,
	PRIMARY KEY("id")
);

COMMENT ON TABLE "items" IS '商品情報テーブル';


CREATE TABLE IF NOT EXISTS "categories" (
	"id" SERIAL,
	"name" VARCHAR(100) NOT NULL,
	"description" VARCHAR(200) NOT NULL,
	"created_by" VARCHAR(45) NOT NULL,
	"created_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	"updated_by" VARCHAR(45) NOT NULL,
	"updated_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	"deleted_at" TIMESTAMP,
	PRIMARY KEY("id")
);

COMMENT ON TABLE "categories" IS 'カテゴリ情報テーブル';


CREATE TABLE IF NOT EXISTS "item_category" (
	"item_id" INTEGER NOT NULL,
	"category_id" INTEGER NOT NULL,
	"created_by" VARCHAR(45) NOT NULL,
	"created_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	"updated_by" VARCHAR(45) NOT NULL,
	"updated_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	"deleted_at" TIMESTAMP,
	PRIMARY KEY("item_id", "category_id")
);

COMMENT ON TABLE "item_category" IS '商品とカテゴリの関連テーブル';
CREATE INDEX "idx_item_category_category_id"
ON "item_category" ("category_id");
ALTER TABLE "item_category"
ADD FOREIGN KEY("item_id") REFERENCES "items"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "item_category"
ADD FOREIGN KEY("category_id") REFERENCES "categories"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;

-- 初期管理者ユーザーの挿入 admin123
INSERT INTO "users" ("name", "password_hash", "email", "admin", "created_by", "updated_by")
VALUES (
	'admin',
	'$2b$12$AemB3IUP9cipWKOBMoJSe.xGAGeysP0jLqrobPyVoFfkqxre6zYwm',  -- パスワード: admin123
	'admin@example.com',
	TRUE,
	'system',
	'system'
);
