from .coordinator import HDFuryConfigEntry as HDFuryConfigEntry, HDFuryCoordinator as HDFuryCoordinator
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: HDFuryConfigEntry) -> dict[str, Any]: ...
