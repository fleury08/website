import asyncio
import logging
from datetime import datetime

from starlette.websockets import WebSocket, WebSocketState


class ConnectionManager:

    def __init__(self) -> None:
        self.connections = {}
        self.received_messages = {}  # session_id: queue

    async def connect(self, session_id: str, websocket: WebSocket):
        await websocket.accept()
        self.connections[session_id] = websocket
        self.received_messages[session_id] = asyncio.Queue()
        await self.send_message(
            session_id,
            {
                "message": "connected",
                "session_id": session_id,
                "from": "server",
                "timestamp": datetime.now().isoformat(),
            },
        )


    async def get_received_message(self, session_id):
        if not session_id:
            raise ValueError("Invalid session id")

        if session_id not in self.connections:
            raise KeyError(f"Session id {session_id} not found")

        return await self.received_messages[session_id].get()

    async def queue_received_message(self, session_id, message):
        if not session_id:
            raise ValueError("Invalid session id")

        if session_id not in self.connections:
            raise KeyError(f"Session id {session_id} not found")

        await self.received_messages[session_id].put(message)

    async def disconnect(self, session_id):
        websocket: WebSocket = self.connections[session_id]
        if websocket.client_state != WebSocketState.DISCONNECTED:
            await websocket.close()
        self.connections[session_id] = None
        del self.connections[session_id]

    async def broadcast(self, message):
        for session_id in self.connections:
            await self.send_message(session_id, message)
        return {"session_ids": list(self.connections.keys()), "message": message}

    async def send_messages(self, session_ids, message):
        for session_id in session_ids:
            await self.send_message(session_id, message)

    async def send_message(self, session_id, message):
        websocket: WebSocket = self.connections[session_id]
        if (
                websocket is not None
                and websocket.client_state != WebSocketState.DISCONNECTED
        ):
            logging.getLogger(__name__).info(
                f"sending message to {session_id} : {message}"
            )
            await websocket.send_json(message)
        else:
            logging.getLogger(__name__).error(
                f"cannot send message to {session_id} : {message}"
            )


ws_conn_manager = ConnectionManager()
