import os

import pytest
import pytest_asyncio
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from app.testutils.asserts import AssertsToken

from app.testutils.asserts import AssertsResponse
from app.db.connection import create_session_factory
from app.db.session_manager import SessionManager
from settings.settings import load_settings, Settings


@pytest.fixture(scope="session", autouse=True)
def setup_all():
    os.environ['ENV'] = 'test'
    yield

@pytest.fixture(scope="session")
def settings() -> Settings:
    return load_settings()

@pytest.fixture(scope="session")
def session_factory(settings) -> async_sessionmaker[AsyncSession]:
    return create_session_factory(settings)

@pytest_asyncio.fixture(scope="session")
async def session_manager(session_factory) -> SessionManager:
    return SessionManager(session_factory)

@pytest.fixture(scope="module")
def asserts_token(settings: Settings) -> AssertsToken:
    return AssertsToken.from_settings(settings)


@pytest.fixture(scope="module")
def asserts_response() -> AssertsResponse:
    return AssertsResponse()