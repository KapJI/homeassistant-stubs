from .const import AMBIENT_LIGHT as AMBIENT_LIGHT, DOMAIN as DOMAIN, LIGHT as LIGHT, LIGHT_OFF as LIGHT_OFF, LIGHT_ON as LIGHT_ON, MieleAppliance as MieleAppliance
from .coordinator import MieleConfigEntry as MieleConfigEntry
from .entity import MieleDevice as MieleDevice, MieleEntity as MieleEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.light import ColorMode as ColorMode, LightEntity as LightEntity, LightEntityDescription as LightEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from typing import Any, Final

PARALLEL_UPDATES: int
_LOGGER: Incomplete

@dataclass(frozen=True, kw_only=True)
class MieleLightDescription(LightEntityDescription):
    value_fn: Callable[[MieleDevice], StateType]
    light_type: str

@dataclass
class MieleLightDefinition:
    types: tuple[MieleAppliance, ...]
    description: MieleLightDescription

LIGHT_TYPES: Final[tuple[MieleLightDefinition, ...]]

async def async_setup_entry(hass: HomeAssistant, config_entry: MieleConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class MieleLight(MieleEntity, LightEntity):
    entity_description: MieleLightDescription
    _attr_color_mode: Incomplete
    _attr_supported_color_modes: Incomplete
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_turn_light(self, mode: int) -> None: ...
