import greeneye
from .const import CONF_CHANNELS as CONF_CHANNELS, CONF_COUNTED_QUANTITY as CONF_COUNTED_QUANTITY, CONF_COUNTED_QUANTITY_PER_PULSE as CONF_COUNTED_QUANTITY_PER_PULSE, CONF_MONITORS as CONF_MONITORS, CONF_NET_METERING as CONF_NET_METERING, CONF_NUMBER as CONF_NUMBER, CONF_PULSE_COUNTERS as CONF_PULSE_COUNTERS, CONF_SERIAL_NUMBER as CONF_SERIAL_NUMBER, CONF_TEMPERATURE_SENSORS as CONF_TEMPERATURE_SENSORS, CONF_TIME_UNIT as CONF_TIME_UNIT, CONF_VOLTAGE_SENSORS as CONF_VOLTAGE_SENSORS, DATA_GREENEYE_MONITOR as DATA_GREENEYE_MONITOR
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_SENSORS as CONF_SENSORS, CONF_TEMPERATURE_UNIT as CONF_TEMPERATURE_UNIT, ELECTRIC_POTENTIAL_VOLT as ELECTRIC_POTENTIAL_VOLT, POWER_WATT as POWER_WATT, TIME_HOURS as TIME_HOURS, TIME_MINUTES as TIME_MINUTES, TIME_SECONDS as TIME_SECONDS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

DATA_PULSES: str
DATA_WATT_SECONDS: str
UNIT_WATTS = POWER_WATT
COUNTER_ICON: str

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...

UnderlyingSensorType: Any

class GEMSensor(SensorEntity):
    _attr_should_poll: bool
    _monitor: Any
    _monitor_serial_number: Any
    _attr_name: Any
    _sensor_type: Any
    _sensor: Any
    _number: Any
    _attr_unique_id: Any
    def __init__(self, monitor: greeneye.monitor.Monitor, name: str, sensor_type: str, sensor: UnderlyingSensorType, number: int) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...

class CurrentSensor(GEMSensor):
    _attr_native_unit_of_measurement: Any
    _attr_device_class: Any
    _sensor: Any
    _net_metering: Any
    def __init__(self, monitor: greeneye.monitor.Monitor, number: int, name: str, net_metering: bool) -> None: ...
    @property
    def native_value(self) -> Union[float, None]: ...
    @property
    def extra_state_attributes(self) -> Union[dict[str, Any], None]: ...

class PulseCounter(GEMSensor):
    _attr_icon: Any
    _sensor: Any
    _counted_quantity_per_pulse: Any
    _time_unit: Any
    _attr_native_unit_of_measurement: Any
    def __init__(self, monitor: greeneye.monitor.Monitor, number: int, name: str, counted_quantity: str, time_unit: str, counted_quantity_per_pulse: float) -> None: ...
    @property
    def native_value(self) -> Union[float, None]: ...
    @property
    def _seconds_per_time_unit(self) -> int: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...

class TemperatureSensor(GEMSensor):
    _attr_device_class: Any
    _sensor: Any
    _attr_native_unit_of_measurement: Any
    def __init__(self, monitor: greeneye.monitor.Monitor, number: int, name: str, unit: str) -> None: ...
    @property
    def native_value(self) -> Union[float, None]: ...

class VoltageSensor(GEMSensor):
    _attr_native_unit_of_measurement: Any
    _attr_device_class: Any
    _sensor: Any
    def __init__(self, monitor: greeneye.monitor.Monitor, number: int, name: str) -> None: ...
    @property
    def native_value(self) -> Union[float, None]: ...
