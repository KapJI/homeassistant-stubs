from .coordinator import TileConfigEntry as TileConfigEntry
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.const import CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE, CONF_UUID as CONF_UUID
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

CONF_ALTITUDE: str
TO_REDACT: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: TileConfigEntry) -> dict[str, Any]: ...
