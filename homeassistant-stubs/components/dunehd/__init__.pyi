from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from pdunehd import DuneHDPlayer
from typing import Final

PLATFORMS: Final[list[Platform]]
type DuneHDConfigEntry = ConfigEntry[DuneHDPlayer]

async def async_setup_entry(hass: HomeAssistant, entry: DuneHDConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: DuneHDConfigEntry) -> bool: ...
