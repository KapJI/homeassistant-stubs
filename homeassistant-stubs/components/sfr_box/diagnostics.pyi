from .coordinator import SFRConfigEntry as SFRConfigEntry
from _typeshed import DataclassInstance, Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

TO_REDACT: Incomplete

def _async_redact_data(obj: DataclassInstance | None) -> dict[str, Any] | None: ...
async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: SFRConfigEntry) -> dict[str, Any]: ...
