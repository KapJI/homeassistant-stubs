from .const import CONF_API_USER as CONF_API_USER
from .coordinator import HabiticaConfigEntry as HabiticaConfigEntry
from homeassistant.const import CONF_URL as CONF_URL
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

async def async_get_config_entry_diagnostics(hass: HomeAssistant, config_entry: HabiticaConfigEntry) -> dict[str, Any]: ...
