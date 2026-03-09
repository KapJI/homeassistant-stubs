from .coordinator import LunatoneConfigEntry as LunatoneConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: LunatoneConfigEntry) -> dict[str, Any]: ...
