from .common import SynoApi as SynoApi
from .const import DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL, SIGNAL_CAMERA_SOURCE_CHANGED as SIGNAL_CAMERA_SOURCE_CHANGED, SYNOLOGY_CONNECTION_EXCEPTIONS as SYNOLOGY_CONNECTION_EXCEPTIONS
from _typeshed import Incomplete
from datetime import timedelta
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from synology_dsm.api.surveillance_station.camera import SynoCamera
from typing import Any, TypeVar

_LOGGER: Incomplete
_DataT = TypeVar('_DataT')

class SynologyDSMUpdateCoordinator(DataUpdateCoordinator[_DataT]):
    api: Incomplete
    entry: Incomplete
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry, api: SynoApi, update_interval: timedelta) -> None: ...

class SynologyDSMSwitchUpdateCoordinator(SynologyDSMUpdateCoordinator[dict[str, dict[str, Any]]]):
    version: Incomplete
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry, api: SynoApi) -> None: ...
    async def async_setup(self) -> None: ...
    async def _async_update_data(self) -> dict[str, dict[str, Any]]: ...

class SynologyDSMCentralUpdateCoordinator(SynologyDSMUpdateCoordinator[None]):
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry, api: SynoApi) -> None: ...
    async def _async_update_data(self) -> None: ...

class SynologyDSMCameraUpdateCoordinator(SynologyDSMUpdateCoordinator[dict[str, dict[str, SynoCamera]]]):
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry, api: SynoApi) -> None: ...
    async def _async_update_data(self) -> dict[str, dict[str, SynoCamera]]: ...
