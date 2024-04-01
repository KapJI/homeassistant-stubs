import abc
from .const import CONF_ROUND_DIGITS as CONF_ROUND_DIGITS, CONF_SOURCE_SENSOR as CONF_SOURCE_SENSOR, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT, CONF_UNIT_PREFIX as CONF_UNIT_PREFIX, CONF_UNIT_TIME as CONF_UNIT_TIME, INTEGRATION_METHODS as INTEGRATION_METHODS, METHOD_LEFT as METHOD_LEFT, METHOD_RIGHT as METHOD_RIGHT, METHOD_TRAPEZOIDAL as METHOD_TRAPEZOIDAL
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from dataclasses import dataclass
from decimal import Decimal
from homeassistant.components.sensor import PLATFORM_SCHEMA as PLATFORM_SCHEMA, RestoreSensor as RestoreSensor, SensorDeviceClass as SensorDeviceClass, SensorExtraStoredData as SensorExtraStoredData, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_DEVICE_CLASS as ATTR_DEVICE_CLASS, ATTR_UNIT_OF_MEASUREMENT as ATTR_UNIT_OF_MEASUREMENT, CONF_METHOD as CONF_METHOD, CONF_NAME as CONF_NAME, CONF_UNIQUE_ID as CONF_UNIQUE_ID, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN, UnitOfTime as UnitOfTime
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, State as State, callback as callback
from homeassistant.helpers import condition as condition
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import EventStateChangedData as EventStateChangedData, async_track_state_change_event as async_track_state_change_event
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any, Final, Self

_LOGGER: Incomplete
ATTR_SOURCE_ID: Final[str]
UNIT_PREFIXES: Incomplete
UNIT_TIME: Incomplete
DEFAULT_ROUND: int

class _IntegrationMethod(ABC, metaclass=abc.ABCMeta):
    @staticmethod
    def from_name(method_name: str) -> _IntegrationMethod: ...
    @abstractmethod
    def validate_states(self, left: State, right: State) -> bool: ...
    @abstractmethod
    def calculate_area_with_two_states(self, elapsed_time: float, left: State, right: State) -> Decimal: ...
    def calculate_area_with_one_state(self, elapsed_time: float, constant_state: State) -> Decimal: ...

class _Trapezoidal(_IntegrationMethod):
    def calculate_area_with_two_states(self, elapsed_time: float, left: State, right: State) -> Decimal: ...
    def validate_states(self, left: State, right: State) -> bool: ...

class _Left(_IntegrationMethod):
    def calculate_area_with_two_states(self, elapsed_time: float, left: State, right: State) -> Decimal: ...
    def validate_states(self, left: State, right: State) -> bool: ...

class _Right(_IntegrationMethod):
    def calculate_area_with_two_states(self, elapsed_time: float, left: State, right: State) -> Decimal: ...
    def validate_states(self, left: State, right: State) -> bool: ...

def _is_numeric_state(state: State) -> bool: ...

_NAME_TO_INTEGRATION_METHOD: dict[str, type[_IntegrationMethod]]

@dataclass
class IntegrationSensorExtraStoredData(SensorExtraStoredData):
    source_entity: str | None
    last_valid_state: Decimal | None
    def as_dict(self) -> dict[str, Any]: ...
    @classmethod
    def from_dict(cls, restored: dict[str, Any]) -> Self | None: ...
    def __init__(self, native_value, native_unit_of_measurement, source_entity, last_valid_state) -> None: ...

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class IntegrationSensor(RestoreSensor):
    _attr_state_class: Incomplete
    _attr_should_poll: bool
    _attr_unique_id: Incomplete
    _sensor_source_id: Incomplete
    _round_digits: Incomplete
    _state: Incomplete
    _method: Incomplete
    _attr_name: Incomplete
    _unit_prefix_string: Incomplete
    _unit_of_measurement: Incomplete
    _unit_prefix: Incomplete
    _unit_time: Incomplete
    _unit_time_str: Incomplete
    _attr_icon: str
    _source_entity: Incomplete
    _last_valid_state: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, *, integration_method: str, name: str | None, round_digits: int, source_entity: str, unique_id: str | None, unit_prefix: str | None, unit_time: UnitOfTime, device_info: DeviceInfo | None = None) -> None: ...
    def _calculate_unit(self, source_unit: str) -> str: ...
    _attr_device_class: Incomplete
    def _derive_and_set_attributes_from_state(self, source_state: State) -> None: ...
    def _update_integral(self, area: Decimal) -> None: ...
    _attr_native_value: Incomplete
    _attr_available: bool
    async def async_added_to_hass(self) -> None: ...
    def _handle_state_change(self, event: Event[EventStateChangedData]) -> None: ...
    @property
    def native_value(self) -> Decimal | None: ...
    @property
    def native_unit_of_measurement(self) -> str | None: ...
    @property
    def extra_state_attributes(self) -> dict[str, str] | None: ...
    @property
    def extra_restore_state_data(self) -> IntegrationSensorExtraStoredData: ...
    async def async_get_last_sensor_data(self) -> IntegrationSensorExtraStoredData | None: ...
