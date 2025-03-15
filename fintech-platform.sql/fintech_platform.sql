-- -------------------------------------------------------------
-- TablePlus 6.3.2(586)
--
-- https://tableplus.com/
--
-- Database: fintech_platform
-- Generation Time: 2025-03-14 17:20:00.7670
-- -------------------------------------------------------------


-- This script only contains the table creation statements and does not fully represent the table in the database. Do not use it as a backup.

-- Table Definition
CREATE TABLE "public"."accounts" (
    "user_id" int4 NOT NULL,
    "balance" numeric(18,8) NOT NULL,
    PRIMARY KEY ("user_id")
);

-- This script only contains the table creation statements and does not fully represent the table in the database. Do not use it as a backup.

-- Sequence and defined type
CREATE SEQUENCE IF NOT EXISTS assets_asset_id_seq;

-- Table Definition
CREATE TABLE "public"."assets" (
    "asset_id" int4 NOT NULL DEFAULT nextval('assets_asset_id_seq'::regclass),
    "name" varchar(100) NOT NULL,
    "symbol" varchar(10) NOT NULL,
    "price" numeric(18,8) NOT NULL,
    "market_cap" numeric(18,8),
    "last_updated" timestamp DEFAULT now(),
    "asset_description" text,
    PRIMARY KEY ("asset_id")
);

-- This script only contains the table creation statements and does not fully represent the table in the database. Do not use it as a backup.

-- Sequence and defined type
CREATE SEQUENCE IF NOT EXISTS orders_order_id_seq;

-- Table Definition
CREATE TABLE "public"."orders" (
    "order_id" int4 NOT NULL DEFAULT nextval('orders_order_id_seq'::regclass),
    "user_id" int4,
    "asset_id" int4,
    "type" varchar(50) NOT NULL,
    "quantity" numeric(18,8) NOT NULL,
    "price" numeric(18,8) NOT NULL,
    "status" varchar(50) DEFAULT 'pending'::character varying,
    "timestamp" timestamp DEFAULT now(),
    PRIMARY KEY ("order_id")
);

-- This script only contains the table creation statements and does not fully represent the table in the database. Do not use it as a backup.

-- Sequence and defined type
CREATE SEQUENCE IF NOT EXISTS portfolios_portfolio_id_seq;

-- Table Definition
CREATE TABLE "public"."portfolios" (
    "portfolio_id" int4 NOT NULL DEFAULT nextval('portfolios_portfolio_id_seq'::regclass),
    "user_id" int4,
    "asset_id" int4,
    "quantity" numeric(18,8) NOT NULL,
    "value" numeric(18,8) NOT NULL,
    "last_updated" timestamp DEFAULT now(),
    PRIMARY KEY ("portfolio_id")
);

-- This script only contains the table creation statements and does not fully represent the table in the database. Do not use it as a backup.

-- Table Definition
CREATE TABLE "public"."transactions" (
    PRIMARY KEY ("transaction_id","timestamp")
);

-- This script only contains the table creation statements and does not fully represent the table in the database. Do not use it as a backup.

-- Sequence and defined type
CREATE SEQUENCE IF NOT EXISTS transactions_transaction_id_seq1;

-- Table Definition
CREATE TABLE "public"."transactions_2023_01" (
    "transaction_id" int4 NOT NULL DEFAULT nextval('transactions_transaction_id_seq1'::regclass),
    "user_id" int4 NOT NULL,
    "asset_id" int4 NOT NULL,
    "amount" numeric(18,8) NOT NULL,
    "type" varchar(50) NOT NULL,
    "timestamp" timestamp NOT NULL,
    PRIMARY KEY ("transaction_id","timestamp")
);

-- This script only contains the table creation statements and does not fully represent the table in the database. Do not use it as a backup.

-- Sequence and defined type
CREATE SEQUENCE IF NOT EXISTS transactions_transaction_id_seq1;

-- Table Definition
CREATE TABLE "public"."transactions_2023_02" (
    "transaction_id" int4 NOT NULL DEFAULT nextval('transactions_transaction_id_seq1'::regclass),
    "user_id" int4 NOT NULL,
    "asset_id" int4 NOT NULL,
    "amount" numeric(18,8) NOT NULL,
    "type" varchar(50) NOT NULL,
    "timestamp" timestamp NOT NULL,
    PRIMARY KEY ("transaction_id","timestamp")
);

-- This script only contains the table creation statements and does not fully represent the table in the database. Do not use it as a backup.

-- Sequence and defined type
CREATE SEQUENCE IF NOT EXISTS transactions_transaction_id_seq1;

-- Table Definition
CREATE TABLE "public"."transactions_2025_01" (
    "transaction_id" int4 NOT NULL DEFAULT nextval('transactions_transaction_id_seq1'::regclass),
    "user_id" int4 NOT NULL,
    "asset_id" int4 NOT NULL,
    "amount" numeric(18,8) NOT NULL,
    "type" varchar(50) NOT NULL,
    "timestamp" timestamp NOT NULL,
    PRIMARY KEY ("transaction_id","timestamp")
);

-- This script only contains the table creation statements and does not fully represent the table in the database. Do not use it as a backup.

-- Sequence and defined type
CREATE SEQUENCE IF NOT EXISTS transactions_transaction_id_seq1;

-- Table Definition
CREATE TABLE "public"."transactions_2025_02" (
    "transaction_id" int4 NOT NULL DEFAULT nextval('transactions_transaction_id_seq1'::regclass),
    "user_id" int4 NOT NULL,
    "asset_id" int4 NOT NULL,
    "amount" numeric(18,8) NOT NULL,
    "type" varchar(50) NOT NULL,
    "timestamp" timestamp NOT NULL,
    PRIMARY KEY ("transaction_id","timestamp")
);

-- This script only contains the table creation statements and does not fully represent the table in the database. Do not use it as a backup.

-- Sequence and defined type
CREATE SEQUENCE IF NOT EXISTS transactions_transaction_id_seq1;

-- Table Definition
CREATE TABLE "public"."transactions_2025_03" (
    "transaction_id" int4 NOT NULL DEFAULT nextval('transactions_transaction_id_seq1'::regclass),
    "user_id" int4 NOT NULL,
    "asset_id" int4 NOT NULL,
    "amount" numeric(18,8) NOT NULL,
    "type" varchar(50) NOT NULL,
    "timestamp" timestamp NOT NULL,
    PRIMARY KEY ("transaction_id","timestamp")
);

-- This script only contains the table creation statements and does not fully represent the table in the database. Do not use it as a backup.

-- Sequence and defined type
CREATE SEQUENCE IF NOT EXISTS users_user_id_seq;

-- Table Definition
CREATE TABLE "public"."users" (
    "user_id" int4 NOT NULL DEFAULT nextval('users_user_id_seq'::regclass),
    "name" varchar(100) NOT NULL,
    "email" varchar(100) NOT NULL,
    "password_hash" varchar(255) NOT NULL,
    "created_at" timestamp DEFAULT now(),
    "updated_at" timestamp DEFAULT now(),
    PRIMARY KEY ("user_id")
);



-- Indices
CREATE UNIQUE INDEX assets_symbol_key ON public.assets USING btree (symbol);
CREATE INDEX idx_asset_description ON public.assets USING gin (to_tsvector('english'::regconfig, asset_description));
ALTER TABLE "public"."orders" ADD FOREIGN KEY ("user_id") REFERENCES "public"."users"("user_id") ON DELETE CASCADE;
ALTER TABLE "public"."orders" ADD FOREIGN KEY ("asset_id") REFERENCES "public"."assets"("asset_id") ON DELETE CASCADE;


-- Indices
CREATE INDEX idx_orders_user_id ON public.orders USING btree (user_id);
CREATE INDEX idx_orders_status ON public.orders USING btree (status);
ALTER TABLE "public"."portfolios" ADD FOREIGN KEY ("user_id") REFERENCES "public"."users"("user_id") ON DELETE CASCADE;
ALTER TABLE "public"."portfolios" ADD FOREIGN KEY ("asset_id") REFERENCES "public"."assets"("asset_id") ON DELETE CASCADE;


-- Indices
CREATE INDEX idx_portfolios_user_id ON public.portfolios USING btree (user_id);
CREATE INDEX idx_portfolios_asset_id ON public.portfolios USING btree (asset_id);


-- Indices
CREATE UNIQUE INDEX transactions_pkey1 ON ONLY public.transactions USING btree (transaction_id, "timestamp");
CREATE INDEX idx_user_id ON ONLY public.transactions USING btree (user_id);
CREATE INDEX idx_asset_id ON ONLY public.transactions USING btree (asset_id);
CREATE INDEX idx_timestamp ON ONLY public.transactions USING btree ("timestamp");
CREATE INDEX idx_user_timestamp ON ONLY public.transactions USING btree (user_id, "timestamp");
CREATE INDEX idx_asset_timestamp ON ONLY public.transactions USING btree (asset_id, "timestamp");


-- Indices
CREATE INDEX transactions_2023_01_user_id_idx ON public.transactions_2023_01 USING btree (user_id);
CREATE INDEX transactions_2023_01_asset_id_idx ON public.transactions_2023_01 USING btree (asset_id);
CREATE INDEX transactions_2023_01_timestamp_idx ON public.transactions_2023_01 USING btree ("timestamp");
CREATE INDEX transactions_2023_01_user_id_timestamp_idx ON public.transactions_2023_01 USING btree (user_id, "timestamp");
CREATE INDEX transactions_2023_01_asset_id_timestamp_idx ON public.transactions_2023_01 USING btree (asset_id, "timestamp");


-- Indices
CREATE INDEX transactions_2023_02_user_id_idx ON public.transactions_2023_02 USING btree (user_id);
CREATE INDEX transactions_2023_02_asset_id_idx ON public.transactions_2023_02 USING btree (asset_id);
CREATE INDEX transactions_2023_02_timestamp_idx ON public.transactions_2023_02 USING btree ("timestamp");
CREATE INDEX transactions_2023_02_user_id_timestamp_idx ON public.transactions_2023_02 USING btree (user_id, "timestamp");
CREATE INDEX transactions_2023_02_asset_id_timestamp_idx ON public.transactions_2023_02 USING btree (asset_id, "timestamp");


-- Indices
CREATE INDEX transactions_2025_01_user_id_idx ON public.transactions_2025_01 USING btree (user_id);
CREATE INDEX transactions_2025_01_asset_id_idx ON public.transactions_2025_01 USING btree (asset_id);
CREATE INDEX transactions_2025_01_timestamp_idx ON public.transactions_2025_01 USING btree ("timestamp");
CREATE INDEX transactions_2025_01_user_id_timestamp_idx ON public.transactions_2025_01 USING btree (user_id, "timestamp");
CREATE INDEX transactions_2025_01_asset_id_timestamp_idx ON public.transactions_2025_01 USING btree (asset_id, "timestamp");


-- Indices
CREATE INDEX transactions_2025_02_user_id_idx ON public.transactions_2025_02 USING btree (user_id);
CREATE INDEX transactions_2025_02_asset_id_idx ON public.transactions_2025_02 USING btree (asset_id);
CREATE INDEX transactions_2025_02_timestamp_idx ON public.transactions_2025_02 USING btree ("timestamp");
CREATE INDEX transactions_2025_02_user_id_timestamp_idx ON public.transactions_2025_02 USING btree (user_id, "timestamp");
CREATE INDEX transactions_2025_02_asset_id_timestamp_idx ON public.transactions_2025_02 USING btree (asset_id, "timestamp");


-- Indices
CREATE INDEX transactions_2025_03_user_id_idx ON public.transactions_2025_03 USING btree (user_id);
CREATE INDEX transactions_2025_03_asset_id_idx ON public.transactions_2025_03 USING btree (asset_id);
CREATE INDEX transactions_2025_03_timestamp_idx ON public.transactions_2025_03 USING btree ("timestamp");
CREATE INDEX transactions_2025_03_user_id_timestamp_idx ON public.transactions_2025_03 USING btree (user_id, "timestamp");
CREATE INDEX transactions_2025_03_asset_id_timestamp_idx ON public.transactions_2025_03 USING btree (asset_id, "timestamp");


-- Indices
CREATE UNIQUE INDEX users_email_key ON public.users USING btree (email);
