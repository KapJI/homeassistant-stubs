from .const import DATA_LISTENER_REGISTRY as DATA_LISTENER_REGISTRY, DOMAIN as DOMAIN
from .coordinator import BitvisConfigEntry as BitvisConfigEntry, BitvisDataUpdateCoordinator as BitvisDataUpdateCoordinator, async_get_listener_registry as async_get_listener_registry
from _typeshed import Incomplete
from homeassistant.const import CONF_PORT as CONF_PORT, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType

_PLATFORMS: list[Platform]
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: BitvisConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: BitvisConfigEntry) -> bool: ...
