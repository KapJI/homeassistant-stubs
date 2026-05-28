from .const import DOMAIN as DOMAIN
from .coordinator import IndevoltConfigEntry as IndevoltConfigEntry, IndevoltCoordinator as IndevoltCoordinator
from .services import async_setup_services as async_setup_services
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType

PLATFORMS: list[Platform]
CONFIG_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: IndevoltConfigEntry) -> bool: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: IndevoltConfigEntry) -> bool: ...
