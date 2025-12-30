from .entity import MatterEntity as MatterEntity, MatterEntityDescription as MatterEntityDescription
from .helpers import get_matter as get_matter
from .models import MatterDiscoverySchema as MatterDiscoverySchema
from _typeshed import Incomplete
from chip.clusters.ClusterObjects import ClusterAttributeDescriptor as ClusterAttributeDescriptor
from chip.clusters.Types import Nullable as Nullable
from dataclasses import dataclass, field
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONCENTRATION_MICROGRAMS_PER_CUBIC_METER as CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, EntityCategory as EntityCategory, LIGHT_LUX as LIGHT_LUX, PERCENTAGE as PERCENTAGE, Platform as Platform, REVOLUTIONS_PER_MINUTE as REVOLUTIONS_PER_MINUTE, UnitOfApparentPower as UnitOfApparentPower, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfPower as UnitOfPower, UnitOfPressure as UnitOfPressure, UnitOfReactivePower as UnitOfReactivePower, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime, UnitOfVolume as UnitOfVolume, UnitOfVolumeFlowRate as UnitOfVolumeFlowRate
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.util import slugify as slugify

AIR_QUALITY_MAP: Incomplete
CONTAMINATION_STATE_MAP: Incomplete
EVE_CLUSTER_WEATHER_MAP: Incomplete
OPERATIONAL_STATE_MAP: Incomplete
OPERATIONAL_STATE_ERROR_MAP: Incomplete
RVC_OPERATIONAL_STATE_MAP: Incomplete
RVC_OPERATIONAL_STATE_ERROR_MAP: Incomplete
BOOST_STATE_MAP: Incomplete
CHARGE_STATE_MAP: Incomplete
DEM_OPT_OUT_STATE_MAP: Incomplete
ESA_STATE_MAP: Incomplete
EVSE_FAULT_STATE_MAP: Incomplete
PUMP_CONTROL_MODE_MAP: Incomplete
MATTER_2000_TO_UNIX_EPOCH_OFFSET: int
HUMIDITY_SCALING_FACTOR: int
TEMPERATURE_SCALING_FACTOR: int

def matter_epoch_seconds_to_utc(x: int | None) -> datetime | None: ...
def matter_epoch_microseconds_to_utc(x: int | None) -> datetime | None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

@dataclass(frozen=True, kw_only=True)
class MatterSensorEntityDescription(SensorEntityDescription, MatterEntityDescription): ...

@dataclass(frozen=True, kw_only=True)
class MatterListSensorEntityDescription(MatterSensorEntityDescription):
    list_attribute: type[ClusterAttributeDescriptor]

@dataclass(frozen=True, kw_only=True)
class MatterOperationalStateSensorEntityDescription(MatterSensorEntityDescription):
    state_list_attribute: type[ClusterAttributeDescriptor] = ...
    state_attribute: type[ClusterAttributeDescriptor] = ...
    state_map: dict[int, str] = field(default_factory=Incomplete)

class MatterSensor(MatterEntity, SensorEntity):
    entity_description: MatterSensorEntityDescription
    _attr_native_value: Incomplete
    @callback
    def _update_from_device(self) -> None: ...

class MatterDraftElectricalMeasurementSensor(MatterEntity, SensorEntity):
    entity_description: MatterSensorEntityDescription
    _attr_native_value: Incomplete
    @callback
    def _update_from_device(self) -> None: ...

class MatterOperationalStateSensor(MatterSensor):
    entity_description: MatterOperationalStateSensorEntityDescription
    states_map: dict[int, str]
    _attr_options: Incomplete
    _attr_native_value: Incomplete
    @callback
    def _update_from_device(self) -> None: ...

class MatterListSensor(MatterSensor):
    entity_description: MatterListSensorEntityDescription
    _attr_device_class: Incomplete
    _attr_options: Incomplete
    _attr_native_value: Incomplete
    @callback
    def _update_from_device(self) -> None: ...

DISCOVERY_SCHEMAS: Incomplete
