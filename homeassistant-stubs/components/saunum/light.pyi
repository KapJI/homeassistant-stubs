from . import LeilSaunaConfigEntry as LeilSaunaConfigEntry
from .const import DOMAIN as DOMAIN
from .coordinator import LeilSaunaCoordinator as LeilSaunaCoordinator
from .entity import LeilSaunaEntity as LeilSaunaEntity
from _typeshed import Incomplete
from homeassistant.components.light import ColorMode as ColorMode, LightEntity as LightEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: LeilSaunaConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LeilSaunaLight(LeilSaunaEntity, LightEntity):
    _attr_translation_key: str
    _attr_color_mode: Incomplete
    _attr_supported_color_modes: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: LeilSaunaCoordinator) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
