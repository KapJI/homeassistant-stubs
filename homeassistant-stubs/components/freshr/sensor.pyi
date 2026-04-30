from .coordinator import FreshrConfigEntry as FreshrConfigEntry, FreshrReadingsCoordinator as FreshrReadingsCoordinator
from .entity import FreshrEntity as FreshrEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass, StateType as StateType
from homeassistant.const import CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, PERCENTAGE as PERCENTAGE, UnitOfTemperature as UnitOfTemperature, UnitOfVolumeFlowRate as UnitOfVolumeFlowRate
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyfreshr.models import DeviceReadings as DeviceReadings, DeviceType

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class FreshrSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[DeviceReadings], StateType]

_T1: Incomplete
_T2: Incomplete
_CO2: Incomplete
_HUM: Incomplete
_FLOW: Incomplete
_DP: Incomplete
_TEMP: Incomplete
SENSOR_TYPES: dict[DeviceType, tuple[FreshrSensorEntityDescription, ...]]

async def async_setup_entry(hass: HomeAssistant, config_entry: FreshrConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class FreshrSensor(FreshrEntity, SensorEntity):
    entity_description: FreshrSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: FreshrReadingsCoordinator, description: FreshrSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
