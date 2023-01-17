from .const import DOMAIN as DOMAIN
from .util import get_usb_service_info as get_usb_service_info
from _typeshed import Incomplete
from homeassistant.components import usb as usb
from homeassistant.components.hassio import AddonError as AddonError, AddonInfo as AddonInfo, AddonManager as AddonManager, AddonState as AddonState, is_hassio as is_hassio
from homeassistant.components.homeassistant_hardware.silabs_multiprotocol_addon import get_addon_manager as get_addon_manager, get_zigbee_socket as get_zigbee_socket
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady

_LOGGER: Incomplete

async def _wait_multi_pan_addon(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
async def _multi_pan_addon_info(hass: HomeAssistant, entry: ConfigEntry) -> Union[AddonInfo, None]: ...
async def _async_usb_scan_done(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
