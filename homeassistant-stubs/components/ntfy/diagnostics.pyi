from . import NtfyConfigEntry as NtfyConfigEntry
from homeassistant.components.diagnostics import REDACTED as REDACTED
from homeassistant.const import CONF_URL as CONF_URL
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

async def async_get_config_entry_diagnostics(hass: HomeAssistant, config_entry: NtfyConfigEntry) -> dict[str, Any]: ...
