from .const import DOMAIN as DOMAIN
from .coordinator import EvilGeniusUpdateCoordinator as EvilGeniusUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

PLATFORMS: Incomplete
UPDATE_INTERVAL: int

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class EvilGeniusEntity(CoordinatorEntity[EvilGeniusUpdateCoordinator]):
    _attr_has_entity_name: bool
    @property
    def device_info(self) -> DeviceInfo: ...
