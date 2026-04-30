from .coordinator import LiebherrConfigEntry as LiebherrConfigEntry
from _typeshed import Incomplete
from homeassistant.const import CONF_API_KEY as CONF_API_KEY
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

TO_REDACT: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: LiebherrConfigEntry) -> dict[str, Any]: ...
