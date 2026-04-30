from .const import CONF_GATEWAY_ID as CONF_GATEWAY_ID, DOMAIN as DOMAIN
from .coordinator import TradfriConfigEntry as TradfriConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: TradfriConfigEntry) -> dict[str, Any]: ...
