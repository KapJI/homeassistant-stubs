from .const import CONF_LOCALE as CONF_LOCALE, DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from .renault_hub import RenaultHub as RenaultHub
from .services import SERVICE_AC_START as SERVICE_AC_START, setup_services as setup_services, unload_services as unload_services
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
