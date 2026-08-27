from .const import CONF_USE_LIGHT as CONF_USE_LIGHT, DOMAIN as DOMAIN
from .coordinator import NeoPoolConfigEntry as NeoPoolConfigEntry, NeoPoolCoordinator as NeoPoolCoordinator
from .entity import NeoPoolEntity as NeoPoolEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.light import ColorMode as ColorMode, LightEntity as LightEntity, LightEntityDescription as LightEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, override

PARALLEL_UPDATES: int
_LIGHT_TIMER_ENABLE_KEY: str

@dataclass(frozen=True, kw_only=True)
class NeoPoolLightEntityDescription(LightEntityDescription):
    supported_fn: Callable[[dict[str, Any]], bool] | None = ...

LIGHT_DESCRIPTIONS: dict[str, NeoPoolLightEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: NeoPoolConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class NeoPoolLight(NeoPoolEntity, LightEntity):
    entity_description: NeoPoolLightEntityDescription
    _attr_supported_color_modes: Incomplete
    _attr_color_mode: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: NeoPoolCoordinator, key: str, description: NeoPoolLightEntityDescription) -> None: ...
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def _async_set_state(self, state: bool) -> None: ...
    @property
    @override
    def is_on(self) -> bool: ...
