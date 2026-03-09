from cmd_manager import BaseCommand, Argument

from app.commands.base import AsyncBaseCommand


class Command(AsyncBaseCommand):
    def get_arguments(self):
        return [
            Argument('--name', is_argument=False, required=True),
            Argument('--token', is_argument=False, required=True),
        ]
    async def async_run(self, *args, **kwargs):
        name, token = kwargs['name'], kwargs['token']
        saved_token = await self.container.command_service.create_primary_token(name, token)
        if saved_token is None:
            print("token already exist")