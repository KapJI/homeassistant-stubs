from .const import CONF_SITE_ID as CONF_SITE_ID, DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from .coordinator import AmberConfigEntry as AmberConfigEntry, AmberUpdateCoordinator as AmberUpdateCoordinator
from .services import async_setup_services as async_setup_services
from _typeshed import Incomplete
from homeassistant.components.sensor import ConfigType as ConfigType
from homeassistant.const import CONF_API_TOKEN as CONF_API_TOKEN
from homeassistant.core import HomeAssistant as HomeAssistant

CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: AmberConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: AmberConfigEntry) -> bool: ...
