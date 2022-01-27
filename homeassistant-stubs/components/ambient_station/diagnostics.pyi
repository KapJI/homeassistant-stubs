from . import AmbientStation as AmbientStation
from .const import CONF_APP_KEY as CONF_APP_KEY, DOMAIN as DOMAIN
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

CONF_API_KEY_CAMEL: str
CONF_APP_KEY_CAMEL: str
CONF_DEVICE_ID_CAMEL: str
CONF_LOCATION: str
CONF_MAC_ADDRESS: str
CONF_MAC_ADDRESS_CAMEL: str
CONF_TZ: str
TO_REDACT: Any

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: ConfigEntry) -> dict[str, Any]: ...
