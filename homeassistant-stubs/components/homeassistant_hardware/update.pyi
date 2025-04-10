from .coordinator import FirmwareUpdateCoordinator as FirmwareUpdateCoordinator
from .helpers import async_register_firmware_info_callback as async_register_firmware_info_callback
from .util import ApplicationType as ApplicationType, FirmwareInfo as FirmwareInfo, guess_firmware_info as guess_firmware_info, probe_silabs_firmware_info as probe_silabs_firmware_info
from _typeshed import Incomplete
from collections.abc import AsyncIterator, Callable
from contextlib import asynccontextmanager
from dataclasses import dataclass
from ha_silabs_firmware_client import FirmwareManifest, FirmwareMetadata as FirmwareMetadata
from homeassistant.components.update import UpdateEntity as UpdateEntity, UpdateEntityDescription as UpdateEntityDescription, UpdateEntityFeature as UpdateEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.restore_state import ExtraStoredData as ExtraStoredData
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

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
    def as_dict(self) -> dict[str, Any]: ...
    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> FirmwareUpdateExtraStoredData: ...

class BaseFirmwareUpdateEntity(CoordinatorEntity[FirmwareUpdateCoordinator], UpdateEntity):
    entity_description: FirmwareUpdateEntityDescription
    bootloader_reset_type: str | None
    _attr_supported_features: Incomplete
    _attr_has_entity_name: bool
    _current_device: Incomplete
    _config_entry: Incomplete
    _current_firmware_info: FirmwareInfo | None
    _firmware_type_change_callbacks: set[FirmwareChangeCallbackType]
    _latest_manifest: FirmwareManifest | None
    _latest_firmware: FirmwareMetadata | None
    def __init__(self, device: str, config_entry: ConfigEntry, update_coordinator: FirmwareUpdateCoordinator, entity_description: FirmwareUpdateEntityDescription) -> None: ...
    def add_firmware_type_changed_callback(self, change_callback: FirmwareChangeCallbackType) -> CALLBACK_TYPE: ...
    async def async_added_to_hass(self) -> None: ...
    @property
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
    def _handle_coordinator_update(self) -> None: ...
    _attr_update_percentage: Incomplete
    def _update_progress(self, offset: int, total_size: int) -> None: ...
    @asynccontextmanager
    async def _temporarily_stop_hardware_owners(self, device: str) -> AsyncIterator[None]: ...
    _attr_in_progress: bool
    async def async_install(self, version: str | None, backup: bool, **kwargs: Any) -> None: ...
