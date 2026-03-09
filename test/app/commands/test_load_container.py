from app.commands.container import DIContainer


def test_load_container(container: DIContainer):
    settings = container.settings
    assert settings is not None
    assert "test" in settings.DB_NAME