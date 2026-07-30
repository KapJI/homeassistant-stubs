from .coordinator import WattwaechterConfigEntry as WattwaechterConfigEntry
from _typeshed import Incomplete
from aio_wattwaechter.models import SystemInfo as SystemInfo
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.const import CONF_MAC as CONF_MAC, CONF_TOKEN as CONF_TOKEN
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

TO_REDACT: Incomplete

def _flatten_system(system: SystemInfo) -> dict[str, dict[str, Any]]: ...
async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: WattwaechterConfigEntry) -> dict[str, Any]: ...
