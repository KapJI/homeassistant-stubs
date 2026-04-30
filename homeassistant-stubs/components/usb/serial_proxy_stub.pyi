from collections.abc import Callable as Callable
from homeassistant.core import Event as Event, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from serialx.platforms.serial_esphome import ESPHomeSerial, ESPHomeSerialTransport

class HassESPHomeSerialStub(ESPHomeSerial):
    async def _async_open(self) -> None: ...

class HassESPHomeSerialStubTransport(ESPHomeSerialTransport):
    transport_name: str
    _serial_cls = HassESPHomeSerialStub

def register_serialx_transport() -> Callable[[Event], None]: ...
