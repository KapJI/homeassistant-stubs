from .const import DATA_ACCOUNT as DATA_ACCOUNT, DATA_COORDINATOR as DATA_COORDINATOR, DOMAIN as DOMAIN, LOGGER as LOGGER, SENSOR_TYPE_NEXT_PICKUP as SENSOR_TYPE_NEXT_PICKUP
from aioridwell.model import RidwellAccount as RidwellAccount, RidwellPickupEvent as RidwellPickupEvent
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any

DEFAULT_UPDATE_INTERVAL: Any
PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class RidwellEntity(CoordinatorEntity):
    _account: Any
    _attr_unique_id: Any
    entity_description: Any
    def __init__(self, coordinator: DataUpdateCoordinator, account: RidwellAccount, description: EntityDescription) -> None: ...
