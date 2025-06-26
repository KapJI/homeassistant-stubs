from .const import MieleAppliance as MieleAppliance, PlatePowerStep as PlatePowerStep, STATE_PROGRAM_ID as STATE_PROGRAM_ID, STATE_PROGRAM_PHASE as STATE_PROGRAM_PHASE, STATE_STATUS_TAGS as STATE_STATUS_TAGS, StateDryingStep as StateDryingStep, StateProgramType as StateProgramType, StateStatus as StateStatus
from .coordinator import MieleConfigEntry as MieleConfigEntry, MieleDataUpdateCoordinator as MieleDataUpdateCoordinator
from .entity import MieleEntity as MieleEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, REVOLUTIONS_PER_MINUTE as REVOLUTIONS_PER_MINUTE, UnitOfEnergy as UnitOfEnergy, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime, UnitOfVolume as UnitOfVolume
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from pymiele import MieleDevice as MieleDevice
from typing import Final

PARALLEL_UPDATES: int
_LOGGER: Incomplete
DISABLED_TEMPERATURE: int
DEFAULT_PLATE_COUNT: int
PLATE_COUNT: Incomplete

def _get_plate_count(tech_type: str) -> int: ...
def _convert_duration(value_list: list[int]) -> int | None: ...

@dataclass(frozen=True, kw_only=True)
class MieleSensorDescription(SensorEntityDescription):
    value_fn: Callable[[MieleDevice], StateType]
    zone: int = ...

@dataclass
class MieleSensorDefinition:
    types: tuple[MieleAppliance, ...]
    description: MieleSensorDescription

SENSOR_TYPES: Final[tuple[MieleSensorDefinition, ...]]

async def async_setup_entry(hass: HomeAssistant, config_entry: MieleConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

APPLIANCE_ICONS: Incomplete

class MieleSensor(MieleEntity, SensorEntity):
    entity_description: MieleSensorDescription
    @property
    def native_value(self) -> StateType: ...

class MielePlateSensor(MieleSensor):
    entity_description: MieleSensorDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: MieleDataUpdateCoordinator, device_id: str, description: MieleSensorDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...

class MieleStatusSensor(MieleSensor):
    _attr_name: Incomplete
    _attr_icon: Incomplete
    def __init__(self, coordinator: MieleDataUpdateCoordinator, device_id: str, description: MieleSensorDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
    @property
    def available(self) -> bool: ...

class MielePhaseSensor(MieleSensor):
    @property
    def native_value(self) -> StateType: ...
    @property
    def options(self) -> list[str]: ...

class MieleProgramIdSensor(MieleSensor):
    @property
    def native_value(self) -> StateType: ...
    @property
    def options(self) -> list[str]: ...
