from .coordinator import ZinvoltConfigEntry as ZinvoltConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: ZinvoltConfigEntry) -> dict[str, Any]: ...
