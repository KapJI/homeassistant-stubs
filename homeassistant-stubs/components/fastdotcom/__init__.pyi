from .const import CONF_MANUAL as CONF_MANUAL, DEFAULT_INTERVAL as DEFAULT_INTERVAL, DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from .coordinator import FastdotcomDataUpdateCoordindator as FastdotcomDataUpdateCoordindator
from .services import async_setup_services as async_setup_services
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.start import async_at_started as async_at_started
from homeassistant.helpers.typing import ConfigType as ConfigType

_LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
