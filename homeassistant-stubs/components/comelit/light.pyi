from .coordinator import ComelitConfigEntry as ComelitConfigEntry, ComelitSerialBridge as ComelitSerialBridge
from .entity import ComelitBridgeBaseEntity as ComelitBridgeBaseEntity
from _typeshed import Incomplete
from homeassistant.components.light import ColorMode as ColorMode, LightEntity as LightEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: ComelitConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ComelitLightEntity(ComelitBridgeBaseEntity, LightEntity):
    _attr_color_mode: Incomplete
    _attr_name: Incomplete
    _attr_supported_color_modes: Incomplete
    async def _light_set_state(self, state: int) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @property
    def is_on(self) -> bool: ...
