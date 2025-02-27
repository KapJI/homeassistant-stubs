from .coordinator import InComfortConfigEntry as InComfortConfigEntry
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from typing import Any

REDACT_CONFIG: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: InComfortConfigEntry) -> dict[str, Any]: ...
@callback
def _async_get_diagnostics(hass: HomeAssistant, entry: InComfortConfigEntry) -> dict[str, Any]: ...
