from .const import RADIO_DEVICE as RADIO_DEVICE, ZHA_HW_DISCOVERY_DATA as ZHA_HW_DISCOVERY_DATA
from homeassistant.components.hassio import get_os_info as get_os_info, is_hassio as is_hassio
from homeassistant.components.homeassistant_hardware.silabs_multiprotocol_addon import check_multi_pan_addon as check_multi_pan_addon, get_zigbee_socket as get_zigbee_socket, multi_pan_addon_using_device as multi_pan_addon_using_device
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_HARDWARE as SOURCE_HARDWARE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady, HomeAssistantError as HomeAssistantError
from homeassistant.helpers import discovery_flow as discovery_flow

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
