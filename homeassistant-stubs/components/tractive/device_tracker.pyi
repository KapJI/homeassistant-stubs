from . import Trackables as Trackables
from .const import CLIENT as CLIENT, DOMAIN as DOMAIN, SERVER_UNAVAILABLE as SERVER_UNAVAILABLE, TRACKABLES as TRACKABLES, TRACKER_HARDWARE_STATUS_UPDATED as TRACKER_HARDWARE_STATUS_UPDATED, TRACKER_POSITION_UPDATED as TRACKER_POSITION_UPDATED
from .entity import TractiveEntity as TractiveEntity
from _typeshed import Incomplete
from homeassistant.components.device_tracker import SourceType as SourceType, TrackerEntity as TrackerEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TractiveDeviceTracker(TractiveEntity, TrackerEntity):
    _attr_has_entity_name: bool
    _attr_icon: str
    _attr_name: str
    _battery_level: Incomplete
    _latitude: Incomplete
    _longitude: Incomplete
    _accuracy: Incomplete
    _source_type: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, user_id: str, item: Trackables) -> None: ...
    @property
    def source_type(self) -> SourceType: ...
    @property
    def latitude(self) -> float: ...
    @property
    def longitude(self) -> float: ...
    @property
    def location_accuracy(self) -> int: ...
    @property
    def battery_level(self) -> int: ...
    _attr_available: bool
    def _handle_hardware_status_update(self, event: dict[str, Any]) -> None: ...
    def _handle_position_update(self, event: dict[str, Any]) -> None: ...
    def _handle_server_unavailable(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
