from .const import DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from .coordinator import TautulliDataUpdateCoordinator as TautulliDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_URL as CONF_URL, CONF_VERIFY_SSL as CONF_VERIFY_SSL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from pytautulli import PyTautulliApiUser as PyTautulliApiUser

PLATFORMS: Incomplete
TautulliConfigEntry = ConfigEntry[TautulliDataUpdateCoordinator]

async def async_setup_entry(hass: HomeAssistant, entry: TautulliConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: TautulliConfigEntry) -> bool: ...

class TautulliEntity(CoordinatorEntity[TautulliDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    entity_description: Incomplete
    user: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: TautulliDataUpdateCoordinator, description: EntityDescription, user: PyTautulliApiUser | None = None) -> None: ...
