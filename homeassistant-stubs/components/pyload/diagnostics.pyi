from .coordinator import PyLoadConfigEntry as PyLoadConfigEntry, PyLoadData as PyLoadData
from _typeshed import Incomplete
from homeassistant.components.diagnostics import REDACTED as REDACTED, async_redact_data as async_redact_data
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_URL as CONF_URL, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

TO_REDACT: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, config_entry: PyLoadConfigEntry) -> dict[str, Any]: ...
