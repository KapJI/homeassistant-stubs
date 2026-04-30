from .const import DOMAIN as DOMAIN
from .coordinator import LiebherrConfigEntry as LiebherrConfigEntry, LiebherrCoordinator as LiebherrCoordinator
from .entity import LiebherrEntity as LiebherrEntity
from _typeshed import Incomplete
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ColorMode as ColorMode, LightEntity as LightEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyliebherrhomeapi import PresentationLightControl
from typing import Any

PARALLEL_UPDATES: int

def _create_light_entities(coordinators: list[LiebherrCoordinator]) -> list[LiebherrPresentationLight]: ...
async def async_setup_entry(hass: HomeAssistant, entry: LiebherrConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LiebherrPresentationLight(LiebherrEntity, LightEntity):
    _attr_translation_key: str
    _attr_color_mode: Incomplete
    _attr_supported_color_modes: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: LiebherrCoordinator) -> None: ...
    @property
    def _light_control(self) -> PresentationLightControl | None: ...
    @property
    def available(self) -> bool: ...
    @property
    def is_on(self) -> bool | None: ...
    @property
    def brightness(self) -> int | None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
