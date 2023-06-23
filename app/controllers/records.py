from pydantic import UUID4
from sqlalchemy import Sequence
from starlite import Controller, get, post
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import CreateRecordDTO, add_record, get_weekly_leaderboard

from app.models import Record


class RecordController(Controller):
    path = "/records"

    @post()
    async def create_record(self, data: CreateRecordDTO, async_session: AsyncSession) -> Record:
        return add_record(data, async_session)

    @get()
    async def list_users(self) -> list[Record]:
        ...

    @get(path="/{record_id:int}")
    async def get_record(self, record_id: int) -> Record:
        ...

    @get()
    async def get_weekly_leaderboard(self, async_session: AsyncSession) -> Sequence[Record]:
        return get_weekly_leaderboard(async_session)
