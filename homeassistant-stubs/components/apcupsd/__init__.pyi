from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.util import Throttle as Throttle
from typing import Any, Final

_LOGGER: Incomplete
DOMAIN: Final[str]
VALUE_ONLINE: Final[int]
PLATFORMS: Final[Incomplete]
MIN_TIME_BETWEEN_UPDATES: Final[Incomplete]
CONFIG_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class APCUPSdData:
    _host: Incomplete
    _port: Incomplete
    status: Incomplete
    def __init__(self, host: str, port: int) -> None: ...
    @property
    def name(self) -> str | None: ...
    @property
    def model(self) -> str | None: ...
    @property
    def serial_no(self) -> str | None: ...
    @property
    def statflag(self) -> str | None: ...
    @property
    def device_info(self) -> DeviceInfo | None: ...
    def update(self, **kwargs: Any) -> None: ...
