from . import WithingsConfigEntry as WithingsConfigEntry
from .const import DOMAIN as DOMAIN, LOGGER as LOGGER, SCORE_POINTS as SCORE_POINTS, UOM_BEATS_PER_MINUTE as UOM_BEATS_PER_MINUTE, UOM_BREATHS_PER_MINUTE as UOM_BREATHS_PER_MINUTE, UOM_FREQUENCY as UOM_FREQUENCY, UOM_MMHG as UOM_MMHG
from .coordinator import WithingsActivityDataUpdateCoordinator as WithingsActivityDataUpdateCoordinator, WithingsDataUpdateCoordinator as WithingsDataUpdateCoordinator, WithingsGoalsDataUpdateCoordinator as WithingsGoalsDataUpdateCoordinator, WithingsMeasurementDataUpdateCoordinator as WithingsMeasurementDataUpdateCoordinator, WithingsSleepDataUpdateCoordinator as WithingsSleepDataUpdateCoordinator, WithingsWorkoutDataUpdateCoordinator as WithingsWorkoutDataUpdateCoordinator
from .entity import WithingsEntity as WithingsEntity
from _typeshed import Incomplete
from aiowithings import Activity as Activity, Goals as Goals, MeasurementPosition, MeasurementType, SleepSummary as SleepSummary, Workout as Workout
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import PERCENTAGE as PERCENTAGE, Platform as Platform, UnitOfLength as UnitOfLength, UnitOfMass as UnitOfMass, UnitOfSpeed as UnitOfSpeed, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType

@dataclass(frozen=True, kw_only=True)
class WithingsMeasurementSensorEntityDescription(SensorEntityDescription):
    measurement_type: MeasurementType
    measurement_position: MeasurementPosition | None = ...
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, measurement_type, measurement_position) -> None: ...

MEASUREMENT_SENSORS: dict[MeasurementType, WithingsMeasurementSensorEntityDescription]

def get_positional_measurement_description(measurement_type: MeasurementType, measurement_position: MeasurementPosition) -> WithingsMeasurementSensorEntityDescription | None: ...
def get_measurement_description(measurement: tuple[MeasurementType, MeasurementPosition | None]) -> WithingsMeasurementSensorEntityDescription | None: ...

@dataclass(frozen=True, kw_only=True)
class WithingsSleepSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[SleepSummary], StateType]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, value_fn) -> None: ...

SLEEP_SENSORS: Incomplete

@dataclass(frozen=True, kw_only=True)
class WithingsActivitySensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[Activity], StateType]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, value_fn) -> None: ...

ACTIVITY_SENSORS: Incomplete
STEP_GOAL: str
SLEEP_GOAL: str
WEIGHT_GOAL: str

@dataclass(frozen=True, kw_only=True)
class WithingsGoalsSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[Goals], StateType]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, value_fn) -> None: ...

GOALS_SENSORS: dict[str, WithingsGoalsSensorEntityDescription]

@dataclass(frozen=True, kw_only=True)
class WithingsWorkoutSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[Workout], StateType]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, value_fn) -> None: ...

_WORKOUT_CATEGORY: Incomplete
WORKOUT_SENSORS: Incomplete

def get_current_goals(goals: Goals) -> set[str]: ...
async def async_setup_entry(hass: HomeAssistant, entry: WithingsConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class WithingsSensor(WithingsEntity[_T], SensorEntity):
    entity_description: _ED
    def __init__(self, coordinator: _T, entity_description: _ED) -> None: ...

class WithingsMeasurementSensor(WithingsSensor[WithingsMeasurementDataUpdateCoordinator, WithingsMeasurementSensorEntityDescription]):
    @property
    def native_value(self) -> float: ...
    @property
    def available(self) -> bool: ...

class WithingsSleepSensor(WithingsSensor[WithingsSleepDataUpdateCoordinator, WithingsSleepSensorEntityDescription]):
    @property
    def native_value(self) -> StateType: ...

class WithingsGoalsSensor(WithingsSensor[WithingsGoalsDataUpdateCoordinator, WithingsGoalsSensorEntityDescription]):
    @property
    def native_value(self) -> StateType: ...

class WithingsActivitySensor(WithingsSensor[WithingsActivityDataUpdateCoordinator, WithingsActivitySensorEntityDescription]):
    @property
    def native_value(self) -> StateType: ...
    @property
    def last_reset(self) -> datetime: ...

class WithingsWorkoutSensor(WithingsSensor[WithingsWorkoutDataUpdateCoordinator, WithingsWorkoutSensorEntityDescription]):
    @property
    def native_value(self) -> StateType: ...
