from .const import RADIO_DEVICE as RADIO_DEVICE, ZHA_HW_DISCOVERY_DATA as ZHA_HW_DISCOVERY_DATA
from _typeshed import Incomplete
from homeassistant.components.hassio import AddonError as AddonError, AddonInfo as AddonInfo, AddonManager as AddonManager, AddonState as AddonState, get_os_info as get_os_info
from homeassistant.components.homeassistant_hardware.silabs_multiprotocol_addon import get_addon_manager as get_addon_manager, get_zigbee_socket as get_zigbee_socket
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady

_LOGGER: Incomplete

async def _multi_pan_addon_info(hass: HomeAssistant, entry: ConfigEntry) -> Union[AddonInfo, None]: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
