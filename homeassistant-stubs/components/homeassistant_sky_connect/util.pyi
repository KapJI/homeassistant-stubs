from .const import HardwareVariant as HardwareVariant, OTBR_ADDON_MANAGER_DATA as OTBR_ADDON_MANAGER_DATA, OTBR_ADDON_NAME as OTBR_ADDON_NAME, OTBR_ADDON_SLUG as OTBR_ADDON_SLUG, ZHA_DOMAIN as ZHA_DOMAIN, ZIGBEE_FLASHER_ADDON_MANAGER_DATA as ZIGBEE_FLASHER_ADDON_MANAGER_DATA, ZIGBEE_FLASHER_ADDON_NAME as ZIGBEE_FLASHER_ADDON_NAME, ZIGBEE_FLASHER_ADDON_SLUG as ZIGBEE_FLASHER_ADDON_SLUG
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components import usb as usb
from homeassistant.components.hassio import AddonError as AddonError, AddonState as AddonState, is_hassio as is_hassio
from homeassistant.components.homeassistant_hardware.silabs_multiprotocol_addon import WaitingAddonManager as WaitingAddonManager, get_multiprotocol_addon_manager as get_multiprotocol_addon_manager
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigEntryState as ConfigEntryState
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.singleton import singleton as singleton
from universal_silabs_flasher.const import ApplicationType

_LOGGER: Incomplete

def get_usb_service_info(config_entry: ConfigEntry) -> usb.UsbServiceInfo: ...
def get_hardware_variant(config_entry: ConfigEntry) -> HardwareVariant: ...
def get_zha_device_path(config_entry: ConfigEntry) -> str | None: ...
def get_otbr_addon_manager(hass: HomeAssistant) -> WaitingAddonManager: ...
def get_zigbee_flasher_addon_manager(hass: HomeAssistant) -> WaitingAddonManager: ...

@dataclass(slots=True, kw_only=True)
class FirmwareGuess:
    is_running: bool
    firmware_type: ApplicationType
    source: str
    def __init__(self, *, is_running, firmware_type, source) -> None: ...

async def guess_firmware_type(hass: HomeAssistant, device_path: str) -> FirmwareGuess: ...
