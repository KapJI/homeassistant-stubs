from .host import ReolinkHost as ReolinkHost
from _typeshed import Incomplete
from datetime import timedelta
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigEntryState as ConfigEntryState
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete
NUM_CRED_ERRORS: int
DEVICE_UPDATE_INTERVAL_MIN: Incomplete
DEVICE_UPDATE_INTERVAL_PER_CAM: Incomplete

class ReolinkCoordinator(DataUpdateCoordinator[None]):
    config_entry: ConfigEntry
    _host: Incomplete
    _min_timeout: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry, host: ReolinkHost, name: str, *, min_timeout: float, update_interval: timedelta | None) -> None: ...

class ReolinkDeviceCoordinator(ReolinkCoordinator):
    _update_timeout: Incomplete
    _last_known_firmware: dict[int | None, str | None]
    firmware_coordinator: ReolinkFirmwareCoordinator | None
    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry, host: ReolinkHost, *, min_timeout: float) -> None: ...
    async def _async_update_data(self) -> None: ...

class ReolinkFirmwareCoordinator(ReolinkCoordinator):
    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry, host: ReolinkHost, *, min_timeout: float) -> None: ...
    async def _async_update_data(self) -> None: ...
