from .const import PLATFORMS as PLATFORMS
from .coordinator import QubeCoordinator as QubeCoordinator
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from python_qube_heatpump import QubeClient

@dataclass
class QubeData:
    coordinator: QubeCoordinator
    client: QubeClient
    sw_version: str | None
type QubeConfigEntry = ConfigEntry[QubeData]

async def async_setup_entry(hass: HomeAssistant, entry: QubeConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: QubeConfigEntry) -> bool: ...
