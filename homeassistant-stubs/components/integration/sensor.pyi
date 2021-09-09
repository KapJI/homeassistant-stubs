from homeassistant.components.sensor import DEVICE_CLASS_ENERGY as DEVICE_CLASS_ENERGY, DEVICE_CLASS_POWER as DEVICE_CLASS_POWER, PLATFORM_SCHEMA as PLATFORM_SCHEMA, STATE_CLASS_TOTAL_INCREASING as STATE_CLASS_TOTAL_INCREASING, SensorEntity as SensorEntity
from homeassistant.const import ATTR_DEVICE_CLASS as ATTR_DEVICE_CLASS, ATTR_UNIT_OF_MEASUREMENT as ATTR_UNIT_OF_MEASUREMENT, CONF_METHOD as CONF_METHOD, CONF_NAME as CONF_NAME, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN, TIME_DAYS as TIME_DAYS, TIME_HOURS as TIME_HOURS, TIME_MINUTES as TIME_MINUTES, TIME_SECONDS as TIME_SECONDS
from homeassistant.core import callback as callback
from homeassistant.helpers.event import async_track_state_change_event as async_track_state_change_event
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from typing import Any

_LOGGER: Any
ATTR_SOURCE_ID: str
CONF_SOURCE_SENSOR: str
CONF_ROUND_DIGITS: str
CONF_UNIT_PREFIX: str
CONF_UNIT_TIME: str
CONF_UNIT_OF_MEASUREMENT: str
TRAPEZOIDAL_METHOD: str
LEFT_METHOD: str
RIGHT_METHOD: str
INTEGRATION_METHOD: Any
UNIT_PREFIXES: Any
UNIT_TIME: Any
ICON: str
DEFAULT_ROUND: int

async def async_setup_platform(hass, config, async_add_entities, discovery_info: Any | None = ...) -> None: ...

class IntegrationSensor(RestoreEntity, SensorEntity):
    _sensor_source_id: Any
    _round_digits: Any
    _state: Any
    _method: Any
    _name: Any
    _unit_template: Any
    _unit_of_measurement: Any
    _unit_prefix: Any
    _unit_time: Any
    _attr_state_class: Any
    def __init__(self, source_entity, name, round_digits, unit_prefix, unit_time, unit_of_measurement, integration_method) -> None: ...
    _attr_device_class: Any
    async def async_added_to_hass(self) -> None: ...
    @property
    def name(self): ...
    @property
    def native_value(self): ...
    @property
    def native_unit_of_measurement(self): ...
    @property
    def should_poll(self): ...
    @property
    def extra_state_attributes(self): ...
    @property
    def icon(self): ...
