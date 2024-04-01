from .const import DOMAIN_COORDINATOR as DOMAIN_COORDINATOR
from .coordinator import SystemMonitorCoordinator as SystemMonitorCoordinator
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: ConfigEntry) -> dict[str, Any]: ...
