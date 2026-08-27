from .coordinator import HotSpringConfigEntry as HotSpringConfigEntry
from _typeshed import Incomplete
from homeassistant.components.diagnostics import REDACTED as REDACTED, async_redact_data as async_redact_data
from homeassistant.const import CONF_HOST as CONF_HOST
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

TO_REDACT: Incomplete

def _redact_mac(value: str, patterns: list[str]) -> str: ...
async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: HotSpringConfigEntry) -> dict[str, Any]: ...
