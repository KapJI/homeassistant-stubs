from .const import CONF_MANUAL as CONF_MANUAL, DEFAULT_INTERVAL as DEFAULT_INTERVAL, DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from .coordinator import FastdotcomDataUpdateCoordindator as FastdotcomDataUpdateCoordindator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL, EVENT_HOMEASSISTANT_STARTED as EVENT_HOMEASSISTANT_STARTED
from homeassistant.core import CoreState as CoreState, Event as Event, HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.helpers.typing import ConfigType as ConfigType

_LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
