import asyncio
from . import OnkyoConfigEntry as OnkyoConfigEntry
from .const import DEVICE_DISCOVERY_TIMEOUT as DEVICE_DISCOVERY_TIMEOUT, DEVICE_INTERVIEW_TIMEOUT as DEVICE_INTERVIEW_TIMEOUT, ZONES as ZONES
from _typeshed import Incomplete
from aioonkyo import Instruction as Instruction, Receiver as Receiver, ReceiverInfo as ReceiverInfo, Status as Status
from collections.abc import Awaitable, Callable as Callable, Iterable
from dataclasses import dataclass, field
from homeassistant.components import network as network
from homeassistant.core import HomeAssistant as HomeAssistant

_LOGGER: Incomplete

@dataclass
class Callbacks:
    connect: list[Callable[[bool], Awaitable[None]]] = field(default_factory=list)
    update: list[Callable[[Status], Awaitable[None]]] = field(default_factory=list)
    def clear(self) -> None: ...

class ReceiverManager:
    hass: HomeAssistant
    entry: OnkyoConfigEntry
    info: ReceiverInfo
    receiver: Receiver | None
    callbacks: Callbacks
    _started: asyncio.Event
    def __init__(self, hass: HomeAssistant, entry: OnkyoConfigEntry, info: ReceiverInfo) -> None: ...
    async def start(self) -> Awaitable[None] | None: ...
    async def _run(self) -> None: ...
    async def on_connect(self, reconnect: bool) -> None: ...
    async def on_update(self, message: Status) -> None: ...
    async def write(self, message: Instruction) -> None: ...
    def start_unloading(self) -> None: ...

async def async_interview(host: str) -> ReceiverInfo: ...
async def async_discover(hass: HomeAssistant) -> Iterable[ReceiverInfo]: ...
