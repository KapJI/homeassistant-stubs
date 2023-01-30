from .const import DATA_DEVICE_MANAGER as DATA_DEVICE_MANAGER, DATA_SDM as DATA_SDM, DOMAIN as DOMAIN
from _typeshed import Incomplete
from google_nest_sdm.device import Device as Device
from google_nest_sdm.device_manager import DeviceManager as DeviceManager
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceEntry as DeviceEntry
from typing import Any

REDACT_DEVICE_TRAITS: Incomplete

def _async_get_nest_devices(hass: HomeAssistant, config_entry: ConfigEntry) -> dict[str, Device]: ...
async def async_get_config_entry_diagnostics(hass: HomeAssistant, config_entry: ConfigEntry) -> dict[str, Any]: ...
async def async_get_device_diagnostics(hass: HomeAssistant, config_entry: ConfigEntry, device: DeviceEntry) -> dict[str, Any]: ...
