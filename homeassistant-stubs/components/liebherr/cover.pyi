from .const import DOMAIN as DOMAIN
from .coordinator import LiebherrConfigEntry as LiebherrConfigEntry, LiebherrCoordinator as LiebherrCoordinator
from .entity import LiebherrEntity as LiebherrEntity, ZONE_POSITION_MAP as ZONE_POSITION_MAP
from _typeshed import Incomplete
from homeassistant.components.cover import CoverDeviceClass as CoverDeviceClass, CoverEntity as CoverEntity, CoverEntityFeature as CoverEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyliebherrhomeapi import AutoDoorControl as AutoDoorControl
from typing import Any, override

PARALLEL_UPDATES: int

def _create_cover_entities(coordinators: list[LiebherrCoordinator]) -> list[LiebherrAutoDoor]: ...
async def async_setup_entry(hass: HomeAssistant, entry: LiebherrConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LiebherrAutoDoor(LiebherrEntity, CoverEntity):
    _attr_device_class: Incomplete
    _attr_supported_features: Incomplete
    _attr_translation_key: str
    _optimistic_state: bool | None
    _zone_id: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: LiebherrCoordinator, zone_id: int, has_multiple_zones: bool) -> None: ...
    @property
    def _auto_door_control(self) -> AutoDoorControl | None: ...
    @property
    @override
    def available(self) -> bool: ...
    @callback
    @override
    def _handle_coordinator_update(self) -> None: ...
    @property
    @override
    def is_closed(self) -> bool | None: ...
    @property
    @override
    def is_opening(self) -> bool | None: ...
    @property
    @override
    def is_closing(self) -> bool | None: ...
    async def _async_set_door(self, value: bool) -> None: ...
    @override
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    @override
    async def async_close_cover(self, **kwargs: Any) -> None: ...
