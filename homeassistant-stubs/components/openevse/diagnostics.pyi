from .coordinator import OpenEVSEConfigEntry as OpenEVSEConfigEntry
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

REDACT_CONFIG_DATA: Incomplete
CHARGER_PROPERTIES: Incomplete

def _to_json_safe(val: Any) -> Any: ...
async def async_get_config_entry_diagnostics(_hass: HomeAssistant, config_entry: OpenEVSEConfigEntry) -> dict[str, Any]: ...
