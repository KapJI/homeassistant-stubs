from .const import CONF_SENSOR_ID as CONF_SENSOR_ID
from .coordinator import LuftdatenConfigEntry as LuftdatenConfigEntry
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.const import CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

TO_REDACT: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: LuftdatenConfigEntry) -> dict[str, Any]: ...
