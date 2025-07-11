from channels.generic.websocket import AsyncWebsocketConsumer
import json

class PoseConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps({"msg": "WebSocket Connected"}))
