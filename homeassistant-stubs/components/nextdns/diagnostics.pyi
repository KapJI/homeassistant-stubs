from .const import ATTR_DNSSEC as ATTR_DNSSEC, ATTR_ENCRYPTION as ATTR_ENCRYPTION, ATTR_IP_VERSIONS as ATTR_IP_VERSIONS, ATTR_PROTOCOLS as ATTR_PROTOCOLS, ATTR_SETTINGS as ATTR_SETTINGS, ATTR_STATUS as ATTR_STATUS, CONF_PROFILE_ID as CONF_PROFILE_ID, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_UNIQUE_ID as CONF_UNIQUE_ID
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

TO_REDACT: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, config_entry: ConfigEntry) -> dict[str, Any]: ...
