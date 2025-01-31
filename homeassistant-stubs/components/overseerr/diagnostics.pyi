from . import CONF_CLOUDHOOK_URL as CONF_CLOUDHOOK_URL
from .coordinator import OverseerrConfigEntry as OverseerrConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: OverseerrConfigEntry) -> dict[str, Any]: ...
