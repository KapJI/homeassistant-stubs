from .const import DOMAIN_COORDINATORS as DOMAIN_COORDINATORS
from .coordinator import MonitorCoordinator as MonitorCoordinator
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: ConfigEntry) -> dict[str, Any]: ...
