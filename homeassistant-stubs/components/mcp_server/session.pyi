from _typeshed import Incomplete
from anyio.streams.memory import MemoryObjectSendStream as MemoryObjectSendStream
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from dataclasses import dataclass
from mcp import types as types

_LOGGER: Incomplete

@dataclass
class Session:
    read_stream_writer: MemoryObjectSendStream[types.JSONRPCMessage | Exception]

class SessionManager:
    _sessions: dict[str, Session]
    def __init__(self) -> None: ...
    @asynccontextmanager
    async def create(self, session: Session) -> AsyncGenerator[str]: ...
    def get(self, session_id: str) -> Session | None: ...
    def close(self) -> None: ...
