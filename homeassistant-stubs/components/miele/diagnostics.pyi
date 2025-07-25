from .coordinator import MieleConfigEntry as MieleConfigEntry
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntry as DeviceEntry
from typing import Any

TO_REDACT: Incomplete

def hash_identifier(key: str) -> str: ...
def redact_identifiers(in_data: dict[str, Any]) -> dict[str, Any]: ...
async def async_get_config_entry_diagnostics(hass: HomeAssistant, config_entry: MieleConfigEntry) -> dict[str, Any]: ...
async def async_get_device_diagnostics(hass: HomeAssistant, config_entry: MieleConfigEntry, device: DeviceEntry) -> dict[str, Any]: ...
