from . import MyUplinkDataCoordinator as MyUplinkDataCoordinator
from .const import DOMAIN as DOMAIN
from .entity import MyUplinkEntity as MyUplinkEntity
from .helpers import find_matching_platform as find_matching_platform
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfEnergy as UnitOfEnergy, UnitOfFrequency as UnitOfFrequency, UnitOfPower as UnitOfPower, UnitOfPressure as UnitOfPressure, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime, UnitOfVolumeFlowRate as UnitOfVolumeFlowRate
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from myuplink import DevicePoint as DevicePoint

DEVICE_POINT_UNIT_DESCRIPTIONS: dict[str, SensorEntityDescription]
MARKER_FOR_UNKNOWN_VALUE: int
CATEGORY_BASED_DESCRIPTIONS: dict[str, dict[str, SensorEntityDescription]]

def get_description(device_point: DevicePoint) -> SensorEntityDescription | None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MyUplinkDevicePointSensor(MyUplinkEntity, SensorEntity):
    point_id: Incomplete
    _attr_name: Incomplete
    entity_description: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    def __init__(self, coordinator: MyUplinkDataCoordinator, device_id: str, device_point: DevicePoint, entity_description: SensorEntityDescription | None, unique_id_suffix: str) -> None: ...
    @property
    def native_value(self) -> StateType: ...

class MyUplinkEnumSensor(MyUplinkDevicePointSensor):
    _attr_options: Incomplete
    options_map: Incomplete
    def __init__(self, coordinator: MyUplinkDataCoordinator, device_id: str, device_point: DevicePoint, entity_description: SensorEntityDescription | None, unique_id_suffix: str) -> None: ...
    @property
    def native_value(self) -> str: ...

class MyUplinkEnumRawSensor(MyUplinkDevicePointSensor):
    _attr_entity_registry_enabled_default: bool
    _attr_device_class: Incomplete
    _attr_name: Incomplete
    def __init__(self, coordinator: MyUplinkDataCoordinator, device_id: str, device_point: DevicePoint, entity_description: SensorEntityDescription | None, unique_id_suffix: str) -> None: ...
