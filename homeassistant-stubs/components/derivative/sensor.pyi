from .const import CONF_MAX_SUB_INTERVAL as CONF_MAX_SUB_INTERVAL, CONF_ROUND_DIGITS as CONF_ROUND_DIGITS, CONF_TIME_WINDOW as CONF_TIME_WINDOW, CONF_UNIT as CONF_UNIT, CONF_UNIT_PREFIX as CONF_UNIT_PREFIX, CONF_UNIT_TIME as CONF_UNIT_TIME
from _typeshed import Incomplete
from datetime import datetime, timedelta
from decimal import Decimal
from homeassistant.components.sensor import ATTR_STATE_CLASS as ATTR_STATE_CLASS, RestoreSensor as RestoreSensor, SensorEntity as SensorEntity, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_UNIT_OF_MEASUREMENT as ATTR_UNIT_OF_MEASUREMENT, CONF_NAME as CONF_NAME, CONF_SOURCE as CONF_SOURCE, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN, UnitOfTime as UnitOfTime
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, EventStateChangedData as EventStateChangedData, EventStateReportedData as EventStateReportedData, HomeAssistant as HomeAssistant, State as State, callback as callback
from homeassistant.helpers.device import async_entity_id_to_device as async_entity_id_to_device
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback, AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_call_later as async_call_later, async_track_state_change_event as async_track_state_change_event, async_track_state_report_event as async_track_state_report_event
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType

_LOGGER: Incomplete
ATTR_SOURCE_ID: str
UNIT_PREFIXES: Incomplete
UNIT_TIME: Incomplete
DEFAULT_ROUND: int
DEFAULT_TIME_WINDOW: int
PLATFORM_SCHEMA: Incomplete

def _is_decimal_state(state: str) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class DerivativeSensor(RestoreSensor, SensorEntity):
    _attr_translation_key: str
    _attr_should_poll: bool
    _attr_unique_id: Incomplete
    device_entry: Incomplete
    _sensor_source_id: Incomplete
    _round_digits: Incomplete
    _attr_native_value: Incomplete
    _state_list: list[tuple[datetime, datetime, Decimal]]
    _last_valid_state_time: tuple[str, datetime] | None
    _attr_name: Incomplete
    _attr_extra_state_attributes: Incomplete
    _unit_template: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _unit_prefix: Incomplete
    _unit_time: Incomplete
    _time_window: Incomplete
    _max_sub_interval: timedelta | None
    _cancel_max_sub_interval_exceeded_callback: CALLBACK_TYPE
    def __init__(self, hass: HomeAssistant, *, name: str | None, round_digits: int, source_entity: str, time_window: timedelta, unit_of_measurement: str | None, unit_prefix: str | None, unit_time: UnitOfTime, max_sub_interval: timedelta | None, unique_id: str | None) -> None: ...
    def _calc_derivative_from_state_list(self, current_time: datetime) -> Decimal: ...
    def _prune_state_list(self, current_time: datetime) -> None: ...
    _attr_available: bool
    def _handle_invalid_source_state(self, state: State | None) -> bool: ...
    def _write_native_value(self, derivative: Decimal | None) -> None: ...
    async def async_added_to_hass(self) -> None: ...
