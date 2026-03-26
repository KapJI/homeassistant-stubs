from .const import CONF_CITY as CONF_CITY, LOGGER as LOGGER
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_COUNTRY as CONF_COUNTRY, CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE, CONF_STATE as CONF_STATE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pyairvisual.cloud_api import CloudAPI as CloudAPI
from typing import Any

type AirVisualConfigEntry = ConfigEntry[AirVisualDataUpdateCoordinator]
class AirVisualDataUpdateCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    config_entry: AirVisualConfigEntry
    _cloud_api: Incomplete
    def __init__(self, hass: HomeAssistant, entry: AirVisualConfigEntry, cloud_api: CloudAPI, name: str) -> None: ...
    async def _async_update_data(self) -> dict[str, Any]: ...
