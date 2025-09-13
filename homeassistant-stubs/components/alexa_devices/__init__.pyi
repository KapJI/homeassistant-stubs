from .const import CONF_LOGIN_DATA as CONF_LOGIN_DATA, CONF_SITE as CONF_SITE, COUNTRY_DOMAINS as COUNTRY_DOMAINS, DOMAIN as DOMAIN, _LOGGER as _LOGGER
from .coordinator import AmazonConfigEntry as AmazonConfigEntry, AmazonDevicesCoordinator as AmazonDevicesCoordinator
from .services import async_setup_services as async_setup_services
from _typeshed import Incomplete
from homeassistant.const import CONF_COUNTRY as CONF_COUNTRY, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.typing import ConfigType as ConfigType

PLATFORMS: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: AmazonConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, entry: AmazonConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: AmazonConfigEntry) -> bool: ...
