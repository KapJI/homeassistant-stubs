from .coordinator import LinearConfigEntry as LinearConfigEntry
from .entity import LinearEntity as LinearEntity
from _typeshed import Incomplete
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ColorMode as ColorMode, LightEntity as LightEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from linear_garage_door import Linear as Linear
from typing import Any

SUPPORTED_SUBDEVICES: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: LinearConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LinearLightEntity(LinearEntity, LightEntity):
    _attr_color_mode: Incomplete
    _attr_supported_color_modes: Incomplete
    _attr_translation_key: str
    @property
    def is_on(self) -> bool: ...
    @property
    def brightness(self) -> int | None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
