from datetime import datetime, timedelta
import os
from sqlalchemy import Sequence, func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import NoResultFound
from starlite import DTOFactory
from starlite.plugins.sql_alchemy import SQLAlchemyConfig, SQLAlchemyPlugin
from app.models import Record

sqlalchemy_config = SQLAlchemyConfig(
    connection_string=f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}:5432/postgres", dependency_key="async_session"
)
sqlalchemy_plugin = SQLAlchemyPlugin(config=sqlalchemy_config)
dto_factory = DTOFactory(plugins=[sqlalchemy_plugin])

CreateRecordDTO = dto_factory("CreateRecordDTO", Record, exclude=["id"])


async def db_startup() -> None:
    """Initialize the database."""
    async with sqlalchemy_config.engine.begin() as conn:  # type: ignore
        await conn.run_sync(Record)  # pyright: ignore


async def add_record(data: CreateRecordDTO, async_session: AsyncSession) -> Record:
    record: Record = data.to_model_instance()
    async_session.add(record)
    await async_session.commit()
    return record


async def get_record(record_id: int, async_session: AsyncSession) -> Record:
    result = await async_session.scalars(select(Record).where(Record.id == record_id))
    record: Record | None = result.one_or_none()
    if not record:
        raise NoResultFound(f"No entry found for id: {record_id}")
    return record


async def get_weekly_leaderboard(async_session: AsyncSession) -> Sequence[Record]:
    now = datetime.utcnow()
    start = now - timedelta(days=now.weekday)
    end = start + timedelta(days=6)
    result = await async_session.scalars(select(Record).where(Record.created_at.between(start.date(), end.date())))
    records: Record | None = result.all()
    if not records:
        raise NoResultFound(f"No entries found")
    return records
