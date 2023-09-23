from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
import os

#config your database
DB_USER = os.getenv("DB_USER", "default")
DB_PASSWORD = os.getenv("DB_PASSWORD", "9kViT4vGCrPa")
DB_NAME = os.getenv("DB_NAME", "verceldb")
DB_HOST = os.getenv("DB_HOST", "ep-late-hat-19016131-pooler.ap-southeast-1.postgres.vercel-storage.com")
DB_CONFIG = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"


class AsyncDatabaseSession:

    def __init__(self):
        self.session = None
        self.engine = None

    def __getattr__(self, name):
        return getattr(self.session, name)

    def init(self):
        self.engine = create_async_engine(DB_CONFIG, future=True, echo=True)
        self.session = sessionmaker(self.engine, expire_on_commit=False, class_=AsyncSession)()

    async def create_all(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)


db = AsyncDatabaseSession()


async def commit_rollback():
    try:
        await db.commit()
    except Exception:
        await db.rollback()
        raise
