from .coordinator import MinecraftServerConfigEntry as MinecraftServerConfigEntry
from collections.abc import Iterable
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

TO_REDACT: Iterable[Any]

async def async_get_config_entry_diagnostics(hass: HomeAssistant, config_entry: MinecraftServerConfigEntry) -> dict[str, Any]: ...
