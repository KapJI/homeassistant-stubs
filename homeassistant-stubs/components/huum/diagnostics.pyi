from .coordinator import HuumConfigEntry as HuumConfigEntry
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

TO_REDACT_DATA: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: HuumConfigEntry) -> dict[str, Any]: ...
