from .const import CONF_HAS_PWD as CONF_HAS_PWD
from .coordinator import SolarLogCoordinator as SolarLogCoordinator, SolarlogConfigEntry as SolarlogConfigEntry
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

_LOGGER: Incomplete
PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: SolarlogConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: SolarlogConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, config_entry: SolarlogConfigEntry) -> bool: ...
