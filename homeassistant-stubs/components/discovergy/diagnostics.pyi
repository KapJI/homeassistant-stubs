from .coordinator import DiscovergyConfigEntry as DiscovergyConfigEntry
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

TO_REDACT_METER: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: DiscovergyConfigEntry) -> dict[str, Any]: ...
