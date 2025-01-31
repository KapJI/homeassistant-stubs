from .const import OTBR_ADDON_MANAGER_DATA as OTBR_ADDON_MANAGER_DATA, OTBR_ADDON_NAME as OTBR_ADDON_NAME, OTBR_ADDON_SLUG as OTBR_ADDON_SLUG, ZHA_DOMAIN as ZHA_DOMAIN, ZIGBEE_FLASHER_ADDON_MANAGER_DATA as ZIGBEE_FLASHER_ADDON_MANAGER_DATA, ZIGBEE_FLASHER_ADDON_NAME as ZIGBEE_FLASHER_ADDON_NAME, ZIGBEE_FLASHER_ADDON_SLUG as ZIGBEE_FLASHER_ADDON_SLUG
from .silabs_multiprotocol_addon import WaitingAddonManager as WaitingAddonManager, get_multiprotocol_addon_manager as get_multiprotocol_addon_manager
from _typeshed import Incomplete
from collections.abc import Iterable
from dataclasses import dataclass
from enum import StrEnum
from homeassistant.components.hassio import AddonError as AddonError, AddonState as AddonState
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigEntryState as ConfigEntryState
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.hassio import is_hassio as is_hassio
from homeassistant.helpers.singleton import singleton as singleton
from universal_silabs_flasher.const import ApplicationType as FlasherApplicationType

_LOGGER: Incomplete

class ApplicationType(StrEnum):
    GECKO_BOOTLOADER = 'bootloader'
    CPC = 'cpc'
    EZSP = 'ezsp'
    SPINEL = 'spinel'
    @classmethod
    def from_flasher_application_type(cls, app_type: FlasherApplicationType) -> ApplicationType: ...
    def as_flasher_application_type(self) -> FlasherApplicationType: ...

def get_zha_device_path(config_entry: ConfigEntry) -> str | None: ...
@callback
def get_otbr_addon_manager(hass: HomeAssistant) -> WaitingAddonManager: ...
@callback
def get_zigbee_flasher_addon_manager(hass: HomeAssistant) -> WaitingAddonManager: ...

@dataclass(slots=True, kw_only=True)
class FirmwareGuess:
    is_running: bool
    firmware_type: ApplicationType
    source: str

async def guess_firmware_type(hass: HomeAssistant, device_path: str) -> FirmwareGuess: ...
async def probe_silabs_firmware_type(device: str, *, probe_methods: Iterable[ApplicationType] | None = None) -> ApplicationType | None: ...
