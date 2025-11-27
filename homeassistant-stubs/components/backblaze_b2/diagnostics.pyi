from . import BackblazeConfigEntry as BackblazeConfigEntry
from .const import CONF_APPLICATION_KEY as CONF_APPLICATION_KEY, CONF_KEY_ID as CONF_KEY_ID
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

TO_REDACT_ENTRY_DATA: Incomplete
TO_REDACT_ACCOUNT_DATA_ALLOWED: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: BackblazeConfigEntry) -> dict[str, Any]: ...
