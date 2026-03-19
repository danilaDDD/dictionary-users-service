import pytest

from app.commands.container import DIContainer
from app.models.models import PrimaryToken
from app.db.session_manager import SessionManager


@pytest.mark.asyncio
@pytest.mark.e2e
class TestCreatePrimaryTokenCommand:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, container: DIContainer, session_manager: SessionManager):
        self.container = container
        self.session_manager = session_manager
        self.command_service = self.container.command_service

    async def test_with_not_exist_token_should_created(self):
        name = "name"
        token = "jhhdhhdsjhjs"

        await self.command_service.create_primary_token(name, token)

        async with self.session_manager.start_without_commit() as session:
            primary_tokens = await session.primary_tokens.get_all()
            assert len(primary_tokens) == 1
            primary_token = primary_tokens[0]
            assert primary_token.name == name
            assert primary_token.token == token

    async def test_with_exist_token_should_return_none(self):
        name = "name"

        async with self.session_manager.start_with_commit() as session:
            primary_token = PrimaryToken(name=name, token="ueyryuey")
            await session.primary_tokens.save(primary_token)


        saved = await self.command_service.create_primary_token(name, token="uyueyureyuer")
        assert saved is None


