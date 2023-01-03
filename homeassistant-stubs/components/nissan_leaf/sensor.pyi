from . import LeafDataStore as LeafDataStore, LeafEntity as LeafEntity
from .const import DATA_BATTERY as DATA_BATTERY, DATA_CHARGING as DATA_CHARGING, DATA_LEAF as DATA_LEAF, DATA_RANGE_AC as DATA_RANGE_AC, DATA_RANGE_AC_OFF as DATA_RANGE_AC_OFF
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity
from homeassistant.const import PERCENTAGE as PERCENTAGE, UnitOfLength as UnitOfLength
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.icon import icon_for_battery_level as icon_for_battery_level
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.util.unit_conversion import DistanceConverter as DistanceConverter
from homeassistant.util.unit_system import US_CUSTOMARY_SYSTEM as US_CUSTOMARY_SYSTEM
from voluptuous.validators import Number as Number

_LOGGER: Incomplete

def setup_platform(hass: HomeAssistant, config: ConfigType, add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...

class LeafBatterySensor(LeafEntity, SensorEntity):
    _attr_device_class: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, car: LeafDataStore) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def native_value(self) -> Union[Number, None]: ...
    @property
    def icon(self) -> str: ...

class LeafRangeSensor(LeafEntity, SensorEntity):
    _attr_icon: str
    _ac_on: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, car: LeafDataStore, ac_on: bool) -> None: ...
    @property
    def name(self) -> str: ...
    def log_registration(self) -> None: ...
    @property
    def native_value(self) -> Union[float, None]: ...
    @property
    def native_unit_of_measurement(self) -> str: ...
