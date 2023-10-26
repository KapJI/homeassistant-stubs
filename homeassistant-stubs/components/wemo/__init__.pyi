import pywemo
from .const import DOMAIN as DOMAIN
from .models import WemoConfigEntryData as WemoConfigEntryData, WemoData as WemoData, async_wemo_data as async_wemo_data
from .wemo_device import DeviceCoordinator as DeviceCoordinator, async_register_device as async_register_device
from _typeshed import Incomplete
from collections.abc import Callable, Coroutine, Sequence
from datetime import datetime
from homeassistant import config_entries as config_entries
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DISCOVERY as CONF_DISCOVERY, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.event import async_call_later as async_call_later
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.async_ import gather_with_limited_concurrency as gather_with_limited_concurrency
from typing import Any

MAX_CONCURRENCY: int
WEMO_MODEL_DISPATCH: Incomplete
_LOGGER: Incomplete
DispatchCallback = Callable[[DeviceCoordinator], Coroutine[Any, Any, None]]
HostPortTuple: Incomplete

def coerce_host_port(value: str) -> HostPortTuple: ...

CONF_STATIC: str
DEFAULT_DISCOVERY: bool
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_wemo_dispatcher_connect(hass: HomeAssistant, dispatch: DispatchCallback) -> None: ...

class WemoDispatcher:
    _config_entry: Incomplete
    _added_serial_numbers: Incomplete
    _failed_serial_numbers: Incomplete
    _dispatch_backlog: Incomplete
    _dispatch_callbacks: Incomplete
    def __init__(self, config_entry: ConfigEntry) -> None: ...
    async def async_add_unique_device(self, hass: HomeAssistant, wemo: pywemo.WeMoDevice) -> None: ...
    async def async_connect_platform(self, platform: Platform, dispatch: DispatchCallback) -> None: ...
    async def async_unload_platforms(self, hass: HomeAssistant) -> bool: ...

class WemoDiscovery:
    ADDITIONAL_SECONDS_BETWEEN_SCANS: int
    MAX_SECONDS_BETWEEN_SCANS: int
    _hass: Incomplete
    _wemo_dispatcher: Incomplete
    _stop: Incomplete
    _scan_delay: int
    _static_config: Incomplete
    def __init__(self, hass: HomeAssistant, wemo_dispatcher: WemoDispatcher, static_config: Sequence[HostPortTuple]) -> None: ...
    async def async_discover_and_schedule(self, event_time: datetime | None = ...) -> None: ...
    def async_stop_discovery(self) -> None: ...
    async def discover_statics(self) -> None: ...

def validate_static_config(host: str, port: int | None) -> pywemo.WeMoDevice | None: ...
