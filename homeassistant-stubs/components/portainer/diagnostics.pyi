from . import PortainerConfigEntry as PortainerConfigEntry
from .coordinator import PortainerCoordinator as PortainerCoordinator
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.const import CONF_API_TOKEN as CONF_API_TOKEN
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

TO_REDACT: Incomplete

def _serialize_coordinator(coordinator: PortainerCoordinator) -> dict[str, Any]: ...
async def async_get_config_entry_diagnostics(hass: HomeAssistant, config_entry: PortainerConfigEntry) -> dict[str, Any]: ...
