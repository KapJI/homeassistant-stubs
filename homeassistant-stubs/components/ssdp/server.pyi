from .common import async_build_source_set as async_build_source_set
from _typeshed import Incomplete
from async_upnp_client.const import AddressTupleVXType as AddressTupleVXType
from async_upnp_client.server import UpnpServer, UpnpServerDevice, UpnpServerService as UpnpServerService
from homeassistant.const import EVENT_HOMEASSISTANT_STARTED as EVENT_HOMEASSISTANT_STARTED, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant
from homeassistant.helpers.network import NoURLAvailableError as NoURLAvailableError, get_url as get_url
from homeassistant.helpers.system_info import async_get_system_info as async_get_system_info
from typing import Any

UPNP_SERVER_MIN_PORT: int
UPNP_SERVER_MAX_PORT: int
_LOGGER: Incomplete

class HassUpnpServiceDevice(UpnpServerDevice):
    DEVICE_DEFINITION: Incomplete
    EMBEDDED_DEVICES: list[type[UpnpServerDevice]]
    SERVICES: list[type[UpnpServerService]]

async def _async_find_next_available_port(source: AddressTupleVXType) -> int: ...

class Server:
    hass: Incomplete
    _upnp_servers: list[UpnpServer]
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_start(self) -> None: ...
    async def _async_get_instance_udn(self) -> str: ...
    async def _async_start_upnp_servers(self, event: Event) -> None: ...
    async def async_stop(self, *_: Any) -> None: ...
    async def _async_stop_upnp_servers(self) -> None: ...
