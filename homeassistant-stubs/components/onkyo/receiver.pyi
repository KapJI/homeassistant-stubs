import pyeiscp
from .const import DEVICE_DISCOVERY_TIMEOUT as DEVICE_DISCOVERY_TIMEOUT, DEVICE_INTERVIEW_TIMEOUT as DEVICE_INTERVIEW_TIMEOUT, ZONES as ZONES
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Iterable
from dataclasses import dataclass
from typing import Any

_LOGGER: Incomplete

@dataclass
class Callbacks:
    connect: list[Callable[[Receiver], None]] = ...
    update: list[Callable[[Receiver, tuple[str, str, Any]], None]] = ...
    def __init__(self, connect=..., update=...) -> None: ...

@dataclass
class Receiver:
    conn: pyeiscp.Connection
    model_name: str
    identifier: str
    host: str
    first_connect: bool = ...
    callbacks: Callbacks = ...
    @classmethod
    async def async_create(cls, info: ReceiverInfo) -> Receiver: ...
    def on_connect(self) -> None: ...
    def on_update(self, message: tuple[str, str, Any]) -> None: ...
    def __init__(self, conn, model_name, identifier, host, first_connect=..., callbacks=...) -> None: ...

@dataclass
class ReceiverInfo:
    host: str
    port: int
    model_name: str
    identifier: str
    def __init__(self, host, port, model_name, identifier) -> None: ...

async def async_interview(host: str) -> ReceiverInfo | None: ...
async def async_discover() -> Iterable[ReceiverInfo]: ...
