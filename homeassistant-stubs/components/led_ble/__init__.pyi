from .const import DEVICE_TIMEOUT as DEVICE_TIMEOUT
from .coordinator import LEDBLEConfigEntry as LEDBLEConfigEntry, LEDBLECoordinator as LEDBLECoordinator, LEDBLEData as LEDBLEData
from homeassistant.components import bluetooth as bluetooth
from homeassistant.components.bluetooth.match import ADDRESS as ADDRESS, BluetoothCallbackMatcher as BluetoothCallbackMatcher
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: LEDBLEConfigEntry) -> bool: ...
async def _async_update_listener(hass: HomeAssistant, entry: LEDBLEConfigEntry) -> None: ...
async def async_unload_entry(hass: HomeAssistant, entry: LEDBLEConfigEntry) -> bool: ...
