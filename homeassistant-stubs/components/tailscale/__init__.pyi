from .const import DOMAIN as DOMAIN
from .coordinator import TailscaleDataUpdateCoordinator as TailscaleDataUpdateCoordinator
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from tailscale import Device as TailscaleDevice
from typing import Any

PLATFORMS: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class TailscaleEntity(CoordinatorEntity):
    entity_description: Any
    device_id: Any
    friendly_name: Any
    _attr_name: Any
    _attr_unique_id: Any
    def __init__(self, coordinator: DataUpdateCoordinator, device: TailscaleDevice, description: EntityDescription) -> None: ...
    @property
    def device_info(self) -> DeviceInfo: ...
