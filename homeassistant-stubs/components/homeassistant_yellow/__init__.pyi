from .const import FIRMWARE as FIRMWARE, FIRMWARE_VERSION as FIRMWARE_VERSION, NABU_CASA_FIRMWARE_RELEASES_URL as NABU_CASA_FIRMWARE_RELEASES_URL, RADIO_DEVICE as RADIO_DEVICE, ZHA_HW_DISCOVERY_DATA as ZHA_HW_DISCOVERY_DATA
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.hassio import get_os_info as get_os_info
from homeassistant.components.homeassistant_hardware.coordinator import FirmwareUpdateCoordinator as FirmwareUpdateCoordinator
from homeassistant.components.homeassistant_hardware.silabs_multiprotocol_addon import check_multi_pan_addon as check_multi_pan_addon
from homeassistant.components.homeassistant_hardware.util import ApplicationType as ApplicationType, guess_firmware_info as guess_firmware_info
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_HARDWARE as SOURCE_HARDWARE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady, HomeAssistantError as HomeAssistantError
from homeassistant.helpers import discovery_flow as discovery_flow
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.hassio import is_hassio as is_hassio

_LOGGER: Incomplete
type HomeAssistantYellowConfigEntry = ConfigEntry[HomeAssistantYellowData]

@dataclass
class HomeAssistantYellowData:
    coordinator: FirmwareUpdateCoordinator

async def async_setup_entry(hass: HomeAssistant, entry: HomeAssistantYellowConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: HomeAssistantYellowConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, config_entry: HomeAssistantYellowConfigEntry) -> bool: ...
