from .const import DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from .coordinator import BesenCoordinator as BesenCoordinator
from _typeshed import Incomplete
from bleak.backends.device import BLEDevice as BLEDevice
from homeassistant.components import bluetooth as bluetooth
from homeassistant.components.bluetooth import BluetoothReachabilityIntent as BluetoothReachabilityIntent
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS, CONF_NAME as CONF_NAME, CONF_PIN as CONF_PIN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady

type BesenConfigEntry = ConfigEntry[BesenCoordinator]
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: BesenConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: BesenConfigEntry) -> bool: ...
