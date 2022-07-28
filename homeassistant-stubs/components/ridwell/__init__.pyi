from .const import DOMAIN as DOMAIN, LOGGER as LOGGER, SENSOR_TYPE_NEXT_PICKUP as SENSOR_TYPE_NEXT_PICKUP
from _typeshed import Incomplete
from aioridwell.model import RidwellAccount as RidwellAccount, RidwellPickupEvent as RidwellPickupEvent
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

DEFAULT_UPDATE_INTERVAL: Incomplete
PLATFORMS: list[Platform]

class RidwellData:
    accounts: dict[str, RidwellAccount]
    coordinator: DataUpdateCoordinator
    def __init__(self, accounts, coordinator) -> None: ...

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class RidwellEntity(CoordinatorEntity):
    _attr_has_entity_name: bool
    _account: Incomplete
    _attr_unique_id: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: DataUpdateCoordinator, account: RidwellAccount, description: EntityDescription) -> None: ...
