import asyncio
from .const import DOMAIN as DOMAIN
from .entry_data import ESPHomeConfigEntry as ESPHomeConfigEntry
from _typeshed import Incomplete
from aioesphomeapi import APIClient as APIClient
from collections.abc import Callable as Callable
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, async_get_hass as async_get_hass, callback as callback
from serialx.platforms.serial_esphome import ESPHomeSerial, ESPHomeSerialTransport
from yarl import URL

_HASS_LOOP: asyncio.AbstractEventLoop | None

def build_url(entry_id: str, port_name: str) -> URL: ...
async def _resolve_client(entry_id: str) -> APIClient: ...

class HassESPHomeSerial(ESPHomeSerial):
    _api: APIClient | None
    _path: str | None
    _port_name: Incomplete
    _client_loop: Incomplete
    async def _async_open(self) -> None: ...

class HassESPHomeSerialTransport(ESPHomeSerialTransport):
    transport_name: str
    _serial_cls = HassESPHomeSerial

def register_serialx_transport(loop: asyncio.AbstractEventLoop) -> Callable[[Event], None]: ...
