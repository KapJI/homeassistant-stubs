from .const import DOMAIN as DOMAIN
from .coordinator import TailwindDataUpdateCoordinator as TailwindDataUpdateCoordinator
from .typing import TailwindConfigEntry as TailwindConfigEntry
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: TailwindConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
