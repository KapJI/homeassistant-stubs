from . import TeslemetryConfigEntry as TeslemetryConfigEntry
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

VEHICLE_REDACT: Incomplete
ENERGY_LIVE_REDACT: Incomplete
ENERGY_INFO_REDACT: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: TeslemetryConfigEntry) -> dict[str, Any]: ...
