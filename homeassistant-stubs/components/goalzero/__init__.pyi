from .const import ATTRIBUTION as ATTRIBUTION, DATA_KEY_API as DATA_KEY_API, DATA_KEY_COORDINATOR as DATA_KEY_COORDINATOR, DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER, MIN_TIME_BETWEEN_UPDATES as MIN_TIME_BETWEEN_UPDATES
from goalzero import Yeti
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_ATTRIBUTION as ATTR_ATTRIBUTION, ATTR_MODEL as ATTR_MODEL, CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any

_LOGGER: Any
PLATFORMS: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class YetiEntity(CoordinatorEntity):
    _attr_extra_state_attributes: Any
    api: Any
    _name: Any
    _server_unique_id: Any
    def __init__(self, api: Yeti, coordinator: DataUpdateCoordinator, name: str, server_unique_id: str) -> None: ...
    @property
    def device_info(self) -> DeviceInfo: ...
