from .const import CONF_ROUND_DIGITS as CONF_ROUND_DIGITS, CONF_SOURCE_SENSOR as CONF_SOURCE_SENSOR, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT, CONF_UNIT_PREFIX as CONF_UNIT_PREFIX, CONF_UNIT_TIME as CONF_UNIT_TIME, INTEGRATION_METHODS as INTEGRATION_METHODS, METHOD_LEFT as METHOD_LEFT, METHOD_RIGHT as METHOD_RIGHT, METHOD_TRAPEZOIDAL as METHOD_TRAPEZOIDAL
from homeassistant.components.sensor import PLATFORM_SCHEMA as PLATFORM_SCHEMA, SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_DEVICE_CLASS as ATTR_DEVICE_CLASS, ATTR_UNIT_OF_MEASUREMENT as ATTR_UNIT_OF_MEASUREMENT, CONF_METHOD as CONF_METHOD, CONF_NAME as CONF_NAME, CONF_UNIQUE_ID as CONF_UNIQUE_ID, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN, TIME_DAYS as TIME_DAYS, TIME_HOURS as TIME_HOURS, TIME_MINUTES as TIME_MINUTES, TIME_SECONDS as TIME_SECONDS
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_track_state_change_event as async_track_state_change_event
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

_LOGGER: Any
ATTR_SOURCE_ID: str
UNIT_PREFIXES: Any
UNIT_TIME: Any
ICON: str
DEFAULT_ROUND: int

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...

class IntegrationSensor(RestoreEntity, SensorEntity):
    _attr_unique_id: Any
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
    def __init__(self, *, integration_method: str, name: Union[str, None], round_digits: int, source_entity: str, unique_id: Union[str, None], unit_of_measurement: Union[str, None], unit_prefix: Union[str, None], unit_time: str) -> None: ...
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
