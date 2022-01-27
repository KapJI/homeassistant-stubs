from . import CONF_NOISE_PSK as CONF_NOISE_PSK, DomainData as DomainData
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

CONF_MAC_ADDRESS: str
REDACT_KEYS: Any

async def async_get_config_entry_diagnostics(hass: HomeAssistant, config_entry: ConfigEntry) -> dict[str, Any]: ...
