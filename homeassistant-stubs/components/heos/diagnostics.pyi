from .const import ATTR_PASSWORD as ATTR_PASSWORD, ATTR_USERNAME as ATTR_USERNAME, DOMAIN as DOMAIN
from .coordinator import HeosConfigEntry as HeosConfigEntry
from _typeshed import Incomplete
from collections.abc import Mapping, Sequence
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntry as DeviceEntry
from typing import Any

TO_REDACT: Incomplete

def _as_dict(data: Any, redact: bool = False) -> Mapping[str, Any] | Sequence[Any] | Any: ...
async def async_get_config_entry_diagnostics(hass: HomeAssistant, config_entry: HeosConfigEntry) -> dict[str, Any]: ...
async def async_get_device_diagnostics(hass: HomeAssistant, config_entry: HeosConfigEntry, device: DeviceEntry) -> dict[str, Any]: ...
