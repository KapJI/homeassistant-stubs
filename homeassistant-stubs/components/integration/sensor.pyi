from homeassistant.components.sensor import PLATFORM_SCHEMA as PLATFORM_SCHEMA, SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorStateClass as SensorStateClass
from homeassistant.const import ATTR_DEVICE_CLASS as ATTR_DEVICE_CLASS, ATTR_UNIT_OF_MEASUREMENT as ATTR_UNIT_OF_MEASUREMENT, CONF_METHOD as CONF_METHOD, CONF_NAME as CONF_NAME, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN, TIME_DAYS as TIME_DAYS, TIME_HOURS as TIME_HOURS, TIME_MINUTES as TIME_MINUTES, TIME_SECONDS as TIME_SECONDS
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_track_state_change_event as async_track_state_change_event
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
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

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...

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
    def __init__(self, source_entity: str, name: Union[str, None], round_digits: int, unit_prefix: Union[str, None], unit_time: str, unit_of_measurement: Union[str, None], integration_method: str) -> None: ...
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
