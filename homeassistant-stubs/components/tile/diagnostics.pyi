from .const import DATA_TILE as DATA_TILE, DOMAIN as DOMAIN
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE
from homeassistant.core import HomeAssistant as HomeAssistant
from pytile.tile import Tile as Tile
from typing import Any

CONF_ALTITUDE: str
CONF_UUID: str
TO_REDACT: Any

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: ConfigEntry) -> dict[str, Any]: ...
