from .const import DOMAIN as DOMAIN
from .util import get_usb_service_info as get_usb_service_info
from homeassistant.components import usb as usb
from homeassistant.components.homeassistant_hardware.silabs_multiprotocol_addon import check_multi_pan_addon as check_multi_pan_addon, get_zigbee_socket as get_zigbee_socket, multi_pan_addon_using_device as multi_pan_addon_using_device
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady, HomeAssistantError as HomeAssistantError

async def _async_usb_scan_done(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
