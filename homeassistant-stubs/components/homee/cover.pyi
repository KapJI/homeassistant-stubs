from . import HomeeConfigEntry as HomeeConfigEntry
from .entity import HomeeNodeEntity as HomeeNodeEntity
from .helpers import setup_homee_platform as setup_homee_platform
from _typeshed import Incomplete
from enum import Enum
from homeassistant.components.cover import ATTR_POSITION as ATTR_POSITION, ATTR_TILT_POSITION as ATTR_TILT_POSITION, CoverDeviceClass as CoverDeviceClass, CoverEntity as CoverEntity, CoverEntityFeature as CoverEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyHomee.model import HomeeAttribute as HomeeAttribute, HomeeNode as HomeeNode
from typing import Any, override

_LOGGER: Incomplete
PARALLEL_UPDATES: int
COVER_DEVICE_PROFILES: Incomplete
IS_CLOSED_ATTRIBUTES: Incomplete

class HomeeCoverState(float, Enum):
    OPEN = 0.0
    CLOSED = 1.0
    STOPPED = 2.0
    OPENING = 3.0
    CLOSING = 4.0

class HomeeSlatState(float, Enum):
    STOPPED = 0.0
    CLOSED = 1.0
    OPEN = 2.0

def get_open_close_attribute(node: HomeeNode) -> HomeeAttribute | None: ...
def get_cover_features(node: HomeeNode, open_close_attribute: HomeeAttribute | None) -> CoverEntityFeature: ...
def get_device_class(node: HomeeNode) -> CoverDeviceClass | None: ...
async def add_cover_entities(config_entry: HomeeConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback, nodes: list[HomeeNode]) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: HomeeConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
def is_cover_node(node: HomeeNode) -> bool: ...

class HomeeCover(HomeeNodeEntity, CoverEntity):
    _attr_name: Incomplete
    _open_close_attribute: Incomplete
    _attr_supported_features: Incomplete
    _attr_device_class: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, node: HomeeNode, entry: HomeeConfigEntry) -> None: ...
    @property
    @override
    def current_cover_position(self) -> int | None: ...
    @property
    @override
    def current_cover_tilt_position(self) -> int | None: ...
    @property
    @override
    def is_opening(self) -> bool | None: ...
    @property
    @override
    def is_closing(self) -> bool | None: ...
    @property
    @override
    def is_closed(self) -> bool: ...
    @override
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    @override
    async def async_close_cover(self, **kwargs: Any) -> None: ...
    @override
    async def async_set_cover_position(self, **kwargs: Any) -> None: ...
    @override
    async def async_stop_cover(self, **kwargs: Any) -> None: ...
    @override
    async def async_open_cover_tilt(self, **kwargs: Any) -> None: ...
    @override
    async def async_close_cover_tilt(self, **kwargs: Any) -> None: ...
    @override
    async def async_stop_cover_tilt(self, **kwargs: Any) -> None: ...
    @override
    async def async_set_cover_tilt_position(self, **kwargs: Any) -> None: ...
