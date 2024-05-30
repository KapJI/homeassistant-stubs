from .const import CONF_CONTINENT as CONF_CONTINENT, DOMAIN as DOMAIN
from .controller import EcovacsController as EcovacsController
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_COUNTRY as CONF_COUNTRY, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType

CONFIG_SCHEMA: Incomplete
PLATFORMS: Incomplete
EcovacsConfigEntry = ConfigEntry[EcovacsController]

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: EcovacsConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: EcovacsConfigEntry) -> bool: ...
