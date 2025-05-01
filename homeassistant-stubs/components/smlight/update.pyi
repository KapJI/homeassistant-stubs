from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from .coordinator import SmConfigEntry as SmConfigEntry, SmFirmwareUpdateCoordinator as SmFirmwareUpdateCoordinator, SmFwData as SmFwData
from .entity import SmEntity as SmEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.update import UpdateDeviceClass as UpdateDeviceClass, UpdateEntity as UpdateEntity, UpdateEntityDescription as UpdateEntityDescription, UpdateEntityFeature as UpdateEntityFeature
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pysmlight.models import Firmware as Firmware, Info as Info
from pysmlight.sse import MessageEvent as MessageEvent
from typing import Any

PARALLEL_UPDATES: int

def zigbee_latest_version(data: SmFwData, idx: int) -> Firmware | None: ...

@dataclass(frozen=True, kw_only=True)
class SmUpdateEntityDescription(UpdateEntityDescription):
    installed_version: Callable[[Info, int], str | None]
    latest_version: Callable[[SmFwData, int], Firmware | None]

CORE_UPDATE_ENTITY: Incomplete
ZB_UPDATE_ENTITY: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: SmConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SmUpdateEntity(SmEntity, UpdateEntity):
    coordinator: SmFirmwareUpdateCoordinator
    entity_description: SmUpdateEntityDescription
    _attr_entity_category: Incomplete
    _attr_device_class: Incomplete
    _attr_supported_features: Incomplete
    _attr_unique_id: Incomplete
    _finished_event: Incomplete
    _firmware: Firmware | None
    _unload: list[Callable]
    idx: Incomplete
    def __init__(self, coordinator: SmFirmwareUpdateCoordinator, description: SmUpdateEntityDescription, idx: int = 0) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    @property
    def installed_version(self) -> str | None: ...
    @property
    def latest_version(self) -> str | None: ...
    def register_callbacks(self) -> None: ...
    def release_notes(self) -> str | None: ...
    _attr_update_percentage: Incomplete
    @callback
    def _update_progress(self, progress: MessageEvent) -> None: ...
    _attr_in_progress: bool
    def _update_done(self) -> None: ...
    @callback
    def _update_finished(self, event: MessageEvent) -> None: ...
    @callback
    def _update_failed(self, event: MessageEvent) -> None: ...
    async def async_install(self, version: str | None, backup: bool, **kwargs: Any) -> None: ...
