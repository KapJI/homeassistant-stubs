from .coordinator import WAQIConfigEntry as WAQIConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: WAQIConfigEntry) -> dict[str, Any]: ...
