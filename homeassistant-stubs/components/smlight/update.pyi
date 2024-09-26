from . import SmConfigEntry as SmConfigEntry
from .coordinator import SmFirmwareUpdateCoordinator as SmFirmwareUpdateCoordinator, SmFwData as SmFwData
from .entity import SmEntity as SmEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.update import UpdateDeviceClass as UpdateDeviceClass, UpdateEntity as UpdateEntity, UpdateEntityDescription as UpdateEntityDescription, UpdateEntityFeature as UpdateEntityFeature
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pysmlight.models import Firmware as Firmware, Info as Info
from pysmlight.sse import MessageEvent as MessageEvent
from typing import Any, Final

@dataclass(frozen=True, kw_only=True)
class SmUpdateEntityDescription(UpdateEntityDescription):
    installed_version: Callable[[Info], str | None]
    fw_list: Callable[[SmFwData], list[Firmware] | None]
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., installed_version, fw_list) -> None: ...

UPDATE_ENTITIES: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, entry: SmConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SmUpdateEntity(SmEntity, UpdateEntity):
    coordinator: SmFirmwareUpdateCoordinator
    entity_description: SmUpdateEntityDescription
    _attr_entity_category: Incomplete
    _attr_device_class: Incomplete
    _attr_supported_features: Incomplete
    _attr_unique_id: Incomplete
    _finished_event: Incomplete
    _firmware: Incomplete
    _unload: Incomplete
    def __init__(self, coordinator: SmFirmwareUpdateCoordinator, description: SmUpdateEntityDescription) -> None: ...
    @property
    def installed_version(self) -> str | None: ...
    @property
    def latest_version(self) -> str | None: ...
    def register_callbacks(self) -> None: ...
    def release_notes(self) -> str | None: ...
    _attr_in_progress: Incomplete
    def _update_progress(self, progress: MessageEvent) -> None: ...
    def _update_done(self) -> None: ...
    def _update_finished(self, event: MessageEvent) -> None: ...
    def _update_failed(self, event: MessageEvent) -> None: ...
    async def async_install(self, version: str | None, backup: bool, **kwargs: Any) -> None: ...
