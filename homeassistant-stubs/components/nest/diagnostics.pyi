from .const import DATA_SDM as DATA_SDM, DATA_SUBSCRIBER as DATA_SUBSCRIBER, DOMAIN as DOMAIN
from google_nest_sdm.device import Device as Device
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

REDACT_DEVICE_TRAITS: Any

async def async_get_config_entry_diagnostics(hass: HomeAssistant, config_entry: ConfigEntry) -> dict: ...
def get_device_data(device: Device) -> dict[str, Any]: ...
