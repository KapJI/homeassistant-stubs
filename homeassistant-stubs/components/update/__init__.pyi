from .const import ATTR_BACKUP as ATTR_BACKUP, ATTR_INSTALLED_VERSION as ATTR_INSTALLED_VERSION, ATTR_LATEST_VERSION as ATTR_LATEST_VERSION, ATTR_VERSION as ATTR_VERSION, DOMAIN as DOMAIN, SERVICE_INSTALL as SERVICE_INSTALL, SERVICE_SKIP as SERVICE_SKIP, UpdateEntityFeature as UpdateEntityFeature
from _typeshed import Incomplete
from enum import StrEnum
from homeassistant.components import websocket_api
from homeassistant.const import EntityCategory
from homeassistant.helpers.entity import ABCCachedProperties, EntityDescription
from homeassistant.helpers.restore_state import RestoreEntity
from propcache import cached_property
from typing import Any, final

__all__ = ['ATTR_BACKUP', 'ATTR_INSTALLED_VERSION', 'ATTR_LATEST_VERSION', 'ATTR_VERSION', 'DEVICE_CLASSES_SCHEMA', 'DOMAIN', 'PLATFORM_SCHEMA_BASE', 'PLATFORM_SCHEMA', 'SERVICE_INSTALL', 'SERVICE_SKIP', 'UpdateDeviceClass', 'UpdateEntity', 'UpdateEntityDescription', 'UpdateEntityFeature']

PLATFORM_SCHEMA: Incomplete
PLATFORM_SCHEMA_BASE: Incomplete

class UpdateDeviceClass(StrEnum):
    FIRMWARE = 'firmware'

DEVICE_CLASSES_SCHEMA: Incomplete

class UpdateEntityDescription(EntityDescription, frozen_or_thawed=True):
    device_class: UpdateDeviceClass | None = ...
    display_precision: int = ...
    entity_category: EntityCategory | None = ...

class UpdateEntity(RestoreEntity, cached_properties=CACHED_PROPERTIES_WITH_ATTR_, metaclass=ABCCachedProperties):
    _entity_component_unrecorded_attributes: Incomplete
    entity_description: UpdateEntityDescription
    _attr_auto_update: bool
    _attr_installed_version: str | None
    _attr_device_class: UpdateDeviceClass | None
    _attr_display_precision: int
    _attr_in_progress: bool | int
    _attr_latest_version: str | None
    _attr_release_summary: str | None
    _attr_release_url: str | None
    _attr_state: None
    _attr_supported_features: UpdateEntityFeature
    _attr_title: str | None
    _attr_update_percentage: int | float | None
    __skipped_version: str | None
    __in_progress: bool
    @cached_property
    def auto_update(self) -> bool: ...
    @cached_property
    def installed_version(self) -> str | None: ...
    def _default_to_device_class_name(self) -> bool: ...
    @cached_property
    def device_class(self) -> UpdateDeviceClass | None: ...
    @cached_property
    def display_precision(self) -> int: ...
    @property
    def entity_category(self) -> EntityCategory | None: ...
    @property
    def entity_picture(self) -> str | None: ...
    @cached_property
    def in_progress(self) -> bool | int | None: ...
    @cached_property
    def latest_version(self) -> str | None: ...
    @cached_property
    def release_summary(self) -> str | None: ...
    @cached_property
    def release_url(self) -> str | None: ...
    @cached_property
    def supported_features(self) -> UpdateEntityFeature: ...
    @cached_property
    def title(self) -> str | None: ...
    @cached_property
    def update_percentage(self) -> int | float | None: ...
    @final
    async def async_skip(self) -> None: ...
    @final
    async def async_clear_skipped(self) -> None: ...
    async def async_install(self, version: str | None, backup: bool, **kwargs: Any) -> None: ...
    def install(self, version: str | None, backup: bool, **kwargs: Any) -> None: ...
    async def async_release_notes(self) -> str | None: ...
    def release_notes(self) -> str | None: ...
    def version_is_newer(self, latest_version: str, installed_version: str) -> bool: ...
    @property
    @final
    def state(self) -> str | None: ...
    @final
    @property
    def state_attributes(self) -> dict[str, Any] | None: ...
    @final
    async def async_install_with_progress(self, version: str | None, backup: bool) -> None: ...
    async def async_internal_added_to_hass(self) -> None: ...
