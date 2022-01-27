from .const import NEATO_DOMAIN as NEATO_DOMAIN, NEATO_LOGIN as NEATO_LOGIN, NEATO_ROBOTS as NEATO_ROBOTS, SCAN_INTERVAL_MINUTES as SCAN_INTERVAL_MINUTES
from .hub import NeatoHub as NeatoHub
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pybotvac.robot import Robot as Robot
from typing import Any

_LOGGER: Any
SCAN_INTERVAL: Any
BATTERY: str

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NeatoSensor(SensorEntity):
    robot: Any
    _available: bool
    _robot_name: Any
    _robot_serial: Any
    _state: Any
    def __init__(self, neato: NeatoHub, robot: Robot) -> None: ...
    def update(self) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def device_class(self) -> str: ...
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
