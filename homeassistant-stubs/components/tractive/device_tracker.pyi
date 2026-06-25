from . import Trackables as Trackables, TractiveClient as TractiveClient, TractiveConfigEntry as TractiveConfigEntry
from .const import SERVER_UNAVAILABLE as SERVER_UNAVAILABLE, TRACKER_POSITION_UPDATED as TRACKER_POSITION_UPDATED
from .entity import TractiveEntity as TractiveEntity
from _typeshed import Incomplete
from homeassistant.components.device_tracker import SourceType as SourceType, TrackerEntity as TrackerEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, override

async def async_setup_entry(hass: HomeAssistant, entry: TractiveConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class TractiveDeviceTracker(TractiveEntity, TrackerEntity):
    _attr_translation_key: str
    _attr_name: Incomplete
    _attr_latitude: Incomplete
    _attr_longitude: Incomplete
    _attr_location_accuracy: float
    _source_type: str
    _attr_unique_id: Incomplete
    def __init__(self, client: TractiveClient, item: Trackables) -> None: ...
    @property
    @override
    def source_type(self) -> SourceType: ...
    _attr_available: bool
    @callback
    def _handle_position_update(self, event: dict[str, Any]) -> None: ...
    @override
    async def async_added_to_hass(self) -> None: ...
