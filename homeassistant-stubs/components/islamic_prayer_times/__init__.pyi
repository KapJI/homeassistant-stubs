from .const import DOMAIN as DOMAIN
from .coordinator import IslamicPrayerDataUpdateCoordinator as IslamicPrayerDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

PLATFORMS: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
async def async_options_updated(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
