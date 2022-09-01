from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.diagnostics.util import async_redact_data as async_redact_data
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import device_registry as dr
from typing import Any

DEVICE_INFO_TO_REDACT: Incomplete
SETTINGS_TO_REDACT: Incomplete

async def async_get_device_diagnostics(hass: HomeAssistant, entry: ConfigEntry, device: dr.DeviceEntry) -> dict[str, Any]: ...
