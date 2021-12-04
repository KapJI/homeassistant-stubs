import greeneye
from . import CONF_COUNTED_QUANTITY as CONF_COUNTED_QUANTITY, CONF_COUNTED_QUANTITY_PER_PULSE as CONF_COUNTED_QUANTITY_PER_PULSE, CONF_MONITOR_SERIAL_NUMBER as CONF_MONITOR_SERIAL_NUMBER, CONF_NET_METERING as CONF_NET_METERING, CONF_NUMBER as CONF_NUMBER, CONF_TIME_UNIT as CONF_TIME_UNIT, DATA_GREENEYE_MONITOR as DATA_GREENEYE_MONITOR, SENSOR_TYPE_CURRENT as SENSOR_TYPE_CURRENT, SENSOR_TYPE_PULSE_COUNTER as SENSOR_TYPE_PULSE_COUNTER, SENSOR_TYPE_TEMPERATURE as SENSOR_TYPE_TEMPERATURE, SENSOR_TYPE_VOLTAGE as SENSOR_TYPE_VOLTAGE
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_SENSORS as CONF_SENSORS, CONF_SENSOR_TYPE as CONF_SENSOR_TYPE, CONF_TEMPERATURE_UNIT as CONF_TEMPERATURE_UNIT, DEVICE_CLASS_POWER as DEVICE_CLASS_POWER, DEVICE_CLASS_TEMPERATURE as DEVICE_CLASS_TEMPERATURE, DEVICE_CLASS_VOLTAGE as DEVICE_CLASS_VOLTAGE, ELECTRIC_POTENTIAL_VOLT as ELECTRIC_POTENTIAL_VOLT, POWER_WATT as POWER_WATT, TIME_HOURS as TIME_HOURS, TIME_MINUTES as TIME_MINUTES, TIME_SECONDS as TIME_SECONDS
from homeassistant.core import Config as Config, HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import DiscoveryInfoType as DiscoveryInfoType
from typing import Any

DATA_PULSES: str
DATA_WATT_SECONDS: str
UNIT_WATTS = POWER_WATT
COUNTER_ICON: str

async def async_setup_platform(hass: HomeAssistant, config: Config, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType) -> None: ...

UnderlyingSensorType: Any

class GEMSensor(SensorEntity):
    _attr_should_poll: bool
    _monitor_serial_number: Any
    _attr_name: Any
    _monitor: Any
    _sensor_type: Any
    _number: Any
    _attr_unique_id: Any
    def __init__(self, monitor_serial_number: int, name: str, sensor_type: str, number: int) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def _on_new_monitor(self, monitor: greeneye.monitor.Monitor) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    def _try_connect_to_monitor(self, monitors: greeneye.Monitors) -> bool: ...
    @property
    def _sensor(self) -> Union[UnderlyingSensorType, None]: ...

class CurrentSensor(GEMSensor):
    _attr_native_unit_of_measurement: Any
    _attr_device_class: Any
    _net_metering: Any
    def __init__(self, monitor_serial_number: int, number: int, name: str, net_metering: bool) -> None: ...
    @property
    def _sensor(self) -> Union[greeneye.monitor.Channel, None]: ...
    @property
    def native_value(self) -> Union[float, None]: ...
    @property
    def extra_state_attributes(self) -> Union[dict[str, Any], None]: ...

class PulseCounter(GEMSensor):
    _attr_icon: Any
    _counted_quantity_per_pulse: Any
    _time_unit: Any
    _attr_native_unit_of_measurement: Any
    def __init__(self, monitor_serial_number: int, number: int, name: str, counted_quantity: str, time_unit: str, counted_quantity_per_pulse: float) -> None: ...
    @property
    def _sensor(self) -> Union[greeneye.monitor.PulseCounter, None]: ...
    @property
    def native_value(self) -> Union[float, None]: ...
    @property
    def _seconds_per_time_unit(self) -> int: ...
    @property
    def extra_state_attributes(self) -> Union[dict[str, Any], None]: ...

class TemperatureSensor(GEMSensor):
    _attr_device_class: Any
    _attr_native_unit_of_measurement: Any
    def __init__(self, monitor_serial_number: int, number: int, name: str, unit: str) -> None: ...
    @property
    def _sensor(self) -> Union[greeneye.monitor.TemperatureSensor, None]: ...
    @property
    def native_value(self) -> Union[float, None]: ...

class VoltageSensor(GEMSensor):
    _attr_native_unit_of_measurement: Any
    _attr_device_class: Any
    def __init__(self, monitor_serial_number: int, number: int, name: str) -> None: ...
    @property
    def _sensor(self) -> Union[greeneye.monitor.Monitor, None]: ...
    @property
    def native_value(self) -> Union[float, None]: ...
