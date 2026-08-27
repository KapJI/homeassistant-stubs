from .coordinator import HotSpringConfigEntry as HotSpringConfigEntry, HotSpringDataUpdateCoordinator as HotSpringDataUpdateCoordinator
from .entity import HotSpringEntity as HotSpringEntity
from .helpers import hotspring_exception_handler as hotspring_exception_handler
from _typeshed import Incomplete
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_RGB_COLOR as ATTR_RGB_COLOR, ColorMode as ColorMode, LightEntity as LightEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.util.color import brightness_to_value as brightness_to_value, value_to_brightness as value_to_brightness
from hotspring import LightColor, LightZone as LightZone
from typing import Any, override

PARALLEL_UPDATES: int
LIGHT_COLOR_TO_RGB: dict[LightColor, tuple[int, int, int]]

async def async_setup_entry(hass: HomeAssistant, entry: HotSpringConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HotSpringLightEntity(HotSpringEntity, LightEntity):
    _attr_color_mode: Incomplete
    _attr_supported_color_modes: Incomplete
    _attr_translation_key: str
    _zone_id: Incomplete
    _attr_translation_placeholders: Incomplete
    def __init__(self, coordinator: HotSpringDataUpdateCoordinator, zone_id: int) -> None: ...
    @property
    def _zone(self) -> LightZone: ...
    @property
    @override
    def is_on(self) -> bool: ...
    @property
    @override
    def brightness(self) -> int | None: ...
    @property
    @override
    def rgb_color(self) -> tuple[int, int, int] | None: ...
    @hotspring_exception_handler
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @hotspring_exception_handler
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
