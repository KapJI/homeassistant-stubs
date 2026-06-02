from .const import DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from .models import SnoozConfigEntry as SnoozConfigEntry, SnoozConfigurationData as SnoozConfigurationData
from homeassistant.components.bluetooth import BluetoothReachabilityIntent as BluetoothReachabilityIntent, async_address_reachability_diagnostics as async_address_reachability_diagnostics, async_ble_device_from_address as async_ble_device_from_address
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS, CONF_TOKEN as CONF_TOKEN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady

async def async_setup_entry(hass: HomeAssistant, entry: SnoozConfigEntry) -> bool: ...
async def _async_update_listener(hass: HomeAssistant, entry: SnoozConfigEntry) -> None: ...
async def async_unload_entry(hass: HomeAssistant, entry: SnoozConfigEntry) -> bool: ...
