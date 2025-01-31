from .const import DOMAIN as DOMAIN
from .onewirehub import OneWireConfigEntry as OneWireConfigEntry, OneWireHub as OneWireHub
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import device_registry as dr

_LOGGER: Incomplete
_PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: OneWireConfigEntry) -> bool: ...
async def async_remove_config_entry_device(hass: HomeAssistant, config_entry: OneWireConfigEntry, device_entry: dr.DeviceEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: OneWireConfigEntry) -> bool: ...
async def options_update_listener(hass: HomeAssistant, entry: OneWireConfigEntry) -> None: ...
