from .common import FritzBoxBaseEntity as FritzBoxBaseEntity, FritzBoxTools as FritzBoxTools
from .const import DOMAIN as DOMAIN, UPTIME_DEVIATION as UPTIME_DEVIATION
from fritzconnection.lib.fritzstatus import FritzStatus as FritzStatus
from homeassistant.components.sensor import STATE_CLASS_MEASUREMENT as STATE_CLASS_MEASUREMENT, SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import DATA_GIGABYTES as DATA_GIGABYTES, DATA_RATE_KILOBITS_PER_SECOND as DATA_RATE_KILOBITS_PER_SECOND, DATA_RATE_KILOBYTES_PER_SECOND as DATA_RATE_KILOBYTES_PER_SECOND, DEVICE_CLASS_TIMESTAMP as DEVICE_CLASS_TIMESTAMP
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.dt import utcnow as utcnow
from typing import Any, Callable, TypedDict

_LOGGER: Any

def _uptime_calculation(seconds_uptime: float, last_value: Union[str, None]) -> str: ...
def _retrieve_device_uptime_state(status: FritzStatus, last_value: str) -> str: ...
def _retrieve_connection_uptime_state(status: FritzStatus, last_value: Union[str, None]) -> str: ...
def _retrieve_external_ip_state(status: FritzStatus, last_value: str) -> str: ...
def _retrieve_kb_s_sent_state(status: FritzStatus, last_value: str) -> float: ...
def _retrieve_kb_s_received_state(status: FritzStatus, last_value: str) -> float: ...
def _retrieve_max_kb_s_sent_state(status: FritzStatus, last_value: str) -> float: ...
def _retrieve_max_kb_s_received_state(status: FritzStatus, last_value: str) -> float: ...
def _retrieve_gb_sent_state(status: FritzStatus, last_value: str) -> float: ...
def _retrieve_gb_received_state(status: FritzStatus, last_value: str) -> float: ...

class SensorData(TypedDict):
    name: str
    device_class: Union[str, None]
    state_class: Union[str, None]
    last_reset: bool
    unit_of_measurement: Union[str, None]
    icon: Union[str, None]
    state_provider: Callable

SENSOR_DATA: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FritzBoxSensor(FritzBoxBaseEntity, SensorEntity):
    _sensor_data: Any
    _last_device_value: Any
    _last_wan_value: Any
    _attr_available: bool
    _attr_device_class: Any
    _attr_icon: Any
    _attr_name: Any
    _attr_state_class: Any
    _attr_unit_of_measurement: Any
    _attr_unique_id: Any
    def __init__(self, fritzbox_tools: FritzBoxTools, device_friendly_name: str, sensor_type: str) -> None: ...
    @property
    def _state_provider(self) -> Callable: ...
    _attr_state: Any
    _attr_last_reset: Any
    def update(self) -> None: ...
