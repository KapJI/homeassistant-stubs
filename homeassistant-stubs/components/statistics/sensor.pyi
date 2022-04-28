from . import DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from collections.abc import Callable as Callable
from datetime import datetime, timedelta
from homeassistant.components.recorder import get_instance as get_instance, history as history
from homeassistant.components.sensor import PLATFORM_SCHEMA as PLATFORM_SCHEMA, SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorStateClass as SensorStateClass
from homeassistant.const import ATTR_DEVICE_CLASS as ATTR_DEVICE_CLASS, ATTR_UNIT_OF_MEASUREMENT as ATTR_UNIT_OF_MEASUREMENT, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_NAME as CONF_NAME, CONF_UNIQUE_ID as CONF_UNIQUE_ID, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, HomeAssistant as HomeAssistant, State as State, callback as callback, split_entity_id as split_entity_id
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_track_point_in_utc_time as async_track_point_in_utc_time, async_track_state_change_event as async_track_state_change_event
from homeassistant.helpers.reload import async_setup_reload_service as async_setup_reload_service
from homeassistant.helpers.start import async_at_start as async_at_start
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType, StateType as StateType
from typing import Any, Literal

_LOGGER: Any
STAT_AGE_COVERAGE_RATIO: str
STAT_BUFFER_USAGE_RATIO: str
STAT_SOURCE_VALUE_VALID: str
STAT_AVERAGE_LINEAR: str
STAT_AVERAGE_STEP: str
STAT_AVERAGE_TIMELESS: str
STAT_CHANGE: str
STAT_CHANGE_SAMPLE: str
STAT_CHANGE_SECOND: str
STAT_COUNT: str
STAT_DATETIME_NEWEST: str
STAT_DATETIME_OLDEST: str
STAT_DISTANCE_95P: str
STAT_DISTANCE_99P: str
STAT_DISTANCE_ABSOLUTE: str
STAT_MEAN: str
STAT_MEDIAN: str
STAT_NOISINESS: str
STAT_QUANTILES: str
STAT_STANDARD_DEVIATION: str
STAT_TOTAL: str
STAT_VALUE_MAX: str
STAT_VALUE_MIN: str
STAT_VARIANCE: str
DEPRECATION_WARNING_CHARACTERISTIC: str
STATS_NUMERIC_SUPPORT: Any
STATS_BINARY_SUPPORT: Any
STATS_NOT_A_NUMBER: Any
STATS_DATETIME: Any
STAT_NUMERIC_RETAIN_UNIT: Any
STAT_BINARY_PERCENTAGE: Any
CONF_STATE_CHARACTERISTIC: str
CONF_SAMPLES_MAX_BUFFER_SIZE: str
CONF_MAX_AGE: str
CONF_PRECISION: str
CONF_QUANTILE_INTERVALS: str
CONF_QUANTILE_METHOD: str
DEFAULT_NAME: str
DEFAULT_BUFFER_SIZE: int
DEFAULT_PRECISION: int
DEFAULT_QUANTILE_INTERVALS: int
DEFAULT_QUANTILE_METHOD: str
ICON: str

def valid_state_characteristic_configuration(config: dict[str, Any]) -> dict[str, Any]: ...

_PLATFORM_SCHEMA_BASE: Any

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...

class StatisticsSensor(SensorEntity):
    _attr_icon: Any
    _attr_name: Any
    _attr_should_poll: bool
    _attr_unique_id: Any
    _source_entity_id: Any
    is_binary: Any
    _state_characteristic: Any
    _samples_max_buffer_size: Any
    _samples_max_age: Any
    _precision: Any
    _quantile_intervals: Any
    _quantile_method: Any
    _value: Any
    _unit_of_measurement: Any
    _available: bool
    states: Any
    ages: Any
    attributes: Any
    _state_characteristic_fn: Any
    _update_listener: Any
    def __init__(self, source_entity_id: str, name: str, unique_id: Union[str, None], state_characteristic: str, samples_max_buffer_size: int, samples_max_age: Union[timedelta, None], precision: int, quantile_intervals: int, quantile_method: Literal['exclusive', 'inclusive']) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def _add_state_to_queue(self, new_state: State) -> None: ...
    def _derive_unit_of_measurement(self, new_state: State) -> Union[str, None]: ...
    @property
    def device_class(self) -> Union[SensorDeviceClass, None]: ...
    @property
    def state_class(self) -> Union[Literal[SensorStateClass.MEASUREMENT], None]: ...
    @property
    def native_value(self) -> Union[StateType, datetime]: ...
    @property
    def native_unit_of_measurement(self) -> Union[str, None]: ...
    @property
    def available(self) -> bool: ...
    @property
    def extra_state_attributes(self) -> Union[dict[str, StateType], None]: ...
    def _purge_old_states(self, max_age: timedelta) -> None: ...
    def _next_to_purge_timestamp(self) -> Union[datetime, None]: ...
    async def async_update(self) -> None: ...
    def _fetch_states_from_database(self) -> list[State]: ...
    async def _initialize_from_database(self) -> None: ...
    def _update_attributes(self) -> None: ...
    def _update_value(self) -> None: ...
    def _stat_average_linear(self) -> StateType: ...
    def _stat_average_step(self) -> StateType: ...
    def _stat_average_timeless(self) -> StateType: ...
    def _stat_change(self) -> StateType: ...
    def _stat_change_sample(self) -> StateType: ...
    def _stat_change_second(self) -> StateType: ...
    def _stat_count(self) -> StateType: ...
    def _stat_datetime_newest(self) -> Union[datetime, None]: ...
    def _stat_datetime_oldest(self) -> Union[datetime, None]: ...
    def _stat_distance_95_percent_of_values(self) -> StateType: ...
    def _stat_distance_99_percent_of_values(self) -> StateType: ...
    def _stat_distance_absolute(self) -> StateType: ...
    def _stat_mean(self) -> StateType: ...
    def _stat_median(self) -> StateType: ...
    def _stat_noisiness(self) -> StateType: ...
    def _stat_quantiles(self) -> StateType: ...
    def _stat_standard_deviation(self) -> StateType: ...
    def _stat_total(self) -> StateType: ...
    def _stat_value_max(self) -> StateType: ...
    def _stat_value_min(self) -> StateType: ...
    def _stat_variance(self) -> StateType: ...
    def _stat_binary_average_step(self) -> StateType: ...
    def _stat_binary_average_timeless(self) -> StateType: ...
    def _stat_binary_count(self) -> StateType: ...
    def _stat_binary_mean(self) -> StateType: ...
