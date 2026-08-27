from .const import DATA_WIIM as DATA_WIIM, WiimConfigEntry as WiimConfigEntry
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

TO_REDACT: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: WiimConfigEntry) -> dict[str, Any]: ...
