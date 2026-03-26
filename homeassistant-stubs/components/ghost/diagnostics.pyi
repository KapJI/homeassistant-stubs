from . import GhostConfigEntry as GhostConfigEntry
from .const import CONF_ADMIN_API_KEY as CONF_ADMIN_API_KEY
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

TO_REDACT: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, config_entry: GhostConfigEntry) -> dict[str, Any]: ...
