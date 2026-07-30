from . import DsmrConfigEntry as DsmrConfigEntry
from .const import CONF_ENCRYPTION_KEY as CONF_ENCRYPTION_KEY
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.util.json import json_loads as json_loads
from typing import Any

TO_REDACT: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, config_entry: DsmrConfigEntry) -> dict[str, Any]: ...
