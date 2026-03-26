from .const import CONFIG_LIGHT as CONFIG_LIGHT, CONFIG_STEAMER_AND_LIGHT as CONFIG_STEAMER_AND_LIGHT
from .coordinator import HuumConfigEntry as HuumConfigEntry, HuumDataUpdateCoordinator as HuumDataUpdateCoordinator
from .entity import HuumBaseEntity as HuumBaseEntity
from _typeshed import Incomplete
from homeassistant.components.light import ColorMode as ColorMode, LightEntity as LightEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

_LOGGER: Incomplete
PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: HuumConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HuumLight(HuumBaseEntity, LightEntity):
    _attr_translation_key: str
    _attr_supported_color_modes: Incomplete
    _attr_color_mode: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: HuumDataUpdateCoordinator) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def _toggle_light(self) -> None: ...
