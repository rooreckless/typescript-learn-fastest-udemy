-- public.categories definition

-- Drop table

-- DROP TABLE public.categories;

CREATE TABLE public.categories (
	id serial4 NOT NULL,
	"name" varchar(200) NOT NULL,
	description varchar(200) NOT NULL,
	created_by varchar(45) NOT NULL,
	created_at timestamptz DEFAULT CURRENT_TIMESTAMP NOT NULL,
	updated_by varchar(45) NOT NULL,
	updated_at timestamptz DEFAULT CURRENT_TIMESTAMP NOT NULL,
	deleted_at timestamptz NULL,
	CONSTRAINT categories_pkey PRIMARY KEY (id)
);
COMMENT ON TABLE public.categories IS 'カテゴリ情報テーブル';


-- public.items definition

-- Drop table

-- DROP TABLE public.items;

CREATE TABLE public.items (
	id serial4 NOT NULL,
	"name" varchar(100) NOT NULL,
	description varchar(200) NOT NULL,
	price int4 NOT NULL,
	created_by varchar(45) NOT NULL,
	created_at timestamptz DEFAULT CURRENT_TIMESTAMP NOT NULL,
	updated_by varchar(45) NOT NULL,
	updated_at timestamptz DEFAULT CURRENT_TIMESTAMP NOT NULL,
	deleted_at timestamptz NULL,
	CONSTRAINT items_pkey PRIMARY KEY (id)
);
COMMENT ON TABLE public.items IS '商品情報テーブル';


-- public.users definition

-- Drop table

-- DROP TABLE public.users;

CREATE TABLE public.users (
	id serial4 NOT NULL,
	"name" varchar(45) NOT NULL,
	password_hash varchar(255) NOT NULL,
	email varchar(255) NOT NULL,
	"admin" bool DEFAULT false NOT NULL,
	created_by varchar(45) NOT NULL,
	created_at timestamptz DEFAULT CURRENT_TIMESTAMP NOT NULL,
	updated_by varchar(45) NOT NULL,
	updated_at timestamptz DEFAULT CURRENT_TIMESTAMP NOT NULL,
	deleted_at timestamptz NULL,
	CONSTRAINT users_pkey PRIMARY KEY (id)
);
COMMENT ON TABLE public.users IS 'ユーザー情報テーブル';


-- public.item_category definition

-- Drop table

-- DROP TABLE public.item_category;

CREATE TABLE public.item_category (
	item_id int4 NOT NULL,
	category_id int4 NOT NULL,
	created_by varchar(45) NOT NULL,
	created_at timestamptz DEFAULT CURRENT_TIMESTAMP NOT NULL,
	updated_by varchar(45) NOT NULL,
	updated_at timestamptz DEFAULT CURRENT_TIMESTAMP NOT NULL,
	deleted_at timestamptz NULL,
	CONSTRAINT item_category_pkey PRIMARY KEY (item_id, category_id),
	CONSTRAINT item_category_category_id_fkey FOREIGN KEY (category_id) REFERENCES public.categories(id),
	CONSTRAINT item_category_item_id_fkey FOREIGN KEY (item_id) REFERENCES public.items(id)
);
CREATE INDEX idx_item_category_category_id ON public.item_category USING btree (category_id);
COMMENT ON TABLE public.item_category IS '商品とカテゴリの関連テーブル';

-- 初期管理者ユーザーの挿入 admin123
INSERT INTO public.users ("name", "password_hash", "email", "admin", "created_by", "updated_by")
VALUES (
	'admin',
	'$2b$12$AemB3IUP9cipWKOBMoJSe.xGAGeysP0jLqrobPyVoFfkqxre6zYwm',  -- パスワード: admin123
	'admin@example.com',
	TRUE,
	'system',
	'system'
);
