from .const import ACCOUNT_ID as ACCOUNT_ID, SCAN_INTERVAL as SCAN_INTERVAL
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_IP_ADDRESS as CONF_IP_ADDRESS, CONF_PASSWORD as CONF_PASSWORD, CONF_TOKEN as CONF_TOKEN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any

_LOGGER: Incomplete
type AdaxConfigEntry = ConfigEntry[AdaxCloudCoordinator | AdaxLocalCoordinator]

class AdaxCloudCoordinator(DataUpdateCoordinator[dict[str, dict[str, Any]]]):
    adax_data_handler: Incomplete
    def __init__(self, hass: HomeAssistant, entry: AdaxConfigEntry) -> None: ...
    async def _async_update_data(self) -> dict[str, dict[str, Any]]: ...

class AdaxLocalCoordinator(DataUpdateCoordinator[dict[str, Any] | None]):
    adax_data_handler: Incomplete
    def __init__(self, hass: HomeAssistant, entry: AdaxConfigEntry) -> None: ...
    async def _async_update_data(self) -> dict[str, Any]: ...
