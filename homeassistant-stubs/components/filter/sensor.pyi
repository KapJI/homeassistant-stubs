from .const import CONF_FILTERS as CONF_FILTERS, CONF_FILTER_LOWER_BOUND as CONF_FILTER_LOWER_BOUND, CONF_FILTER_NAME as CONF_FILTER_NAME, CONF_FILTER_PRECISION as CONF_FILTER_PRECISION, CONF_FILTER_RADIUS as CONF_FILTER_RADIUS, CONF_FILTER_TIME_CONSTANT as CONF_FILTER_TIME_CONSTANT, CONF_FILTER_UPPER_BOUND as CONF_FILTER_UPPER_BOUND, CONF_FILTER_WINDOW_SIZE as CONF_FILTER_WINDOW_SIZE, CONF_TIME_SMA_TYPE as CONF_TIME_SMA_TYPE, DEFAULT_FILTER_RADIUS as DEFAULT_FILTER_RADIUS, DEFAULT_FILTER_TIME_CONSTANT as DEFAULT_FILTER_TIME_CONSTANT, DEFAULT_PRECISION as DEFAULT_PRECISION, DEFAULT_WINDOW_SIZE as DEFAULT_WINDOW_SIZE, DOMAIN as DOMAIN, FILTER_NAME_LOWPASS as FILTER_NAME_LOWPASS, FILTER_NAME_OUTLIER as FILTER_NAME_OUTLIER, FILTER_NAME_RANGE as FILTER_NAME_RANGE, FILTER_NAME_THROTTLE as FILTER_NAME_THROTTLE, FILTER_NAME_TIME_SMA as FILTER_NAME_TIME_SMA, FILTER_NAME_TIME_THROTTLE as FILTER_NAME_TIME_THROTTLE, PLATFORMS as PLATFORMS, TIME_SMA_LAST as TIME_SMA_LAST, WINDOW_SIZE_UNIT_NUMBER_EVENTS as WINDOW_SIZE_UNIT_NUMBER_EVENTS, WINDOW_SIZE_UNIT_TIME as WINDOW_SIZE_UNIT_TIME
from _typeshed import Incomplete
from collections import Counter, deque
from dataclasses import dataclass
from datetime import datetime, timedelta
from homeassistant.components.recorder import get_instance as get_instance, history as history
from homeassistant.components.sensor import ATTR_STATE_CLASS as ATTR_STATE_CLASS, SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_DEVICE_CLASS as ATTR_DEVICE_CLASS, ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_ICON as ATTR_ICON, ATTR_UNIT_OF_MEASUREMENT as ATTR_UNIT_OF_MEASUREMENT, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_NAME as CONF_NAME, CONF_UNIQUE_ID as CONF_UNIQUE_ID, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import Event as Event, EventStateChangedData as EventStateChangedData, HomeAssistant as HomeAssistant, State as State, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback, AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_track_state_change_event as async_track_state_change_event
from homeassistant.helpers.reload import async_setup_reload_service as async_setup_reload_service
from homeassistant.helpers.start import async_at_started as async_at_started
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType, StateType as StateType
from homeassistant.util.decorator import Registry as Registry

_LOGGER: Incomplete
FILTERS: Registry[str, type[Filter]]
ICON: str
FILTER_SCHEMA: Incomplete
FILTER_OUTLIER_SCHEMA: Incomplete
FILTER_LOWPASS_SCHEMA: Incomplete
FILTER_RANGE_SCHEMA: Incomplete
FILTER_TIME_SMA_SCHEMA: Incomplete
FILTER_THROTTLE_SCHEMA: Incomplete
FILTER_TIME_THROTTLE_SCHEMA: Incomplete
PLATFORM_SCHEMA: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SensorFilter(SensorEntity):
    _attr_should_poll: bool
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _entity: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _state: StateType
    _filters: Incomplete
    _attr_icon: Incomplete
    _attr_device_class: Incomplete
    _attr_state_class: Incomplete
    _attr_extra_state_attributes: Incomplete
    def __init__(self, name: str | None, unique_id: str | None, entity_id: str, filters: list[Filter]) -> None: ...
    @callback
    def _update_filter_sensor_state_event(self, event: Event[EventStateChangedData]) -> None: ...
    _attr_available: bool
    @callback
    def _update_filter_sensor_state(self, new_state: State | None, update_ha: bool = True) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def native_value(self) -> datetime | StateType: ...

class FilterState:
    state: str | float | int
    timestamp: Incomplete
    def __init__(self, state: _State) -> None: ...
    def set_precision(self, precision: int | None) -> None: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...

@dataclass
class _State:
    last_updated: datetime
    state: str | float | int

class Filter:
    states: deque[FilterState]
    window_unit: Incomplete
    filter_precision: Incomplete
    _name: Incomplete
    _entity: Incomplete
    _skip_processing: bool
    _window_size: Incomplete
    _store_raw: bool
    _only_numbers: bool
    def __init__(self, name: str, window_size: int | timedelta, entity: str, precision: int | None) -> None: ...
    @property
    def window_size(self) -> int | timedelta: ...
    @property
    def name(self) -> str: ...
    @property
    def skip_processing(self) -> bool: ...
    def reset(self) -> None: ...
    def _filter_state(self, new_state: FilterState) -> FilterState: ...
    def filter_state(self, new_state: _State) -> _State: ...

class RangeFilter(Filter, SensorEntity):
    _lower_bound: Incomplete
    _upper_bound: Incomplete
    _stats_internal: Counter
    def __init__(self, *, entity: str, precision: int | None = None, lower_bound: float | None = None, upper_bound: float | None = None) -> None: ...
    def _filter_state(self, new_state: FilterState) -> FilterState: ...

class OutlierFilter(Filter, SensorEntity):
    _radius: Incomplete
    _stats_internal: Counter
    _store_raw: bool
    def __init__(self, *, window_size: int, entity: str, radius: float, precision: int | None = None) -> None: ...
    def _filter_state(self, new_state: FilterState) -> FilterState: ...

class LowPassFilter(Filter, SensorEntity):
    _time_constant: Incomplete
    def __init__(self, *, window_size: int, entity: str, time_constant: int, precision: int = ...) -> None: ...
    def _filter_state(self, new_state: FilterState) -> FilterState: ...

class TimeSMAFilter(Filter, SensorEntity):
    _time_window: Incomplete
    last_leak: FilterState | None
    queue: Incomplete
    def __init__(self, *, window_size: timedelta, entity: str, type: str, precision: int = ...) -> None: ...
    def _leak(self, left_boundary: datetime) -> None: ...
    def _filter_state(self, new_state: FilterState) -> FilterState: ...

class ThrottleFilter(Filter, SensorEntity):
    _only_numbers: bool
    def __init__(self, *, window_size: int, entity: str, precision: None = None) -> None: ...
    _skip_processing: bool
    def _filter_state(self, new_state: FilterState) -> FilterState: ...

class TimeThrottleFilter(Filter, SensorEntity):
    _time_window: Incomplete
    _last_emitted_at: datetime | None
    _only_numbers: bool
    def __init__(self, *, window_size: timedelta, entity: str, precision: int | None = None) -> None: ...
    _skip_processing: bool
    def _filter_state(self, new_state: FilterState) -> FilterState: ...
