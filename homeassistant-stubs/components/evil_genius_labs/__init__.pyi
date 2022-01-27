import pyevilgenius
from .const import DOMAIN as DOMAIN
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import aiohttp_client as aiohttp_client, update_coordinator as update_coordinator
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from typing import Any

PLATFORMS: Any
UPDATE_INTERVAL: int

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class EvilGeniusUpdateCoordinator(update_coordinator.DataUpdateCoordinator[dict]):
    info: dict
    client: Any
    def __init__(self, hass: HomeAssistant, name: str, client: pyevilgenius.EvilGeniusDevice) -> None: ...
    @property
    def device_name(self) -> str: ...
    async def _async_update_data(self) -> dict: ...

class EvilGeniusEntity(update_coordinator.CoordinatorEntity):
    coordinator: EvilGeniusUpdateCoordinator
    @property
    def device_info(self) -> DeviceInfo: ...
