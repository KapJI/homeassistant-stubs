from .const import CONF_SW_VERSION as CONF_SW_VERSION, DOMAIN as DOMAIN, device_model_name as device_model_name
from .coordinator import EnergieleserConfigEntry as EnergieleserConfigEntry, EnergieleserCoordinator as EnergieleserCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from energieleser import GasleserDevice, GasleserPulseDevice, StromleserOneDevice, WaermeleserDevice, WasserleserDevice
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import CONF_HOST as CONF_HOST, EntityCategory as EntityCategory, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, UnitOfEnergy as UnitOfEnergy, UnitOfPower as UnitOfPower, UnitOfTemperature as UnitOfTemperature, UnitOfVolume as UnitOfVolume, UnitOfVolumeFlowRate as UnitOfVolumeFlowRate
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import override

PARALLEL_UPDATES: int
type AnyGasleserDevice = GasleserDevice | GasleserPulseDevice

@dataclass(frozen=True, kw_only=True)
class StromleserSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[StromleserOneDevice], StateType]
    unit_fn: Callable[[StromleserOneDevice], str | None] | None = ...
    present_fn: Callable[[StromleserOneDevice], bool] = ...

@dataclass(frozen=True, kw_only=True)
class GasleserSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[AnyGasleserDevice], StateType]
    present_fn: Callable[[AnyGasleserDevice], bool] = ...

@dataclass(frozen=True, kw_only=True)
class WasserleserSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[WasserleserDevice], StateType]
    present_fn: Callable[[WasserleserDevice], bool] = ...

@dataclass(frozen=True, kw_only=True)
class WaermeleserSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[WaermeleserDevice], StateType]
    present_fn: Callable[[WaermeleserDevice], bool] = ...

STROMLESER_SENSORS: tuple[StromleserSensorEntityDescription, ...]
GASLESER_SENSORS: tuple[GasleserSensorEntityDescription, ...]
WASSERLESER_SENSORS: tuple[WasserleserSensorEntityDescription, ...]
WAERMELESER_SENSORS: tuple[WaermeleserSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: EnergieleserConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class _EnergieleserSensorBase(CoordinatorEntity[EnergieleserCoordinator], SensorEntity):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: EnergieleserCoordinator, description: SensorEntityDescription) -> None: ...

class StromleserSensor(_EnergieleserSensorBase):
    entity_description: StromleserSensorEntityDescription
    @property
    @override
    def native_value(self) -> StateType: ...
    @property
    @override
    def native_unit_of_measurement(self) -> str | None: ...

class GasleserSensor(_EnergieleserSensorBase):
    entity_description: GasleserSensorEntityDescription
    @property
    @override
    def native_value(self) -> StateType: ...

class WasserleserSensor(_EnergieleserSensorBase):
    entity_description: WasserleserSensorEntityDescription
    @property
    @override
    def native_value(self) -> StateType: ...

class WaermeleserSensor(_EnergieleserSensorBase):
    entity_description: WaermeleserSensorEntityDescription
    @property
    @override
    def native_value(self) -> StateType: ...
