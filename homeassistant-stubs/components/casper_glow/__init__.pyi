from .coordinator import CasperGlowConfigEntry as CasperGlowConfigEntry, CasperGlowCoordinator as CasperGlowCoordinator
from homeassistant.components import bluetooth as bluetooth
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: CasperGlowConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: CasperGlowConfigEntry) -> bool: ...
