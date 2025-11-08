from .coordinator import AmazonConfigEntry as AmazonConfigEntry
from _typeshed import Incomplete
from aioamazondevices.structures import AmazonDevice as AmazonDevice
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntry as DeviceEntry
from typing import Any

TO_REDACT: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: AmazonConfigEntry) -> dict[str, Any]: ...
async def async_get_device_diagnostics(hass: HomeAssistant, entry: AmazonConfigEntry, device_entry: DeviceEntry) -> dict[str, Any]: ...
def build_device_data(device: AmazonDevice) -> dict[str, Any]: ...
