from .const import COFFEE_SYSTEM_PROFILE as COFFEE_SYSTEM_PROFILE, DISABLED_TEMP_ENTITIES as DISABLED_TEMP_ENTITIES, DOMAIN as DOMAIN, MieleAppliance as MieleAppliance, PROGRAM_IDS as PROGRAM_IDS, PROGRAM_PHASE as PROGRAM_PHASE, PlatePowerStep as PlatePowerStep, StateDryingStep as StateDryingStep, StateProgramType as StateProgramType, StateStatus as StateStatus
from .coordinator import MieleConfigEntry as MieleConfigEntry, MieleDataUpdateCoordinator as MieleDataUpdateCoordinator
from .entity import MieleEntity as MieleEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Mapping
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import RestoreSensor as RestoreSensor, SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, REVOLUTIONS_PER_MINUTE as REVOLUTIONS_PER_MINUTE, UnitOfEnergy as UnitOfEnergy, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime, UnitOfVolume as UnitOfVolume
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from pymiele import MieleDevice as MieleDevice, MieleTemperature as MieleTemperature
from typing import Any, Final

PARALLEL_UPDATES: int
_LOGGER: Incomplete
DEFAULT_PLATE_COUNT: int
PLATE_COUNT: Incomplete
ATTRIBUTE_PROFILE: str

def _get_plate_count(tech_type: str) -> int: ...
def _convert_duration(value_list: list[int]) -> int | None: ...
def _convert_temperature(value_list: list[MieleTemperature], index: int) -> float | None: ...
def _get_coffee_profile(value: MieleDevice) -> str | None: ...
def _convert_start_timestamp(elapsed_time_list: list[int], start_time_list: list[int]) -> datetime | None: ...
def _convert_finish_timestamp(remaining_time_list: list[int], start_time_list: list[int]) -> datetime | None: ...

@dataclass(frozen=True, kw_only=True)
class MieleSensorDescription(SensorEntityDescription):
    value_fn: Callable[[MieleDevice], StateType | datetime]
    end_value_fn: Callable[[StateType | datetime], StateType | datetime] | None = ...
    extra_attributes: dict[str, Callable[[MieleDevice], StateType]] | None = ...
    zone: int | None = ...
    unique_id_fn: Callable[[str, MieleSensorDescription], str] | None = ...

@dataclass
class MieleSensorDefinition:
    types: tuple[MieleAppliance, ...]
    description: MieleSensorDescription

SENSOR_TYPES: Final[tuple[MieleSensorDefinition, ...]]

async def async_setup_entry(hass: HomeAssistant, config_entry: MieleConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

APPLIANCE_ICONS: Incomplete

class MieleSensor(MieleEntity, SensorEntity):
    entity_description: MieleSensorDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: MieleDataUpdateCoordinator, device_id: str, description: MieleSensorDescription) -> None: ...
    @property
    def native_value(self) -> StateType | datetime: ...
    @property
    def extra_state_attributes(self) -> Mapping[str, Any] | None: ...

class MieleRestorableSensor(MieleSensor, RestoreSensor):
    _attr_native_value: StateType | datetime
    async def async_added_to_hass(self) -> None: ...
    @property
    def native_value(self) -> StateType | datetime: ...
    def _update_native_value(self) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...

class MielePlateSensor(MieleSensor):
    entity_description: MieleSensorDescription
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

PROGRAM_PHASE_TRANSLATION: Incomplete

class MielePhaseSensor(MieleSensor):
    @property
    def native_value(self) -> StateType: ...
    @property
    def options(self) -> list[str]: ...

class MieleProgramIdSensor(MieleSensor):
    _unrecorded_attributes: Incomplete
    @property
    def native_value(self) -> StateType: ...
    @property
    def options(self) -> list[str]: ...

class MieleTimeSensor(MieleRestorableSensor):
    _attr_native_value: Incomplete
    def _update_native_value(self) -> None: ...

class MieleAbsoluteTimeSensor(MieleRestorableSensor):
    _previous_value: StateType | datetime
    _attr_native_value: Incomplete
    def _update_native_value(self) -> None: ...

class MieleConsumptionSensor(MieleRestorableSensor):
    _is_reporting: bool
    _attr_native_value: Incomplete
    def _update_native_value(self) -> None: ...
