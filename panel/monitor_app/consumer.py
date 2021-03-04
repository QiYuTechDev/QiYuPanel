import asyncio
import random

from channels.generic.websocket import AsyncJsonWebsocketConsumer
from websockets.exceptions import ConnectionClosed

__all__ = ["CpuMonitorConsumer"]


class CpuMonitorConsumer(AsyncJsonWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._closed = False

    async def connect(self):
        await super().connect()
        while True:
            try:
                await self.send_json({"hello": random.random()})
                await asyncio.sleep(1)
                if self._closed:
                    return
            except ConnectionClosed:
                self._closed = True
                return

    async def disconnect(self, code):
        self._closed = True
