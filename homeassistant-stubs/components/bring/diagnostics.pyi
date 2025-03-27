from .coordinator import BringConfigEntry as BringConfigEntry
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.const import CONF_EMAIL as CONF_EMAIL, CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

TO_REDACT: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, config_entry: BringConfigEntry) -> dict[str, Any]: ...
