from . import DeconzConfigEntry as DeconzConfigEntry
from .entity import DeconzDevice as DeconzDevice
from .hub import DeconzHub as DeconzHub
from _typeshed import Incomplete
from homeassistant.components.cover import ATTR_POSITION as ATTR_POSITION, ATTR_TILT_POSITION as ATTR_TILT_POSITION, CoverDeviceClass as CoverDeviceClass, CoverEntity as CoverEntity, CoverEntityFeature as CoverEntityFeature, DOMAIN as COVER_DOMAIN
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pydeconz.models.event import EventType as EventType
from pydeconz.models.light.cover import Cover
from typing import Any

DECONZ_TYPE_TO_DEVICE_CLASS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: DeconzConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DeconzCover(DeconzDevice[Cover], CoverEntity):
    TYPE = COVER_DOMAIN
    _attr_supported_features: Incomplete
    _attr_device_class: Incomplete
    legacy_mode: Incomplete
    def __init__(self, cover_id: str, hub: DeconzHub) -> None: ...
    @property
    def current_cover_position(self) -> int: ...
    @property
    def is_closed(self) -> bool: ...
    async def async_set_cover_position(self, **kwargs: Any) -> None: ...
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    async def async_close_cover(self, **kwargs: Any) -> None: ...
    async def async_stop_cover(self, **kwargs: Any) -> None: ...
    @property
    def current_cover_tilt_position(self) -> int | None: ...
    async def async_set_cover_tilt_position(self, **kwargs: Any) -> None: ...
    async def async_open_cover_tilt(self, **kwargs: Any) -> None: ...
    async def async_close_cover_tilt(self, **kwargs: Any) -> None: ...
    async def async_stop_cover_tilt(self, **kwargs: Any) -> None: ...
