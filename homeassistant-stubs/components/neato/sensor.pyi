from .const import NEATO_DOMAIN as NEATO_DOMAIN, NEATO_LOGIN as NEATO_LOGIN, NEATO_ROBOTS as NEATO_ROBOTS, SCAN_INTERVAL_MINUTES as SCAN_INTERVAL_MINUTES
from .hub import NeatoHub as NeatoHub
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pybotvac.robot import Robot as Robot

_LOGGER: Incomplete
SCAN_INTERVAL: Incomplete
BATTERY: str

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NeatoSensor(SensorEntity):
    robot: Incomplete
    _available: bool
    _robot_name: Incomplete
    _robot_serial: Incomplete
    _state: Incomplete
    def __init__(self, neato: NeatoHub, robot: Robot) -> None: ...
    def update(self) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def device_class(self) -> SensorDeviceClass: ...
    @property
    def entity_category(self) -> EntityCategory: ...
    @property
    def available(self) -> bool: ...
    @property
    def native_value(self) -> Union[str, None]: ...
    @property
    def native_unit_of_measurement(self) -> str: ...
    @property
    def device_info(self) -> DeviceInfo: ...
