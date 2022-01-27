from datetime import datetime, timedelta
from homeassistant.components.sensor import PLATFORM_SCHEMA as PLATFORM_SCHEMA, SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import CONF_RESOURCES as CONF_RESOURCES, CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL, CONF_TYPE as CONF_TYPE, DATA_GIBIBYTES as DATA_GIBIBYTES, DATA_MEBIBYTES as DATA_MEBIBYTES, DATA_RATE_MEGABYTES_PER_SECOND as DATA_RATE_MEGABYTES_PER_SECOND, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, PERCENTAGE as PERCENTAGE, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect, async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.entity_component import DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.util import slugify as slugify
from typing import Any

_LOGGER: Any
CONF_ARG: str
CPU_ICON: str
SENSOR_TYPE_NAME: int
SENSOR_TYPE_UOM: int
SENSOR_TYPE_ICON: int
SENSOR_TYPE_DEVICE_CLASS: int
SENSOR_TYPE_MANDATORY_ARG: int
SIGNAL_SYSTEMMONITOR_UPDATE: str

class SysMonitorSensorEntityDescription(SensorEntityDescription):
    mandatory_arg: bool
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement, last_reset, native_unit_of_measurement, state_class, mandatory_arg) -> None: ...

SENSOR_TYPES: dict[str, SysMonitorSensorEntityDescription]

def check_required_arg(value: Any) -> Any: ...

IO_COUNTER: Any
IF_ADDRS_FAMILY: Any
CPU_SENSOR_PREFIXES: Any

class SensorData:
    argument: Any
    state: Union[str, datetime, None]
    value: Union[Any, None]
    update_time: Union[datetime, None]
    last_exception: Union[BaseException, None]
    def __init__(self, argument, state, value, update_time, last_exception) -> None: ...

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...
async def async_setup_sensor_registry_updates(hass: HomeAssistant, sensor_registry: dict[tuple[str, str], SensorData], scan_interval: timedelta) -> None: ...

class SystemMonitorSensor(SensorEntity):
    should_poll: bool
    entity_description: Any
    _attr_name: Any
    _attr_unique_id: Any
    _sensor_registry: Any
    _argument: Any
    def __init__(self, sensor_registry: dict[tuple[str, str], SensorData], sensor_description: SysMonitorSensorEntityDescription, argument: str = ...) -> None: ...
    @property
    def native_value(self) -> Union[str, datetime, None]: ...
    @property
    def available(self) -> bool: ...
    @property
    def data(self) -> SensorData: ...
    async def async_added_to_hass(self) -> None: ...

def _update(type_: str, data: SensorData) -> tuple[Union[str, datetime, None], Union[str, None], Union[datetime, None]]: ...
def _disk_usage(path: str) -> Any: ...
def _swap_memory() -> Any: ...
def _virtual_memory() -> Any: ...
def _net_io_counters() -> Any: ...
def _net_if_addrs() -> Any: ...
def _getloadavg() -> tuple[float, float, float]: ...
def _read_cpu_temperature() -> Union[float, None]: ...
