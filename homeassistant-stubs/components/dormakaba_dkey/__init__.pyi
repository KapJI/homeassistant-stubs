from .const import CONF_ASSOCIATION_DATA as CONF_ASSOCIATION_DATA
from .coordinator import DormakabaDkeyConfigEntry as DormakabaDkeyConfigEntry, DormakabaDkeyCoordinator as DormakabaDkeyCoordinator
from homeassistant.components import bluetooth as bluetooth
from homeassistant.components.bluetooth.match import ADDRESS as ADDRESS, BluetoothCallbackMatcher as BluetoothCallbackMatcher
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: DormakabaDkeyConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: DormakabaDkeyConfigEntry) -> bool: ...
