from .const import DOMAIN as DOMAIN
from .coordinator import RAVEnDataCoordinator as RAVEnDataCoordinator
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_MAC as CONF_MAC
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from typing import Any

TO_REDACT_CONFIG: Incomplete
TO_REDACT_DATA: Incomplete

def async_redact_meter_macs(data: dict) -> dict: ...
async def async_get_config_entry_diagnostics(hass: HomeAssistant, config_entry: ConfigEntry) -> Mapping[str, Any]: ...
