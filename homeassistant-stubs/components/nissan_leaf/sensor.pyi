from . import LeafEntity as LeafEntity
from .const import DATA_BATTERY as DATA_BATTERY, DATA_CHARGING as DATA_CHARGING, DATA_LEAF as DATA_LEAF, DATA_RANGE_AC as DATA_RANGE_AC, DATA_RANGE_AC_OFF as DATA_RANGE_AC_OFF
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity
from homeassistant.const import LENGTH_KILOMETERS as LENGTH_KILOMETERS, LENGTH_MILES as LENGTH_MILES, PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.icon import icon_for_battery_level as icon_for_battery_level
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.util.unit_system import IMPERIAL_SYSTEM as IMPERIAL_SYSTEM, METRIC_SYSTEM as METRIC_SYSTEM
from pycarwings2.pycarwings2 import Leaf as Leaf
from typing import Any
from voluptuous.validators import Number as Number

_LOGGER: Any
ICON_RANGE: str

def setup_platform(hass: HomeAssistant, config: ConfigType, add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...

class LeafBatterySensor(LeafEntity, SensorEntity):
    _attr_unique_id: Any
    def __init__(self, car: Leaf) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def device_class(self) -> str: ...
    @property
    def native_value(self) -> Union[Number, None]: ...
    @property
    def native_unit_of_measurement(self) -> str: ...
    @property
    def icon(self) -> str: ...

class LeafRangeSensor(LeafEntity, SensorEntity):
    _ac_on: Any
    _attr_unique_id: Any
    def __init__(self, car: Leaf, ac_on: bool) -> None: ...
    @property
    def name(self) -> str: ...
    def log_registration(self) -> None: ...
    @property
    def native_value(self) -> Union[float, None]: ...
    @property
    def native_unit_of_measurement(self) -> str: ...
    @property
    def icon(self) -> str: ...
