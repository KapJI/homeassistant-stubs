from .const import DEVICE_TYPE_TAGS as DEVICE_TYPE_TAGS, DISABLED_TEMP_ENTITIES as DISABLED_TEMP_ENTITIES, DOMAIN as DOMAIN, MieleAppliance as MieleAppliance
from .coordinator import MieleConfigEntry as MieleConfigEntry, MieleDataUpdateCoordinator as MieleDataUpdateCoordinator
from .entity import MieleEntity as MieleEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityDescription as ClimateEntityDescription, ClimateEntityFeature as ClimateEntityFeature, HVACMode as HVACMode
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, PRECISION_WHOLE as PRECISION_WHOLE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from pymiele import MieleDevice as MieleDevice, MieleTemperature as MieleTemperature
from typing import Any, Final

PARALLEL_UPDATES: int
_LOGGER: Incomplete

def _get_temperature_value(temperatures: list[MieleTemperature], index: int) -> float | None: ...

@dataclass(frozen=True, kw_only=True)
class MieleClimateDescription(ClimateEntityDescription):
    value_fn: Callable[[MieleDevice], StateType]
    target_fn: Callable[[MieleDevice], StateType]
    zone: int = ...

@dataclass
class MieleClimateDefinition:
    types: tuple[MieleAppliance, ...]
    description: MieleClimateDescription

CLIMATE_TYPES: Final[tuple[MieleClimateDefinition, ...]]
ZONE1_DEVICES: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: MieleConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class MieleClimate(MieleEntity, ClimateEntity):
    entity_description: MieleClimateDescription
    _attr_precision = PRECISION_WHOLE
    _attr_temperature_unit: Incomplete
    _attr_target_temperature_step: float
    _attr_hvac_modes: Incomplete
    _attr_hvac_mode: Incomplete
    _attr_supported_features: Incomplete
    @property
    def current_temperature(self) -> float | None: ...
    _attr_name: Incomplete
    _attr_translation_key: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: MieleDataUpdateCoordinator, device_id: str, description: MieleClimateDescription) -> None: ...
    @property
    def target_temperature(self) -> float | None: ...
    @property
    def max_temp(self) -> float: ...
    @property
    def min_temp(self) -> float: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
