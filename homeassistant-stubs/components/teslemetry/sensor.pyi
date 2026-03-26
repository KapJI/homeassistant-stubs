from . import TeslemetryConfigEntry as TeslemetryConfigEntry
from .const import ENERGY_HISTORY_FIELDS as ENERGY_HISTORY_FIELDS
from .entity import TeslemetryEnergyHistoryEntity as TeslemetryEnergyHistoryEntity, TeslemetryEnergyInfoEntity as TeslemetryEnergyInfoEntity, TeslemetryEnergyLiveEntity as TeslemetryEnergyLiveEntity, TeslemetryVehiclePollingEntity as TeslemetryVehiclePollingEntity, TeslemetryVehicleStreamEntity as TeslemetryVehicleStreamEntity, TeslemetryWallConnectorEntity as TeslemetryWallConnectorEntity
from .models import TeslemetryEnergyData as TeslemetryEnergyData, TeslemetryVehicleData as TeslemetryVehicleData
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import RestoreSensor as RestoreSensor, SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import DEGREE as DEGREE, EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfLength as UnitOfLength, UnitOfPower as UnitOfPower, UnitOfPressure as UnitOfPressure, UnitOfSpeed as UnitOfSpeed, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.util.variance import ignore_variance as ignore_variance
from teslemetry_stream import TeslemetryStream as TeslemetryStream, TeslemetryStreamVehicle as TeslemetryStreamVehicle

PARALLEL_UPDATES: int
BMS_STATES: Incomplete
CHARGE_STATES: Incomplete
DRIVE_INVERTER_STATES: Incomplete
SHIFT_STATES: Incomplete
SENTRY_MODE_STATES: Incomplete
POWER_SHARE_STATES: Incomplete
POWER_SHARE_STOP_REASONS: Incomplete
POWER_SHARE_TYPES: Incomplete
CHARGE_CABLE_TYPES: Incomplete
FORWARD_COLLISION_SENSITIVITIES: Incomplete
GUEST_MODE_MOBILE_ACCESS_STATES: Incomplete
HVAC_POWER_STATES: Incomplete
LANE_ASSIST_LEVELS: Incomplete
SCHEDULED_CHARGING_MODES: Incomplete
SPEED_ASSIST_LEVELS: Incomplete
TONNEAU_TENT_MODE_STATES: Incomplete
TURN_SIGNAL_STATES: Incomplete

@dataclass(frozen=True, kw_only=True)
class TeslemetryVehicleSensorEntityDescription(SensorEntityDescription):
    polling: bool = ...
    polling_value_fn: Callable[[StateType], StateType] = ...
    nullable: bool = ...
    streaming_listener: Callable[[TeslemetryStreamVehicle, Callable[[StateType], None]], Callable[[], None]] | None = ...
    streaming_firmware: str = ...

VEHICLE_DESCRIPTIONS: tuple[TeslemetryVehicleSensorEntityDescription, ...]

@dataclass(frozen=True, kw_only=True)
class TeslemetryTimeEntityDescription(SensorEntityDescription):
    variance: int
    streaming_listener: Callable[[TeslemetryStreamVehicle, Callable[[float | None], None]], Callable[[], None]]
    streaming_firmware: str = ...
    streaming_unit: str

VEHICLE_TIME_DESCRIPTIONS: tuple[TeslemetryTimeEntityDescription, ...]

@dataclass(frozen=True, kw_only=True)
class TeslemetryEnergySensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[StateType], StateType | datetime] = ...

ENERGY_LIVE_DESCRIPTIONS: tuple[TeslemetryEnergySensorEntityDescription, ...]

@dataclass(frozen=True, kw_only=True)
class TeslemetrySensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[StateType], StateType] = ...

WALL_CONNECTOR_DESCRIPTIONS: tuple[TeslemetrySensorEntityDescription, ...]
ENERGY_INFO_DESCRIPTIONS: tuple[SensorEntityDescription, ...]
ENERGY_HISTORY_DESCRIPTIONS: tuple[SensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: TeslemetryConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class TeslemetryStreamSensorEntity(TeslemetryVehicleStreamEntity, RestoreSensor):
    entity_description: TeslemetryVehicleSensorEntityDescription
    def __init__(self, data: TeslemetryVehicleData, description: TeslemetryVehicleSensorEntityDescription) -> None: ...
    _attr_native_value: Incomplete
    async def async_added_to_hass(self) -> None: ...
    def _async_value_from_stream(self, value: StateType) -> None: ...

class TeslemetryVehicleSensorEntity(TeslemetryVehiclePollingEntity, SensorEntity):
    entity_description: TeslemetryVehicleSensorEntityDescription
    def __init__(self, data: TeslemetryVehicleData, description: TeslemetryVehicleSensorEntityDescription) -> None: ...
    _attr_available: bool
    _attr_native_value: Incomplete
    def _async_update_attrs(self) -> None: ...

class TeslemetryStreamTimeSensorEntity(TeslemetryVehicleStreamEntity, SensorEntity):
    entity_description: TeslemetryTimeEntityDescription
    _get_timestamp: Incomplete
    def __init__(self, data: TeslemetryVehicleData, description: TeslemetryTimeEntityDescription) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    _attr_native_value: Incomplete
    def _value_callback(self, value: float | None) -> None: ...

class TeslemetryVehicleTimeSensorEntity(TeslemetryVehiclePollingEntity, SensorEntity):
    entity_description: TeslemetryTimeEntityDescription
    _get_timestamp: Incomplete
    def __init__(self, data: TeslemetryVehicleData, description: TeslemetryTimeEntityDescription) -> None: ...
    _attr_available: Incomplete
    _attr_native_value: Incomplete
    def _async_update_attrs(self) -> None: ...

class TeslemetryEnergyLiveSensorEntity(TeslemetryEnergyLiveEntity, SensorEntity):
    entity_description: TeslemetryEnergySensorEntityDescription
    def __init__(self, data: TeslemetryEnergyData, description: TeslemetryEnergySensorEntityDescription) -> None: ...
    _attr_available: Incomplete
    _attr_native_value: Incomplete
    def _async_update_attrs(self) -> None: ...

class TeslemetryWallConnectorSensorEntity(TeslemetryWallConnectorEntity, SensorEntity):
    entity_description: TeslemetrySensorEntityDescription
    def __init__(self, data: TeslemetryEnergyData, din: str, description: TeslemetrySensorEntityDescription) -> None: ...
    _attr_native_value: Incomplete
    def _async_update_attrs(self) -> None: ...

class TeslemetryEnergyInfoSensorEntity(TeslemetryEnergyInfoEntity, SensorEntity):
    entity_description: SensorEntityDescription
    def __init__(self, data: TeslemetryEnergyData, description: SensorEntityDescription) -> None: ...
    _attr_available: Incomplete
    _attr_native_value: Incomplete
    def _async_update_attrs(self) -> None: ...

class TeslemetryEnergyHistorySensorEntity(TeslemetryEnergyHistoryEntity, SensorEntity):
    entity_description: SensorEntityDescription
    def __init__(self, data: TeslemetryEnergyData, description: SensorEntityDescription) -> None: ...
    _attr_native_value: Incomplete
    def _async_update_attrs(self) -> None: ...

class TeslemetryCreditBalanceSensor(RestoreSensor):
    _attr_has_entity_name: bool
    stream: TeslemetryStream
    _attr_state_class: Incomplete
    _attr_suggested_display_precision: int
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    def __init__(self, uid: str, stream: TeslemetryStream) -> None: ...
    _attr_native_value: Incomplete
    async def async_added_to_hass(self) -> None: ...
    def _async_update(self, value: int) -> None: ...
