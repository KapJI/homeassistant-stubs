import pyevilgenius
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator

PLATFORMS: Incomplete
UPDATE_INTERVAL: int

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class EvilGeniusUpdateCoordinator(DataUpdateCoordinator[dict]):
    info: dict
    product: Union[dict, None]
    client: Incomplete
    def __init__(self, hass: HomeAssistant, name: str, client: pyevilgenius.EvilGeniusDevice) -> None: ...
    @property
    def device_name(self) -> str: ...
    @property
    def product_name(self) -> Union[str, None]: ...
    async def _async_update_data(self) -> dict: ...

class EvilGeniusEntity(CoordinatorEntity[EvilGeniusUpdateCoordinator]):
    @property
    def device_info(self) -> DeviceInfo: ...
