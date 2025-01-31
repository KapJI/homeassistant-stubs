from .const import DOMAIN as DOMAIN
from .coordinator import CookidooConfigEntry as CookidooConfigEntry, CookidooDataUpdateCoordinator as CookidooDataUpdateCoordinator
from .helpers import cookidoo_from_config_entry as cookidoo_from_config_entry
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: list[Platform]
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: CookidooConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: CookidooConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, config_entry: CookidooConfigEntry) -> bool: ...
