from . import EcowittConfigEntry as EcowittConfigEntry
from .const import DOMAIN as DOMAIN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import AnyDeviceEntry as AnyDeviceEntry
from typing import Any

async def async_get_device_diagnostics(hass: HomeAssistant, entry: EcowittConfigEntry, device: AnyDeviceEntry) -> dict[str, Any]: ...
