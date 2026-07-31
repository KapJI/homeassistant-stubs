from .const import CONF_OVERRIDE_REST_URL as CONF_OVERRIDE_REST_URL, DOMAIN as DOMAIN
from .controller import EcovacsController as EcovacsController
from .services import async_setup_services as async_setup_services
from .util import get_client_device_id as get_client_device_id
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DEVICE_ID as CONF_DEVICE_ID, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType
from sucks import VacBot as VacBot

PLATFORMS: Incomplete
type EcovacsConfigEntry = ConfigEntry[EcovacsController]
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: EcovacsConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: EcovacsConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, entry: EcovacsConfigEntry) -> bool: ...
