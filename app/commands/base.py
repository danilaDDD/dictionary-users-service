import abc
import asyncio
import sys
from abc import ABCMeta, ABC

from cmd_manager import BaseCommand

from app.commands.container import DIContainer


class AsyncBaseCommand(BaseCommand, ABC):
    __abstract__ = ABCMeta
    """Базовый класс для асинхронных команд"""

    def run(self, *args, **kwargs):
        """Синхронная обертка для асинхронного метода"""
        self.container = DIContainer()

        try:
            # Пытаемся получить существующий event loop
            loop = asyncio.get_event_loop()
        except RuntimeError:
            # Если нет event loop, создаем новый
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

        try:
            return loop.run_until_complete(self.async_run(*args, **kwargs))
        finally:
            loop.close()

    @abc.abstractmethod
    async def async_run(self, *args, **kwargs):
        """Асинхронный метод, который нужно переопределить"""
        raise NotImplementedError("Subclasses must implement async_run method")