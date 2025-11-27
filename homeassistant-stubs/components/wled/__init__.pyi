from .const import DOMAIN as DOMAIN
from .coordinator import WLEDConfigEntry as WLEDConfigEntry, WLEDDataUpdateCoordinator as WLEDDataUpdateCoordinator, WLEDReleasesDataUpdateCoordinator as WLEDReleasesDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.hass_dict import HassKey as HassKey

PLATFORMS: Incomplete
WLED_KEY: HassKey[WLEDReleasesDataUpdateCoordinator]
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: WLEDConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: WLEDConfigEntry) -> bool: ...
