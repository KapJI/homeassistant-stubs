from .const import CONF_TAILNET as CONF_TAILNET, DOMAIN as DOMAIN
from .coordinator import TailscaleDataUpdateCoordinator as TailscaleDataUpdateCoordinator
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

TO_REDACT: Any

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: ConfigEntry) -> dict[str, Any]: ...
