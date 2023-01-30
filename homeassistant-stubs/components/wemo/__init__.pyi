import pywemo
from .const import DOMAIN as DOMAIN
from .wemo_device import async_register_device as async_register_device
from _typeshed import Incomplete
from collections.abc import Sequence
from datetime import datetime
from homeassistant import config_entries as config_entries
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DISCOVERY as CONF_DISCOVERY, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.event import async_call_later as async_call_later
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.async_ import gather_with_concurrency as gather_with_concurrency

MAX_CONCURRENCY: int
WEMO_MODEL_DISPATCH: Incomplete
_LOGGER: Incomplete
HostPortTuple: Incomplete

def coerce_host_port(value: str) -> HostPortTuple: ...

CONF_STATIC: str
DEFAULT_DISCOVERY: bool
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class WemoDispatcher:
    _config_entry: Incomplete
    _added_serial_numbers: Incomplete
    _loaded_platforms: Incomplete
    def __init__(self, config_entry: ConfigEntry) -> None: ...
    async def async_add_unique_device(self, hass: HomeAssistant, wemo: pywemo.WeMoDevice) -> None: ...

class WemoDiscovery:
    ADDITIONAL_SECONDS_BETWEEN_SCANS: int
    MAX_SECONDS_BETWEEN_SCANS: int
    _hass: Incomplete
    _wemo_dispatcher: Incomplete
    _stop: Incomplete
    _scan_delay: int
    _static_config: Incomplete
    def __init__(self, hass: HomeAssistant, wemo_dispatcher: WemoDispatcher, static_config: Sequence[HostPortTuple]) -> None: ...
    async def async_discover_and_schedule(self, event_time: Union[datetime, None] = ...) -> None: ...
    def async_stop_discovery(self) -> None: ...
    async def discover_statics(self) -> None: ...

def validate_static_config(host: str, port: Union[int, None]) -> Union[pywemo.WeMoDevice, None]: ...
