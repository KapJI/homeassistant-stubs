from .const import DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from .coordinator import NeoPoolConfigEntry as NeoPoolConfigEntry, NeoPoolCoordinator as NeoPoolCoordinator
from .services import async_setup_services as async_setup_services
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType

CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: NeoPoolConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: NeoPoolConfigEntry) -> bool: ...
