from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

ENTRY_FIELDS_DATA_TO_REDACT: Incomplete
DEVICE_INFORMATION_DATA_TO_REDACT: Incomplete
DEVICE_SIGNAL_DATA_TO_REDACT: Incomplete
MONITORING_STATUS_DATA_TO_REDACT: Incomplete
NET_CURRENT_PLMN_DATA_TO_REDACT: Incomplete
LAN_HOST_INFO_DATA_TO_REDACT: Incomplete
WLAN_WIFI_GUEST_NETWORK_SWITCH_DATA_TO_REDACT: Incomplete
WLAN_MULTI_BASIC_SETTINGS_DATA_TO_REDACT: Incomplete
TO_REDACT: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: ConfigEntry) -> dict[str, Any]: ...
