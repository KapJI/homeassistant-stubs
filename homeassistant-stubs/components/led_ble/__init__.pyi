from .const import DEVICE_TIMEOUT as DEVICE_TIMEOUT, UPDATE_SECONDS as UPDATE_SECONDS
from .models import LEDBLEConfigEntry as LEDBLEConfigEntry, LEDBLEData as LEDBLEData
from _typeshed import Incomplete
from homeassistant.components import bluetooth as bluetooth
from homeassistant.components.bluetooth.match import ADDRESS as ADDRESS, BluetoothCallbackMatcher as BluetoothCallbackMatcher
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

PLATFORMS: list[Platform]
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: LEDBLEConfigEntry) -> bool: ...
async def _async_update_listener(hass: HomeAssistant, entry: LEDBLEConfigEntry) -> None: ...
async def async_unload_entry(hass: HomeAssistant, entry: LEDBLEConfigEntry) -> bool: ...
