from .coordinator import FirmwareUpdateCoordinator as FirmwareUpdateCoordinator
from .helpers import async_register_firmware_info_callback as async_register_firmware_info_callback
from .util import ApplicationType as ApplicationType, FirmwareInfo as FirmwareInfo, async_firmware_flashing_context as async_firmware_flashing_context, async_flash_silabs_firmware as async_flash_silabs_firmware, async_get_raspberry_pi_firmware_info as async_get_raspberry_pi_firmware_info, async_update_raspberry_pi_firmware as async_update_raspberry_pi_firmware, humanize_rpi_firmware_version as humanize_rpi_firmware_version, rpi_firmware_release_url as rpi_firmware_release_url
from _typeshed import Incomplete
from aiohasupervisor.models import RaspberryPiFirmwareInfo as RaspberryPiFirmwareInfo
from collections.abc import Callable
from dataclasses import dataclass
from ha_silabs_firmware_client import FirmwareManifest, FirmwareMetadata as FirmwareMetadata
from homeassistant.components.update import UpdateDeviceClass as UpdateDeviceClass, UpdateEntity as UpdateEntity, UpdateEntityDescription as UpdateEntityDescription, UpdateEntityFeature as UpdateEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.restore_state import ExtraStoredData as ExtraStoredData
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any, override
from universal_silabs_flasher.flasher import DeviceSpecificFlasher as DeviceSpecificFlasher

_LOGGER: Incomplete
type FirmwareChangeCallbackType = Callable[[ApplicationType | None, ApplicationType | None], None]

@dataclass(kw_only=True, frozen=True)
class FirmwareUpdateEntityDescription(UpdateEntityDescription):
    version_parser: Callable[[str], str]
    fw_type: str | None
    version_key: str | None
    expected_firmware_type: ApplicationType | None
    firmware_name: str | None

@dataclass
class FirmwareUpdateExtraStoredData(ExtraStoredData):
    firmware_manifest: FirmwareManifest | None = ...
    @override
    def as_dict(self) -> dict[str, Any]: ...
    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> FirmwareUpdateExtraStoredData: ...

class BaseFirmwareUpdateEntity(CoordinatorEntity[FirmwareUpdateCoordinator], UpdateEntity):
    entity_description: FirmwareUpdateEntityDescription
    _attr_supported_features: Incomplete
    _attr_has_entity_name: bool
    _flasher_cls: type[DeviceSpecificFlasher]
    _current_device: Incomplete
    _config_entry: Incomplete
    _current_firmware_info: FirmwareInfo | None
    _firmware_type_change_callbacks: set[FirmwareChangeCallbackType]
    _latest_manifest: FirmwareManifest | None
    _latest_firmware: FirmwareMetadata | None
    def __init__(self, device: str, config_entry: ConfigEntry, update_coordinator: FirmwareUpdateCoordinator, entity_description: FirmwareUpdateEntityDescription) -> None: ...
    def add_firmware_type_changed_callback(self, change_callback: FirmwareChangeCallbackType) -> CALLBACK_TYPE: ...
    @override
    async def async_added_to_hass(self) -> None: ...
    @property
    @override
    def extra_restore_state_data(self) -> FirmwareUpdateExtraStoredData: ...
    @callback
    def _on_config_entry_change(self) -> None: ...
    @callback
    def _firmware_info_callback(self, firmware_info: FirmwareInfo) -> None: ...
    _attr_title: Incomplete
    _attr_installed_version: Incomplete
    _attr_latest_version: Incomplete
    _attr_release_summary: Incomplete
    _attr_release_url: Incomplete
    def _update_attributes(self) -> None: ...
    @callback
    @override
    def _handle_coordinator_update(self) -> None: ...
    _attr_update_percentage: Incomplete
    def _update_progress(self, offset: int, total_size: int) -> None: ...
    _attr_in_progress: bool
    @override
    async def async_install(self, version: str | None, backup: bool, **kwargs: Any) -> None: ...

class RaspberryPiFirmwareUpdateEntity(UpdateEntity):
    _attr_has_entity_name: bool
    _attr_should_poll: bool
    _attr_device_class: Incomplete
    _attr_supported_features: Incomplete
    _attr_translation_key: str
    _firmware: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    _board: Incomplete
    def __init__(self, firmware: RaspberryPiFirmwareInfo, device_info: DeviceInfo, unique_id: str, board: str) -> None: ...
    @property
    @override
    def installed_version(self) -> str | None: ...
    @property
    @override
    def latest_version(self) -> str | None: ...
    @property
    @override
    def release_url(self) -> str | None: ...
    @override
    async def async_release_notes(self) -> str | None: ...
    @override
    async def async_install(self, version: str | None, backup: bool, **kwargs: Any) -> None: ...
