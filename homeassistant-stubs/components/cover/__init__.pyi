from _typeshed import Incomplete
from collections.abc import Callable as Callable
from enum import IntFlag
from homeassistant.backports.enum import StrEnum as StrEnum
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import SERVICE_CLOSE_COVER as SERVICE_CLOSE_COVER, SERVICE_CLOSE_COVER_TILT as SERVICE_CLOSE_COVER_TILT, SERVICE_OPEN_COVER as SERVICE_OPEN_COVER, SERVICE_OPEN_COVER_TILT as SERVICE_OPEN_COVER_TILT, SERVICE_SET_COVER_POSITION as SERVICE_SET_COVER_POSITION, SERVICE_SET_COVER_TILT_POSITION as SERVICE_SET_COVER_TILT_POSITION, SERVICE_STOP_COVER as SERVICE_STOP_COVER, SERVICE_STOP_COVER_TILT as SERVICE_STOP_COVER_TILT, SERVICE_TOGGLE as SERVICE_TOGGLE, SERVICE_TOGGLE_COVER_TILT as SERVICE_TOGGLE_COVER_TILT, STATE_CLOSED as STATE_CLOSED, STATE_CLOSING as STATE_CLOSING, STATE_OPEN as STATE_OPEN, STATE_OPENING as STATE_OPENING
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.config_validation import PLATFORM_SCHEMA as PLATFORM_SCHEMA, PLATFORM_SCHEMA_BASE as PLATFORM_SCHEMA_BASE
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import bind_hass as bind_hass
from typing import Any, TypeVar

_LOGGER: Incomplete
DOMAIN: str
SCAN_INTERVAL: Incomplete
ENTITY_ID_FORMAT: Incomplete
_P: Incomplete
_R = TypeVar('_R')

class CoverDeviceClass(StrEnum):
    AWNING: str
    BLIND: str
    CURTAIN: str
    DAMPER: str
    DOOR: str
    GARAGE: str
    GATE: str
    SHADE: str
    SHUTTER: str
    WINDOW: str

DEVICE_CLASSES_SCHEMA: Incomplete
DEVICE_CLASSES: Incomplete
DEVICE_CLASS_AWNING: Incomplete
DEVICE_CLASS_BLIND: Incomplete
DEVICE_CLASS_CURTAIN: Incomplete
DEVICE_CLASS_DAMPER: Incomplete
DEVICE_CLASS_DOOR: Incomplete
DEVICE_CLASS_GARAGE: Incomplete
DEVICE_CLASS_GATE: Incomplete
DEVICE_CLASS_SHADE: Incomplete
DEVICE_CLASS_SHUTTER: Incomplete
DEVICE_CLASS_WINDOW: Incomplete

class CoverEntityFeature(IntFlag):
    OPEN: int
    CLOSE: int
    SET_POSITION: int
    STOP: int
    OPEN_TILT: int
    CLOSE_TILT: int
    STOP_TILT: int
    SET_TILT_POSITION: int

SUPPORT_OPEN: int
SUPPORT_CLOSE: int
SUPPORT_SET_POSITION: int
SUPPORT_STOP: int
SUPPORT_OPEN_TILT: int
SUPPORT_CLOSE_TILT: int
SUPPORT_STOP_TILT: int
SUPPORT_SET_TILT_POSITION: int
ATTR_CURRENT_POSITION: str
ATTR_CURRENT_TILT_POSITION: str
ATTR_POSITION: str
ATTR_TILT_POSITION: str

def is_closed(hass: HomeAssistant, entity_id: str) -> bool: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class CoverEntityDescription(EntityDescription):
    device_class: Union[CoverDeviceClass, None]
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

class CoverEntity(Entity):
    entity_description: CoverEntityDescription
    _attr_current_cover_position: Union[int, None]
    _attr_current_cover_tilt_position: Union[int, None]
    _attr_device_class: Union[CoverDeviceClass, None]
    _attr_is_closed: Union[bool, None]
    _attr_is_closing: Union[bool, None]
    _attr_is_opening: Union[bool, None]
    _attr_state: None
    _attr_supported_features: Union[CoverEntityFeature, None]
    _cover_is_last_toggle_direction_open: bool
    @property
    def current_cover_position(self) -> Union[int, None]: ...
    @property
    def current_cover_tilt_position(self) -> Union[int, None]: ...
    @property
    def device_class(self) -> Union[CoverDeviceClass, None]: ...
    @property
    def state(self) -> Union[str, None]: ...
    @property
    def state_attributes(self) -> dict[str, Any]: ...
    @property
    def supported_features(self) -> CoverEntityFeature: ...
    @property
    def is_opening(self) -> Union[bool, None]: ...
    @property
    def is_closing(self) -> Union[bool, None]: ...
    @property
    def is_closed(self) -> Union[bool, None]: ...
    def open_cover(self, **kwargs: Any) -> None: ...
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    def close_cover(self, **kwargs: Any) -> None: ...
    async def async_close_cover(self, **kwargs: Any) -> None: ...
    def toggle(self, **kwargs: Any) -> None: ...
    async def async_toggle(self, **kwargs: Any) -> None: ...
    def set_cover_position(self, **kwargs: Any) -> None: ...
    async def async_set_cover_position(self, **kwargs: Any) -> None: ...
    def stop_cover(self, **kwargs: Any) -> None: ...
    async def async_stop_cover(self, **kwargs: Any) -> None: ...
    def open_cover_tilt(self, **kwargs: Any) -> None: ...
    async def async_open_cover_tilt(self, **kwargs: Any) -> None: ...
    def close_cover_tilt(self, **kwargs: Any) -> None: ...
    async def async_close_cover_tilt(self, **kwargs: Any) -> None: ...
    def set_cover_tilt_position(self, **kwargs: Any) -> None: ...
    async def async_set_cover_tilt_position(self, **kwargs: Any) -> None: ...
    def stop_cover_tilt(self, **kwargs: Any) -> None: ...
    async def async_stop_cover_tilt(self, **kwargs: Any) -> None: ...
    def toggle_tilt(self, **kwargs: Any) -> None: ...
    async def async_toggle_tilt(self, **kwargs: Any) -> None: ...
    def _get_toggle_function(self, fns: dict[str, Callable[_P, _R]]) -> Callable[_P, _R]: ...
