from .const import DESCRIPTION as DESCRIPTION, DEVICE as DEVICE, DOMAIN as DOMAIN, FIRMWARE as FIRMWARE, FIRMWARE_VERSION as FIRMWARE_VERSION, MANUFACTURER as MANUFACTURER, PID as PID, PRODUCT as PRODUCT, SERIAL_NUMBER as SERIAL_NUMBER, VID as VID
from _typeshed import Incomplete
from homeassistant.components.homeassistant_hardware.util import guess_firmware_info as guess_firmware_info
from homeassistant.components.usb import USBDevice as USBDevice, async_register_port_event_callback as async_register_port_event_callback, scan_serial_ports as scan_serial_ports
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady, HomeAssistantError as HomeAssistantError
from homeassistant.helpers.typing import ConfigType as ConfigType

_LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
