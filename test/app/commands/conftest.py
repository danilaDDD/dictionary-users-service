import pytest
import pytest_asyncio

from app.commands.container import DIContainer
from app.db.session_manager import SessionManager


@pytest.fixture(scope='session')
def container():
    return DIContainer()

@pytest_asyncio.fixture(scope="function", autouse=True)
async def clean_db_before_test(session_manager: SessionManager):
    async with session_manager.start_with_commit() as open_session_manager:
        await open_session_manager.users.delete_all()
        await open_session_manager.primary_tokens.delete_all()

    yield