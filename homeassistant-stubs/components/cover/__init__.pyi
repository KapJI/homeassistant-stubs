from _typeshed import Incomplete
from collections.abc import Callable as Callable
from enum import IntFlag, StrEnum
from functools import cached_property as cached_property
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import SERVICE_CLOSE_COVER as SERVICE_CLOSE_COVER, SERVICE_CLOSE_COVER_TILT as SERVICE_CLOSE_COVER_TILT, SERVICE_OPEN_COVER as SERVICE_OPEN_COVER, SERVICE_OPEN_COVER_TILT as SERVICE_OPEN_COVER_TILT, SERVICE_SET_COVER_POSITION as SERVICE_SET_COVER_POSITION, SERVICE_SET_COVER_TILT_POSITION as SERVICE_SET_COVER_TILT_POSITION, SERVICE_STOP_COVER as SERVICE_STOP_COVER, SERVICE_STOP_COVER_TILT as SERVICE_STOP_COVER_TILT, SERVICE_TOGGLE as SERVICE_TOGGLE, SERVICE_TOGGLE_COVER_TILT as SERVICE_TOGGLE_COVER_TILT, STATE_CLOSED as STATE_CLOSED, STATE_CLOSING as STATE_CLOSING, STATE_OPEN as STATE_OPEN, STATE_OPENING as STATE_OPENING
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.config_validation import PLATFORM_SCHEMA as PLATFORM_SCHEMA, PLATFORM_SCHEMA_BASE as PLATFORM_SCHEMA_BASE
from homeassistant.helpers.deprecation import DeprecatedConstantEnum as DeprecatedConstantEnum, all_with_deprecated_constants as all_with_deprecated_constants, check_if_deprecated_constant as check_if_deprecated_constant, dir_with_deprecated_constants as dir_with_deprecated_constants
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import bind_hass as bind_hass
from typing import Any, ParamSpec, TypeVar

_LOGGER: Incomplete
DOMAIN: str
SCAN_INTERVAL: Incomplete
ENTITY_ID_FORMAT: Incomplete
_P = ParamSpec('_P')
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
_DEPRECATED_DEVICE_CLASS_AWNING: Incomplete
_DEPRECATED_DEVICE_CLASS_BLIND: Incomplete
_DEPRECATED_DEVICE_CLASS_CURTAIN: Incomplete
_DEPRECATED_DEVICE_CLASS_DAMPER: Incomplete
_DEPRECATED_DEVICE_CLASS_DOOR: Incomplete
_DEPRECATED_DEVICE_CLASS_GARAGE: Incomplete
_DEPRECATED_DEVICE_CLASS_GATE: Incomplete
_DEPRECATED_DEVICE_CLASS_SHADE: Incomplete
_DEPRECATED_DEVICE_CLASS_SHUTTER: Incomplete
_DEPRECATED_DEVICE_CLASS_WINDOW: Incomplete

class CoverEntityFeature(IntFlag):
    OPEN: int
    CLOSE: int
    SET_POSITION: int
    STOP: int
    OPEN_TILT: int
    CLOSE_TILT: int
    STOP_TILT: int
    SET_TILT_POSITION: int

_DEPRECATED_SUPPORT_OPEN: Incomplete
_DEPRECATED_SUPPORT_CLOSE: Incomplete
_DEPRECATED_SUPPORT_SET_POSITION: Incomplete
_DEPRECATED_SUPPORT_STOP: Incomplete
_DEPRECATED_SUPPORT_OPEN_TILT: Incomplete
_DEPRECATED_SUPPORT_CLOSE_TILT: Incomplete
_DEPRECATED_SUPPORT_STOP_TILT: Incomplete
_DEPRECATED_SUPPORT_SET_TILT_POSITION: Incomplete
ATTR_CURRENT_POSITION: str
ATTR_CURRENT_TILT_POSITION: str
ATTR_POSITION: str
ATTR_TILT_POSITION: str

def is_closed(hass: HomeAssistant, entity_id: str) -> bool: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class CoverEntityDescription(EntityDescription, frozen_or_thawed=True):
    device_class: CoverDeviceClass | None
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement) -> None: ...

CACHED_PROPERTIES_WITH_ATTR_: Incomplete

class CoverEntity(Entity, cached_properties=CACHED_PROPERTIES_WITH_ATTR_):
    entity_description: CoverEntityDescription
    _attr_current_cover_position: int | None
    _attr_current_cover_tilt_position: int | None
    _attr_device_class: CoverDeviceClass | None
    _attr_is_closed: bool | None
    _attr_is_closing: bool | None
    _attr_is_opening: bool | None
    _attr_state: None
    _attr_supported_features: CoverEntityFeature | None
    _cover_is_last_toggle_direction_open: bool
    @cached_property
    def current_cover_position(self) -> int | None: ...
    @cached_property
    def current_cover_tilt_position(self) -> int | None: ...
    @cached_property
    def device_class(self) -> CoverDeviceClass | None: ...
    @property
    def state(self) -> str | None: ...
    @property
    def state_attributes(self) -> dict[str, Any]: ...
    @property
    def supported_features(self) -> CoverEntityFeature: ...
    @cached_property
    def is_opening(self) -> bool | None: ...
    @cached_property
    def is_closing(self) -> bool | None: ...
    @cached_property
    def is_closed(self) -> bool | None: ...
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

__getattr__: Incomplete
__dir__: Incomplete
__all__: Incomplete
