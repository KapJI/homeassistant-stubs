from .coordinator import QnapQswConfigEntry as QnapQswConfigEntry
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_UNIQUE_ID as CONF_UNIQUE_ID, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

TO_REDACT_CONFIG: Incomplete
TO_REDACT_DATA: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, config_entry: QnapQswConfigEntry) -> dict[str, Any]: ...
