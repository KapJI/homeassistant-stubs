from .const import CONF_ROUND_DIGITS as CONF_ROUND_DIGITS, CONF_SOURCE_SENSOR as CONF_SOURCE_SENSOR, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT, CONF_UNIT_PREFIX as CONF_UNIT_PREFIX, CONF_UNIT_TIME as CONF_UNIT_TIME, INTEGRATION_METHODS as INTEGRATION_METHODS, METHOD_LEFT as METHOD_LEFT, METHOD_RIGHT as METHOD_RIGHT, METHOD_TRAPEZOIDAL as METHOD_TRAPEZOIDAL
from _typeshed import Incomplete
from decimal import Decimal
from homeassistant.components.sensor import PLATFORM_SCHEMA as PLATFORM_SCHEMA, SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_DEVICE_CLASS as ATTR_DEVICE_CLASS, ATTR_UNIT_OF_MEASUREMENT as ATTR_UNIT_OF_MEASUREMENT, CONF_METHOD as CONF_METHOD, CONF_NAME as CONF_NAME, CONF_UNIQUE_ID as CONF_UNIQUE_ID, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN, UnitOfTime as UnitOfTime
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, State as State, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_track_state_change_event as async_track_state_change_event
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Final

_LOGGER: Incomplete
ATTR_SOURCE_ID: Final[str]
UNIT_PREFIXES: Incomplete
UNIT_TIME: Incomplete
DEFAULT_ROUND: int

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...

class IntegrationSensor(RestoreEntity, SensorEntity):
    _attr_state_class: Incomplete
    _attr_should_poll: bool
    _attr_unique_id: Incomplete
    _sensor_source_id: Incomplete
    _round_digits: Incomplete
    _state: Incomplete
    _method: Incomplete
    _attr_name: Incomplete
    _unit_template: Incomplete
    _unit_of_measurement: Incomplete
    _unit_prefix: Incomplete
    _unit_time: Incomplete
    _unit_time_str: Incomplete
    _attr_icon: str
    _attr_extra_state_attributes: Incomplete
    def __init__(self, *, integration_method: str, name: Union[str, None], round_digits: int, source_entity: str, unique_id: Union[str, None], unit_prefix: Union[str, None], unit_time: UnitOfTime) -> None: ...
    def _unit(self, source_unit: str) -> str: ...
    _attr_device_class: Incomplete
    async def async_added_to_hass(self) -> None: ...
    @property
    def native_value(self) -> Union[Decimal, None]: ...
    @property
    def native_unit_of_measurement(self) -> Union[str, None]: ...
