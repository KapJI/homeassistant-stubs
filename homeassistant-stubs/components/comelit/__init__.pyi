from .const import DEFAULT_PORT as DEFAULT_PORT
from .coordinator import ComelitBaseCoordinator as ComelitBaseCoordinator, ComelitConfigEntry as ComelitConfigEntry, ComelitSerialBridge as ComelitSerialBridge, ComelitVedoSystem as ComelitVedoSystem
from _typeshed import Incomplete
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PIN as CONF_PIN, CONF_PORT as CONF_PORT, CONF_TYPE as CONF_TYPE, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

BRIDGE_PLATFORMS: Incomplete
VEDO_PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ComelitConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ComelitConfigEntry) -> bool: ...
