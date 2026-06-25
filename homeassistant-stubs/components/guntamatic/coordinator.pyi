from .const import DOMAIN as DOMAIN, SCAN_INTERVAL as SCAN_INTERVAL
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import override

_LOGGER: Incomplete
type GuntamaticConfigEntry = ConfigEntry[GuntamaticCoordinator]

class GuntamaticCoordinator(DataUpdateCoordinator[dict[str, list[str]]]):
    heater: Incomplete
    def __init__(self, hass: HomeAssistant, entry: GuntamaticConfigEntry) -> None: ...
    @override
    async def _async_update_data(self) -> dict[str, list[str]]: ...
