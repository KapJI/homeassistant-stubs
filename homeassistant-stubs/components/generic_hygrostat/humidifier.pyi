from . import CONF_AWAY_FIXED as CONF_AWAY_FIXED, CONF_AWAY_HUMIDITY as CONF_AWAY_HUMIDITY, CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_DRY_TOLERANCE as CONF_DRY_TOLERANCE, CONF_HUMIDIFIER as CONF_HUMIDIFIER, CONF_INITIAL_STATE as CONF_INITIAL_STATE, CONF_KEEP_ALIVE as CONF_KEEP_ALIVE, CONF_MAX_HUMIDITY as CONF_MAX_HUMIDITY, CONF_MIN_DUR as CONF_MIN_DUR, CONF_MIN_HUMIDITY as CONF_MIN_HUMIDITY, CONF_SENSOR as CONF_SENSOR, CONF_STALE_DURATION as CONF_STALE_DURATION, CONF_TARGET_HUMIDITY as CONF_TARGET_HUMIDITY, CONF_WET_TOLERANCE as CONF_WET_TOLERANCE, HYGROSTAT_SCHEMA as HYGROSTAT_SCHEMA
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Mapping
from datetime import datetime, timedelta
from homeassistant.components.humidifier import ATTR_HUMIDITY as ATTR_HUMIDITY, HumidifierAction as HumidifierAction, HumidifierDeviceClass as HumidifierDeviceClass, HumidifierEntity as HumidifierEntity, HumidifierEntityFeature as HumidifierEntityFeature, MODE_AWAY as MODE_AWAY, MODE_NORMAL as MODE_NORMAL
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_MODE as ATTR_MODE, CONF_NAME as CONF_NAME, CONF_UNIQUE_ID as CONF_UNIQUE_ID, EVENT_HOMEASSISTANT_START as EVENT_HOMEASSISTANT_START, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import Event as Event, EventStateChangedData as EventStateChangedData, EventStateReportedData as EventStateReportedData, HomeAssistant as HomeAssistant, State as State, callback as callback
from homeassistant.helpers import condition as condition
from homeassistant.helpers.device import async_device_info_to_link_from_entity as async_device_info_to_link_from_entity
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback, AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_track_state_change_event as async_track_state_change_event, async_track_state_report_event as async_track_state_report_event, async_track_time_interval as async_track_time_interval
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

_LOGGER: Incomplete
ATTR_SAVED_HUMIDITY: str
PLATFORM_SCHEMA: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
def _time_period_or_none(value: Any) -> timedelta | None: ...
async def _async_setup_config(hass: HomeAssistant, config: Mapping[str, Any], unique_id: str | None, async_add_entities: AddEntitiesCallback | AddConfigEntryEntitiesCallback) -> None: ...

class GenericHygrostat(HumidifierEntity, RestoreEntity):
    _attr_should_poll: bool
    _name: Incomplete
    _switch_entity_id: Incomplete
    _sensor_entity_id: Incomplete
    _attr_device_info: Incomplete
    _device_class: Incomplete
    _min_cycle_duration: Incomplete
    _dry_tolerance: Incomplete
    _wet_tolerance: Incomplete
    _keep_alive: Incomplete
    _state: Incomplete
    _saved_target_humidity: Incomplete
    _active: bool
    _cur_humidity: float | None
    _humidity_lock: Incomplete
    _min_humidity: Incomplete
    _max_humidity: Incomplete
    _target_humidity: Incomplete
    _away_humidity: Incomplete
    _away_fixed: Incomplete
    _sensor_stale_duration: Incomplete
    _remove_stale_tracking: Callable[[], None] | None
    _is_away: bool
    _attr_action: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, hass: HomeAssistant, name: str, switch_entity_id: str, sensor_entity_id: str, min_humidity: float | None, max_humidity: float | None, target_humidity: float | None, device_class: HumidifierDeviceClass | None, min_cycle_duration: timedelta | None, dry_tolerance: float, wet_tolerance: float, keep_alive: timedelta | None, initial_state: bool | None, away_humidity: int | None, away_fixed: bool | None, sensor_stale_duration: timedelta | None, unique_id: str | None) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any] | None: ...
    @property
    def name(self) -> str: ...
    @property
    def is_on(self) -> bool | None: ...
    @property
    def current_humidity(self) -> float | None: ...
    @property
    def target_humidity(self) -> float | None: ...
    @property
    def mode(self) -> str | None: ...
    @property
    def available_modes(self) -> list[str] | None: ...
    @property
    def device_class(self) -> HumidifierDeviceClass: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_set_humidity(self, humidity: int) -> None: ...
    @property
    def min_humidity(self) -> float: ...
    @property
    def max_humidity(self) -> float: ...
    async def _async_sensor_event(self, event: Event[EventStateChangedData] | Event[EventStateReportedData]) -> None: ...
    async def _async_sensor_update(self, new_state: State) -> None: ...
    async def _async_sensor_not_responding(self, now: datetime | None = None) -> None: ...
    @callback
    def _async_switch_event(self, event: Event[EventStateChangedData]) -> None: ...
    @callback
    def _async_switch_changed(self, new_state: State | None) -> None: ...
    async def _async_update_humidity(self, humidity: str) -> None: ...
    async def _async_operate(self, time: datetime | None = None, force: bool = False) -> None: ...
    @property
    def _is_device_active(self) -> bool: ...
    async def _async_device_turn_on(self) -> None: ...
    async def _async_device_turn_off(self) -> None: ...
    async def async_set_mode(self, mode: str) -> None: ...
