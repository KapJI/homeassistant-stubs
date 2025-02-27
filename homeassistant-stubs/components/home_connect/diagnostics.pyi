from .const import DOMAIN as DOMAIN
from .coordinator import HomeConnectApplianceData as HomeConnectApplianceData, HomeConnectConfigEntry as HomeConnectConfigEntry
from aiohomeconnect.client import Client as HomeConnectClient
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntry as DeviceEntry
from typing import Any

async def _generate_appliance_diagnostics(client: HomeConnectClient, appliance: HomeConnectApplianceData) -> dict[str, Any]: ...
async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: HomeConnectConfigEntry) -> dict[str, Any]: ...
async def async_get_device_diagnostics(hass: HomeAssistant, entry: HomeConnectConfigEntry, device: DeviceEntry) -> dict[str, Any]: ...
