from app.models.models import PrimaryToken
from app.repositories.base import BaseRepository


class PrimaryTokenRepository(BaseRepository):
    model = PrimaryToken

    async def find_by_token(self, token: str) -> PrimaryToken | None:
        stmt = self.select().where(self.model.token == token)
        return await self.get_one_or_none(stmt)

    async def find_by_name(self, name: str) -> PrimaryToken | None:
        stmt = self.select().where(self.model.name == name)
        return await self.get_one_or_none(stmt)