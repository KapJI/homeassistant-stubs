from . import GuardianConfigEntry as GuardianConfigEntry
from .const import CONF_UID as CONF_UID
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.const import CONF_UNIQUE_ID as CONF_UNIQUE_ID
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

CONF_BSSID: str
CONF_PAIRED_UIDS: str
CONF_SSID: str
CONF_TITLE: str
TO_REDACT: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: GuardianConfigEntry) -> dict[str, Any]: ...
