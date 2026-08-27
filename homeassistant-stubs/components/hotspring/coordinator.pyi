from .const import DOMAIN as DOMAIN, LOGGER as LOGGER, SCAN_INTERVAL as SCAN_INTERVAL
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from hotspring import Spa
from typing import override

type HotSpringConfigEntry = ConfigEntry[HotSpringDataUpdateCoordinator]
class HotSpringDataUpdateCoordinator(DataUpdateCoordinator[Spa]):
    config_entry: HotSpringConfigEntry
    hotspring: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: HotSpringConfigEntry) -> None: ...
    @override
    async def _async_update_data(self) -> Spa: ...
