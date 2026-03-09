from app.services.command_service import CommandService
from db.connection import create_session_factory
from db.session_manager import SessionManager
from settings.settings import Settings, load_settings


class DIContainer:
    def __init__(self):
        self.settings = load_settings()
        self.session_factory = create_session_factory(self.settings)
        self.session_manager = SessionManager(self.session_factory)
        self.command_service = CommandService(self.session_manager)