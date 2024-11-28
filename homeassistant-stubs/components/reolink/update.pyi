from . import DEVICE_UPDATE_INTERVAL as DEVICE_UPDATE_INTERVAL
from .entity import ReolinkChannelCoordinatorEntity as ReolinkChannelCoordinatorEntity, ReolinkChannelEntityDescription as ReolinkChannelEntityDescription, ReolinkHostCoordinatorEntity as ReolinkHostCoordinatorEntity, ReolinkHostEntityDescription as ReolinkHostEntityDescription
from .util import ReolinkConfigEntry as ReolinkConfigEntry, ReolinkData as ReolinkData
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.update import UpdateDeviceClass as UpdateDeviceClass, UpdateEntity as UpdateEntity, UpdateEntityDescription as UpdateEntityDescription, UpdateEntityFeature as UpdateEntityFeature
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_call_later as async_call_later
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

PARALLEL_UPDATES: int
RESUME_AFTER_INSTALL: int
POLL_AFTER_INSTALL: int
POLL_PROGRESS: int

@dataclass(frozen=True, kw_only=True)
class ReolinkUpdateEntityDescription(UpdateEntityDescription, ReolinkChannelEntityDescription):
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., cmd_key=..., cmd_id=..., supported=..., display_precision=...) -> None: ...

@dataclass(frozen=True, kw_only=True)
class ReolinkHostUpdateEntityDescription(UpdateEntityDescription, ReolinkHostEntityDescription):
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., cmd_key=..., cmd_id=..., supported=..., display_precision=...) -> None: ...

UPDATE_ENTITIES: Incomplete
HOST_UPDATE_ENTITIES: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ReolinkConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ReolinkUpdateBaseEntity(CoordinatorEntity[DataUpdateCoordinator[None]], UpdateEntity):
    _attr_release_url: str
    _channel: Incomplete
    _host: Incomplete
    _cancel_update: Incomplete
    _cancel_resume: Incomplete
    _cancel_progress: Incomplete
    _installing: bool
    _reolink_data: Incomplete
    def __init__(self, reolink_data: ReolinkData, channel: int | None, coordinator: DataUpdateCoordinator[None]) -> None: ...
    @property
    def installed_version(self) -> str | None: ...
    @property
    def latest_version(self) -> str | None: ...
    @property
    def in_progress(self) -> bool: ...
    @property
    def update_percentage(self) -> int: ...
    @property
    def supported_features(self) -> UpdateEntityFeature: ...
    @property
    def available(self) -> bool: ...
    def version_is_newer(self, latest_version: str, installed_version: str) -> bool: ...
    async def async_release_notes(self) -> str | None: ...
    async def async_install(self, version: str | None, backup: bool, **kwargs: Any) -> None: ...
    async def _pause_update_coordinator(self) -> None: ...
    async def _resume_update_coordinator(self, *args: Any) -> None: ...
    async def _async_update_progress(self, *args: Any) -> None: ...
    async def _async_update_future(self, *args: Any) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...

class ReolinkUpdateEntity(ReolinkUpdateBaseEntity, ReolinkChannelCoordinatorEntity):
    entity_description: ReolinkUpdateEntityDescription
    _channel: int
    def __init__(self, reolink_data: ReolinkData, channel: int, entity_description: ReolinkUpdateEntityDescription) -> None: ...

class ReolinkHostUpdateEntity(ReolinkUpdateBaseEntity, ReolinkHostCoordinatorEntity):
    entity_description: ReolinkHostUpdateEntityDescription
    def __init__(self, reolink_data: ReolinkData, entity_description: ReolinkHostUpdateEntityDescription) -> None: ...
