from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "users" (
    "uuid" UUID NOT NULL  PRIMARY KEY,
    "email" VARCHAR(255) NOT NULL UNIQUE,
    "password_hash" VARCHAR(128),
    "is_admin" BOOL NOT NULL  DEFAULT False,
    "tg_id" BIGINT
);
CREATE TABLE IF NOT EXISTS "short_tg_token" (
    "uuid" UUID NOT NULL  PRIMARY KEY,
    "value" VARCHAR(32) NOT NULL UNIQUE,
    "date" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "user_id" UUID NOT NULL REFERENCES "users" ("uuid") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "resources" (
    "uuid" UUID NOT NULL  PRIMARY KEY,
    "name" VARCHAR(255) NOT NULL UNIQUE,
    "status" VARCHAR(8) NOT NULL  DEFAULT 'OK'
);
COMMENT ON COLUMN "resources"."status" IS 'ok: OK\npartial: partial\ncritical: critical\nddos: ddos';
CREATE TABLE IF NOT EXISTS "subscriptions" (
    "uuid" UUID NOT NULL  PRIMARY KEY,
    "to_telegram" BOOL NOT NULL  DEFAULT False,
    "to_email" BOOL NOT NULL  DEFAULT False,
    "resource_id" UUID NOT NULL REFERENCES "resources" ("uuid") ON DELETE CASCADE,
    "user_id" UUID NOT NULL REFERENCES "users" ("uuid") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "resource_nodes" (
    "uuid" UUID NOT NULL  PRIMARY KEY,
    "url" VARCHAR(255) NOT NULL UNIQUE,
    "resource_id" UUID NOT NULL REFERENCES "resources" ("uuid") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "checks" (
    "uuid" UUID NOT NULL  PRIMARY KEY,
    "expectation" VARCHAR(255) NOT NULL,
    "request_type" VARCHAR(4) NOT NULL,
    "resource_node_id" UUID NOT NULL REFERENCES "resource_nodes" ("uuid") ON DELETE CASCADE
);
COMMENT ON COLUMN "checks"."request_type" IS 'get: GET\npost: POST\nhead: HEAD\nput: PUT';
CREATE TABLE IF NOT EXISTS "check_results" (
    "uuid" UUID NOT NULL  PRIMARY KEY,
    "response" VARCHAR(255) NOT NULL,
    "status" VARCHAR(8) NOT NULL,
    "datetime" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "location" VARCHAR(7) NOT NULL,
    "parent_check_id" UUID NOT NULL REFERENCES "checks" ("uuid") ON DELETE CASCADE
);
COMMENT ON COLUMN "check_results"."status" IS 'ok: OK\npartial: partial\ncritical: critical\nddos: ddos';
COMMENT ON COLUMN "check_results"."location" IS 'russia: RUSSIA\naustria: AUSTRIA\ngermany: GERMANY';
CREATE TABLE IF NOT EXISTS "reviews" (
    "uuid" UUID NOT NULL  PRIMARY KEY,
    "text" VARCHAR(150) NOT NULL,
    "stars" INT NOT NULL,
    "datetime" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "resource_id" UUID NOT NULL REFERENCES "resources" ("uuid") ON DELETE CASCADE,
    "user_id" UUID NOT NULL REFERENCES "users" ("uuid") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "reports" (
    "uuid" UUID NOT NULL  PRIMARY KEY,
    "status" VARCHAR(8) NOT NULL,
    "is_moderated" BOOL NOT NULL  DEFAULT False,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "resource_id" UUID NOT NULL REFERENCES "resources" ("uuid") ON DELETE CASCADE,
    "user_id" UUID NOT NULL REFERENCES "users" ("uuid") ON DELETE CASCADE
);
COMMENT ON COLUMN "reports"."status" IS 'ok: OK\npartial: partial\ncritical: critical\nddos: ddos';
CREATE TABLE IF NOT EXISTS "social_network_reports" (
    "uuid" UUID NOT NULL  PRIMARY KEY,
    "status" VARCHAR(8) NOT NULL,
    "is_moderated" BOOL NOT NULL  DEFAULT False,
    "social_network" VARCHAR(2) NOT NULL,
    "link" VARCHAR(255) NOT NULL,
    "snippet" VARCHAR(512) NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "resource_id" UUID NOT NULL REFERENCES "resources" ("uuid") ON DELETE CASCADE
);
COMMENT ON COLUMN "social_network_reports"."status" IS 'ok: OK\npartial: partial\ncritical: critical\nddos: ddos';
COMMENT ON COLUMN "social_network_reports"."social_network" IS 'vk: VK\nok: OK';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
