from app.models.models import PrimaryToken
from db.session_manager import SessionManager


class CommandService:
    def __init__(self, session_manager: SessionManager):
        self.session_manager = session_manager

    async def create_primary_token(self, name: str, token: str) -> PrimaryToken | None:
        async with self.session_manager.start_with_commit() as session:
            exist_token = await session.primary_tokens.find_by_name(name)

            if exist_token:
                return None

            return await session.primary_tokens.save(PrimaryToken(name=name, token=token))


