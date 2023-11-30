from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections import OrderedDict
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.debounce import Debouncer as Debouncer
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, REQUEST_REFRESH_DEFAULT_IMMEDIATE as REQUEST_REFRESH_DEFAULT_IMMEDIATE, UpdateFailed as UpdateFailed
from typing import Final

_LOGGER: Incomplete
UPDATE_INTERVAL: Final[Incomplete]
REQUEST_REFRESH_COOLDOWN: Final[int]

class APCUPSdCoordinator(DataUpdateCoordinator[OrderedDict[str, str]]):
    _host: Incomplete
    _port: Incomplete
    def __init__(self, hass: HomeAssistant, host: str, port: int) -> None: ...
    @property
    def ups_name(self) -> str | None: ...
    @property
    def ups_model(self) -> str | None: ...
    @property
    def ups_serial_no(self) -> str | None: ...
    @property
    def device_info(self) -> DeviceInfo | None: ...
    async def _async_update_data(self) -> OrderedDict[str, str]: ...
