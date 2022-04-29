from .const import DATA_SDM as DATA_SDM, DATA_SUBSCRIBER as DATA_SUBSCRIBER, DOMAIN as DOMAIN
from _typeshed import Incomplete
from google_nest_sdm.device import Device as Device
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntry as DeviceEntry

REDACT_DEVICE_TRAITS: Incomplete

async def _get_nest_devices(hass: HomeAssistant, config_entry: ConfigEntry) -> dict[str, Device]: ...
async def async_get_config_entry_diagnostics(hass: HomeAssistant, config_entry: ConfigEntry) -> dict: ...
async def async_get_device_diagnostics(hass: HomeAssistant, config_entry: ConfigEntry, device: DeviceEntry) -> dict: ...
