from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "resources" ADD "status" VARCHAR(8) NOT NULL  DEFAULT 'OK';
        ALTER TABLE "check_results" ALTER COLUMN "status" TYPE VARCHAR(8) USING "status"::VARCHAR(8);
        ALTER TABLE "reports" ALTER COLUMN "status" TYPE VARCHAR(8) USING "status"::VARCHAR(8);
        ALTER TABLE "social_network_reports" ALTER COLUMN "status" TYPE VARCHAR(8) USING "status"::VARCHAR(8);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "reports" ALTER COLUMN "status" TYPE VARCHAR(8) USING "status"::VARCHAR(8);
        ALTER TABLE "resources" DROP COLUMN "status";
        ALTER TABLE "check_results" ALTER COLUMN "status" TYPE VARCHAR(8) USING "status"::VARCHAR(8);
        ALTER TABLE "social_network_reports" ALTER COLUMN "status" TYPE VARCHAR(8) USING "status"::VARCHAR(8);"""
