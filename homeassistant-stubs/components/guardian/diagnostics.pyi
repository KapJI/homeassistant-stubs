from .const import CONF_UID as CONF_UID, DATA_COORDINATOR as DATA_COORDINATOR, DATA_COORDINATOR_PAIRED_SENSOR as DATA_COORDINATOR_PAIRED_SENSOR, DOMAIN as DOMAIN
from .util import GuardianDataUpdateCoordinator as GuardianDataUpdateCoordinator
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

CONF_BSSID: str
CONF_PAIRED_UIDS: str
CONF_SSID: str
TO_REDACT: Any

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: ConfigEntry) -> dict[str, Any]: ...
