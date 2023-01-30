from .const import DOMAIN as DOMAIN, ID_TYPE_DEVICE_ID as ID_TYPE_DEVICE_ID
from .helpers import get_device_id as get_device_id, get_matter as get_matter
from _typeshed import Incomplete
from homeassistant.components.diagnostics import REDACTED as REDACTED
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import device_registry as dr
from typing import Any

ATTRIBUTES_TO_REDACT: Incomplete

def redact_matter_attributes(node_data: dict[str, Any]) -> dict[str, Any]: ...
def remove_serialization_type(data: dict[str, Any]) -> dict[str, Any]: ...
async def async_get_config_entry_diagnostics(hass: HomeAssistant, config_entry: ConfigEntry) -> dict[str, Any]: ...
async def async_get_device_diagnostics(hass: HomeAssistant, config_entry: ConfigEntry, device: dr.DeviceEntry) -> dict[str, Any]: ...
