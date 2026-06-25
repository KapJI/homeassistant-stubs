from .coordinator import SkybellConfigEntry as SkybellConfigEntry
from .entity import SkybellEntity as SkybellEntity
from _typeshed import Incomplete
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_RGB_COLOR as ATTR_RGB_COLOR, ColorMode as ColorMode, LightEntity as LightEntity, LightEntityDescription as LightEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, override

async def async_setup_entry(hass: HomeAssistant, entry: SkybellConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SkybellLight(SkybellEntity, LightEntity):
    _attr_color_mode: Incomplete
    _attr_supported_color_modes: Incomplete
    _attr_name: Incomplete
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @property
    @override
    def is_on(self) -> bool: ...
    @property
    @override
    def brightness(self) -> int: ...
    @property
    @override
    def rgb_color(self) -> tuple[int, int, int] | None: ...
