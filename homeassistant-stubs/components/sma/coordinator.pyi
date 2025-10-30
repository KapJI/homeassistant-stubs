from .const import DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL, DOMAIN as DOMAIN
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pysma import SMAWebConnect as SMAWebConnect
from pysma.helpers import DeviceInfo
from pysma.sensor import Sensors

_LOGGER: Incomplete

@dataclass(slots=True)
class SMACoordinatorData:
    sma_device_info: DeviceInfo
    sensors: Sensors

class SMADataUpdateCoordinator(DataUpdateCoordinator[SMACoordinatorData]):
    config_entry: ConfigEntry
    sma: Incomplete
    _sma_device_info: Incomplete
    _sensors: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry, sma: SMAWebConnect) -> None: ...
    async def _async_setup(self) -> None: ...
    async def _async_update_data(self) -> SMACoordinatorData: ...
    async def async_close_sma_session(self) -> None: ...
