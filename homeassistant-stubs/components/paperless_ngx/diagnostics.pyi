from . import PaperlessConfigEntry as PaperlessConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: PaperlessConfigEntry) -> dict[str, Any]: ...
