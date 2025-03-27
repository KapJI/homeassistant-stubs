from . import DATA_COMPONENT as DATA_COMPONENT
from .const import OTBR_ADDON_MANAGER_DATA as OTBR_ADDON_MANAGER_DATA, OTBR_ADDON_NAME as OTBR_ADDON_NAME, OTBR_ADDON_SLUG as OTBR_ADDON_SLUG, ZIGBEE_FLASHER_ADDON_MANAGER_DATA as ZIGBEE_FLASHER_ADDON_MANAGER_DATA, ZIGBEE_FLASHER_ADDON_NAME as ZIGBEE_FLASHER_ADDON_NAME, ZIGBEE_FLASHER_ADDON_SLUG as ZIGBEE_FLASHER_ADDON_SLUG
from .silabs_multiprotocol_addon import WaitingAddonManager as WaitingAddonManager, get_multiprotocol_addon_manager as get_multiprotocol_addon_manager
from _typeshed import Incomplete
from collections.abc import AsyncIterator, Iterable
from contextlib import asynccontextmanager
from dataclasses import dataclass
from enum import StrEnum
from homeassistant.components.hassio import AddonError as AddonError, AddonManager as AddonManager, AddonState as AddonState
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
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
    ROUTER = 'router'
    @classmethod
    def from_flasher_application_type(cls, app_type: FlasherApplicationType) -> ApplicationType: ...
    def as_flasher_application_type(self) -> FlasherApplicationType: ...

@callback
def get_otbr_addon_manager(hass: HomeAssistant) -> WaitingAddonManager: ...
@callback
def get_zigbee_flasher_addon_manager(hass: HomeAssistant) -> WaitingAddonManager: ...

@dataclass(kw_only=True)
class OwningAddon:
    slug: str
    def _get_addon_manager(self, hass: HomeAssistant) -> WaitingAddonManager: ...
    async def is_running(self, hass: HomeAssistant) -> bool: ...
    @asynccontextmanager
    async def temporarily_stop(self, hass: HomeAssistant) -> AsyncIterator[None]: ...

@dataclass(kw_only=True)
class OwningIntegration:
    config_entry_id: str
    async def is_running(self, hass: HomeAssistant) -> bool: ...
    @asynccontextmanager
    async def temporarily_stop(self, hass: HomeAssistant) -> AsyncIterator[None]: ...

@dataclass(kw_only=True)
class FirmwareInfo:
    device: str
    firmware_type: ApplicationType
    firmware_version: str | None
    source: str
    owners: list[OwningAddon | OwningIntegration]
    async def is_running(self, hass: HomeAssistant) -> bool: ...

async def get_otbr_addon_firmware_info(hass: HomeAssistant, otbr_addon_manager: AddonManager) -> FirmwareInfo | None: ...
async def guess_hardware_owners(hass: HomeAssistant, device_path: str) -> list[FirmwareInfo]: ...
async def guess_firmware_info(hass: HomeAssistant, device_path: str) -> FirmwareInfo: ...
async def probe_silabs_firmware_info(device: str, *, probe_methods: Iterable[ApplicationType] | None = None) -> FirmwareInfo | None: ...
async def probe_silabs_firmware_type(device: str, *, probe_methods: Iterable[ApplicationType] | None = None) -> ApplicationType | None: ...
