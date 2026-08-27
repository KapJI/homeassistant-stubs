from .const import CONF_HMI_HARDWARE as CONF_HMI_HARDWARE, CONF_HMI_SERIAL as CONF_HMI_SERIAL, CONF_WRAPPED_KEY as CONF_WRAPPED_KEY
from .coordinator import SpecializedTurboCoordinator as SpecializedTurboCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

_LOGGER: Incomplete
PLATFORMS: list[Platform]
type SpecializedTurboConfigEntry = ConfigEntry[SpecializedTurboCoordinator]

async def async_setup_entry(hass: HomeAssistant, entry: SpecializedTurboConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: SpecializedTurboConfigEntry) -> bool: ...
