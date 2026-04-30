from . import OmadaConfigEntry as OmadaConfigEntry
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import format_mac as format_mac
from typing import Any

ENTRY_TO_REDACT: Incomplete
RUNTIME_TO_REDACT: Incomplete

def _build_identifier_replacements(mac_values: set[str]) -> dict[str, str]: ...
def _replace_identifiers(data: Any, to_replace: Mapping[str, str]) -> Any: ...
def _redact_runtime_record(raw_data: Mapping[str, Any], replacements: Mapping[str, str]) -> dict[str, Any]: ...
async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: OmadaConfigEntry) -> dict[str, Any]: ...
