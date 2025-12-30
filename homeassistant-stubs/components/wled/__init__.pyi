from .const import DOMAIN as DOMAIN
from .coordinator import WLEDConfigEntry as WLEDConfigEntry, WLEDDataUpdateCoordinator as WLEDDataUpdateCoordinator, WLEDReleasesDataUpdateCoordinator as WLEDReleasesDataUpdateCoordinator, normalize_mac_address as normalize_mac_address
from _typeshed import Incomplete
from homeassistant.config_entries import SOURCE_IGNORE as SOURCE_IGNORE
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.hass_dict import HassKey as HassKey

_LOGGER: Incomplete
PLATFORMS: Incomplete
WLED_KEY: HassKey[WLEDReleasesDataUpdateCoordinator]
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: WLEDConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: WLEDConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, config_entry: WLEDConfigEntry) -> bool: ...
