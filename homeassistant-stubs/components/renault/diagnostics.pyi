from . import RenaultHub as RenaultHub
from .const import CONF_KAMEREON_ACCOUNT_ID as CONF_KAMEREON_ACCOUNT_ID, DOMAIN as DOMAIN
from .renault_vehicle import RenaultVehicleProxy as RenaultVehicleProxy
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntry as DeviceEntry
from typing import Any

TO_REDACT: Any

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: ConfigEntry) -> dict[str, Any]: ...
async def async_get_device_diagnostics(hass: HomeAssistant, entry: ConfigEntry, device: DeviceEntry) -> dict[str, Any]: ...
def _get_vehicle_diagnostics(vehicle: RenaultVehicleProxy) -> dict[str, Any]: ...
