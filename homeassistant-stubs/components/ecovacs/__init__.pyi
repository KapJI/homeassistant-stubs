from .const import DOMAIN as DOMAIN
from .controller import EcovacsController as EcovacsController
from .services import async_setup_services as async_setup_services
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType
from sucks import VacBot as VacBot

PLATFORMS: Incomplete
type EcovacsConfigEntry = ConfigEntry[EcovacsController]
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: EcovacsConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: EcovacsConfigEntry) -> bool: ...
