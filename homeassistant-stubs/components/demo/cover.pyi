from . import DOMAIN as DOMAIN
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.components.cover import ATTR_POSITION as ATTR_POSITION, ATTR_TILT_POSITION as ATTR_TILT_POSITION, CoverDeviceClass as CoverDeviceClass, CoverEntity as CoverEntity, CoverEntityFeature as CoverEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_track_utc_time_change as async_track_utc_time_change
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DemoCover(CoverEntity):
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_should_poll: bool
    hass: Incomplete
    _unique_id: Incomplete
    _position: Incomplete
    _attr_device_class: Incomplete
    _attr_supported_features: Incomplete
    _set_position: int | None
    _set_tilt_position: int | None
    _tilt_position: Incomplete
    _requested_closing: bool
    _requested_closing_tilt: bool
    _unsub_listener_cover: CALLBACK_TYPE | None
    _unsub_listener_cover_tilt: CALLBACK_TYPE | None
    _is_opening: bool
    _is_closing: bool
    _closed: bool
    _attr_device_info: Incomplete
    def __init__(self, hass: HomeAssistant, unique_id: str, device_name: str, position: int | None = None, tilt_position: int | None = None, device_class: CoverDeviceClass | None = None, supported_features: CoverEntityFeature | None = None) -> None: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def current_cover_position(self) -> int | None: ...
    @property
    def current_cover_tilt_position(self) -> int | None: ...
    @property
    def is_closed(self) -> bool: ...
    @property
    def is_closing(self) -> bool: ...
    @property
    def is_opening(self) -> bool: ...
    async def async_close_cover(self, **kwargs: Any) -> None: ...
    async def async_close_cover_tilt(self, **kwargs: Any) -> None: ...
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    async def async_open_cover_tilt(self, **kwargs: Any) -> None: ...
    async def async_set_cover_position(self, **kwargs: Any) -> None: ...
    async def async_set_cover_tilt_position(self, **kwargs: Any) -> None: ...
    async def async_stop_cover(self, **kwargs: Any) -> None: ...
    async def async_stop_cover_tilt(self, **kwargs: Any) -> None: ...
    def _listen_cover(self) -> None: ...
    async def _time_changed_cover(self, now: datetime) -> None: ...
    def _listen_cover_tilt(self) -> None: ...
    async def _time_changed_cover_tilt(self, now: datetime) -> None: ...
