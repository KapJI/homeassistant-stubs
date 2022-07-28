from .const import DOMAIN as DOMAIN
from .coordinator import TailscaleDataUpdateCoordinator as TailscaleDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from tailscale import Device as TailscaleDevice

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class TailscaleEntity(CoordinatorEntity):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    device_id: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, *, coordinator: DataUpdateCoordinator, device: TailscaleDevice, description: EntityDescription) -> None: ...
    @property
    def device_info(self) -> DeviceInfo: ...
