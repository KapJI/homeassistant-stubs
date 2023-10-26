from .const import ATTR_COLOR_PRIMARY as ATTR_COLOR_PRIMARY, ATTR_ON as ATTR_ON, ATTR_SEGMENT_ID as ATTR_SEGMENT_ID, DOMAIN as DOMAIN
from .coordinator import WLEDDataUpdateCoordinator as WLEDDataUpdateCoordinator
from .helpers import wled_exception_handler as wled_exception_handler
from .models import WLEDEntity as WLEDEntity
from _typeshed import Incomplete
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_EFFECT as ATTR_EFFECT, ATTR_RGBW_COLOR as ATTR_RGBW_COLOR, ATTR_RGB_COLOR as ATTR_RGB_COLOR, ATTR_TRANSITION as ATTR_TRANSITION, ColorMode as ColorMode, LightEntity as LightEntity, LightEntityFeature as LightEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class WLEDMainLight(WLEDEntity, LightEntity):
    _attr_color_mode: Incomplete
    _attr_icon: str
    _attr_translation_key: str
    _attr_supported_features: Incomplete
    _attr_supported_color_modes: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: WLEDDataUpdateCoordinator) -> None: ...
    @property
    def brightness(self) -> int | None: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def available(self) -> bool: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...

class WLEDSegmentLight(WLEDEntity, LightEntity):
    _attr_supported_features: Incomplete
    _attr_icon: str
    _rgbw: Incomplete
    _wv: Incomplete
    _segment: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_color_mode: Incomplete
    _attr_supported_color_modes: Incomplete
    def __init__(self, coordinator: WLEDDataUpdateCoordinator, segment: int) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def rgb_color(self) -> tuple[int, int, int] | None: ...
    @property
    def rgbw_color(self) -> tuple[int, int, int, int] | None: ...
    @property
    def effect(self) -> str | None: ...
    @property
    def brightness(self) -> int | None: ...
    @property
    def effect_list(self) -> list[str]: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...

def async_update_segments(coordinator: WLEDDataUpdateCoordinator, current_ids: set[int], async_add_entities: AddEntitiesCallback) -> None: ...
