import asyncio
import websockets

class ChatClient:
    def __init__(self, uri, nickname, on_message, on_error=None):
        self.uri = uri
        self.nickname = nickname
        self.on_message = on_message
        self.on_error = on_error
        self.loop = asyncio.new_event_loop()
        self.ws = None

    def start(self):
        asyncio.set_event_loop(self.loop)
        self.loop.run_until_complete(self.connect())

    async def connect(self):
        try:
            self.ws = await websockets.connect(self.uri)
            await self.ws.send(self.nickname)
            await self.receive()

        except Exception as e:
            if self.on_error:
                self.on_error(str(e))

    async def receive(self):
        while True:
            msg = await self.ws.recv()
            self.on_message(msg)

    def send(self, msg):
        asyncio.run_coroutine_threadsafe(
            self.ws.send(msg),
            self.loop
        )