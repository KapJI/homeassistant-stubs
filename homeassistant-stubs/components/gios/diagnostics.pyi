from .coordinator import GiosConfigEntry as GiosConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

async def async_get_config_entry_diagnostics(hass: HomeAssistant, config_entry: GiosConfigEntry) -> dict[str, Any]: ...
