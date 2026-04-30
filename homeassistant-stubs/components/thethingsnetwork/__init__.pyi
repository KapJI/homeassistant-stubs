from .const import PLATFORMS as PLATFORMS, TTN_API_HOST as TTN_API_HOST
from .coordinator import TTNConfigEntry as TTNConfigEntry, TTNCoordinator as TTNCoordinator
from _typeshed import Incomplete
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_HOST as CONF_HOST
from homeassistant.core import HomeAssistant as HomeAssistant

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: TTNConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: TTNConfigEntry) -> bool: ...
