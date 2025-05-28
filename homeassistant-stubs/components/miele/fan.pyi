from .const import DOMAIN as DOMAIN, MieleAppliance as MieleAppliance, POWER_OFF as POWER_OFF, POWER_ON as POWER_ON, VENTILATION_STEP as VENTILATION_STEP
from .coordinator import MieleConfigEntry as MieleConfigEntry, MieleDataUpdateCoordinator as MieleDataUpdateCoordinator
from .entity import MieleEntity as MieleEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.fan import FanEntity as FanEntity, FanEntityDescription as FanEntityDescription, FanEntityFeature as FanEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.util.percentage import percentage_to_ranged_value as percentage_to_ranged_value, ranged_value_to_percentage as ranged_value_to_percentage
from homeassistant.util.scaling import int_states_in_range as int_states_in_range
from typing import Any, Final

PARALLEL_UPDATES: int
_LOGGER: Incomplete
SPEED_RANGE: Incomplete

@dataclass(frozen=True, kw_only=True)
class MieleFanDefinition:
    types: tuple[MieleAppliance, ...]
    description: FanEntityDescription

FAN_TYPES: Final[tuple[MieleFanDefinition, ...]]

async def async_setup_entry(hass: HomeAssistant, config_entry: MieleConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class MieleFan(MieleEntity, FanEntity):
    entity_description: FanEntityDescription
    _attr_supported_features: FanEntityFeature
    def __init__(self, coordinator: MieleDataUpdateCoordinator, device_id: str, description: FanEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def speed_count(self) -> int: ...
    @property
    def percentage(self) -> int | None: ...
    async def async_set_percentage(self, percentage: int) -> None: ...
    async def async_turn_on(self, percentage: int | None = None, preset_mode: str | None = None, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
