from .const import DATA_HANDLER as DATA_HANDLER, DOMAIN as DOMAIN
from .data_handler import CLIMATE_TOPOLOGY_CLASS_NAME as CLIMATE_TOPOLOGY_CLASS_NAME, NetatmoDataHandler as NetatmoDataHandler
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

TO_REDACT: Any

async def async_get_config_entry_diagnostics(hass: HomeAssistant, config_entry: ConfigEntry) -> dict: ...
