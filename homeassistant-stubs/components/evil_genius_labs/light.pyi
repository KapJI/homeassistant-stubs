from .coordinator import EvilGeniusConfigEntry as EvilGeniusConfigEntry, EvilGeniusUpdateCoordinator as EvilGeniusUpdateCoordinator
from .entity import EvilGeniusEntity as EvilGeniusEntity
from .util import update_when_done as update_when_done
from _typeshed import Incomplete
from homeassistant.components import light as light
from homeassistant.components.light import ColorMode as ColorMode, LightEntity as LightEntity, LightEntityFeature as LightEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, override

HA_NO_EFFECT: str
FIB_NO_EFFECT: str

async def async_setup_entry(hass: HomeAssistant, config_entry: EvilGeniusConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class EvilGeniusLight(EvilGeniusEntity, LightEntity):
    _attr_name: Incomplete
    _attr_supported_features: Incomplete
    _attr_supported_color_modes: Incomplete
    _attr_color_mode: Incomplete
    _attr_unique_id: Incomplete
    _attr_effect_list: Incomplete
    def __init__(self, coordinator: EvilGeniusUpdateCoordinator) -> None: ...
    @property
    @override
    def is_on(self) -> bool: ...
    @property
    @override
    def brightness(self) -> int: ...
    @property
    @override
    def rgb_color(self) -> tuple[int, int, int]: ...
    @property
    @override
    def effect(self) -> str: ...
    @update_when_done
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @update_when_done
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
