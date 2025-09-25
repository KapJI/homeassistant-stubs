import logging
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from compit_inext_api import CompitApiConnector as CompitApiConnector, DeviceInstance
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

SCAN_INTERVAL: Incomplete
_LOGGER: logging.Logger
type CompitConfigEntry = ConfigEntry[CompitDataUpdateCoordinator]

class CompitDataUpdateCoordinator(DataUpdateCoordinator[dict[int, DeviceInstance]]):
    connector: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry, connector: CompitApiConnector) -> None: ...
    async def _async_update_data(self) -> dict[int, DeviceInstance]: ...
