from .const import TibberConfigEntry as TibberConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

async def async_get_config_entry_diagnostics(hass: HomeAssistant, config_entry: TibberConfigEntry) -> dict[str, Any]: ...
