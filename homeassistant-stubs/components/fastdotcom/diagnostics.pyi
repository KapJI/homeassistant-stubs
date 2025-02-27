from .coordinator import FastdotcomConfigEntry as FastdotcomConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

async def async_get_config_entry_diagnostics(hass: HomeAssistant, config_entry: FastdotcomConfigEntry) -> dict[str, Any]: ...
