from .accessories import TYPES as TYPES
from .const import CHAR_ACTIVE as CHAR_ACTIVE, CHAR_AIR_QUALITY as CHAR_AIR_QUALITY, CHAR_CURRENT_AIR_PURIFIER_STATE as CHAR_CURRENT_AIR_PURIFIER_STATE, CHAR_CURRENT_HUMIDITY as CHAR_CURRENT_HUMIDITY, CHAR_CURRENT_TEMPERATURE as CHAR_CURRENT_TEMPERATURE, CHAR_FILTER_CHANGE_INDICATION as CHAR_FILTER_CHANGE_INDICATION, CHAR_FILTER_LIFE_LEVEL as CHAR_FILTER_LIFE_LEVEL, CHAR_NAME as CHAR_NAME, CHAR_PM25_DENSITY as CHAR_PM25_DENSITY, CHAR_TARGET_AIR_PURIFIER_STATE as CHAR_TARGET_AIR_PURIFIER_STATE, CONF_LINKED_FILTER_CHANGE_INDICATION as CONF_LINKED_FILTER_CHANGE_INDICATION, CONF_LINKED_FILTER_LIFE_LEVEL as CONF_LINKED_FILTER_LIFE_LEVEL, CONF_LINKED_HUMIDITY_SENSOR as CONF_LINKED_HUMIDITY_SENSOR, CONF_LINKED_PM25_SENSOR as CONF_LINKED_PM25_SENSOR, CONF_LINKED_TEMPERATURE_SENSOR as CONF_LINKED_TEMPERATURE_SENSOR, SERV_AIR_PURIFIER as SERV_AIR_PURIFIER, SERV_AIR_QUALITY_SENSOR as SERV_AIR_QUALITY_SENSOR, SERV_FILTER_MAINTENANCE as SERV_FILTER_MAINTENANCE, SERV_HUMIDITY_SENSOR as SERV_HUMIDITY_SENSOR, SERV_TEMPERATURE_SENSOR as SERV_TEMPERATURE_SENSOR, THRESHOLD_FILTER_CHANGE_NEEDED as THRESHOLD_FILTER_CHANGE_NEEDED
from .type_fans import ATTR_PRESET_MODE as ATTR_PRESET_MODE, CHAR_ROTATION_SPEED as CHAR_ROTATION_SPEED, Fan as Fan
from .util import cleanup_name_for_homekit as cleanup_name_for_homekit, convert_to_float as convert_to_float, density_to_air_quality as density_to_air_quality
from _typeshed import Incomplete
from homeassistant.const import STATE_ON as STATE_ON, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import Event as Event, EventStateChangedData as EventStateChangedData, HassJobType as HassJobType, State as State, callback as callback
from homeassistant.helpers.event import async_track_state_change_event as async_track_state_change_event
from pyhap.characteristic import Characteristic as Characteristic
from pyhap.service import Service as Service
from pyhap.util import callback as pyhap_callback
from typing import Any

_LOGGER: Incomplete
CURRENT_STATE_INACTIVE: int
CURRENT_STATE_IDLE: int
CURRENT_STATE_PURIFYING_AIR: int
TARGET_STATE_MANUAL: int
TARGET_STATE_AUTO: int
FILTER_CHANGE_FILTER: int
FILTER_OK: int
IGNORED_STATES: Incomplete

class AirPurifier(Fan):
    auto_preset: str | None
    def __init__(self, *args: Any) -> None: ...
    char_active: Characteristic
    preset_mode_chars: dict[str, Characteristic]
    char_current_humidity: Characteristic | None
    char_pm25_density: Characteristic | None
    char_current_temperature: Characteristic | None
    char_filter_change_indication: Characteristic | None
    char_filter_life_level: Characteristic | None
    char_target_air_purifier_state: Characteristic
    char_current_air_purifier_state: Characteristic
    linked_humidity_sensor: Incomplete
    linked_pm25_sensor: Incomplete
    char_air_quality: Incomplete
    linked_temperature_sensor: Incomplete
    linked_filter_change_indicator_binary_sensor: Incomplete
    linked_filter_life_level_sensor: Incomplete
    def create_services(self) -> Service: ...
    def should_add_preset_mode_switch(self, preset_mode: str) -> bool: ...
    @callback
    @pyhap_callback
    def run(self) -> None: ...
    @callback
    def _async_update_current_humidity_event(self, event: Event[EventStateChangedData]) -> None: ...
    @callback
    def _async_update_current_humidity(self, new_state: State | None) -> None: ...
    @callback
    def _async_update_current_pm25_event(self, event: Event[EventStateChangedData]) -> None: ...
    @callback
    def _async_update_current_pm25(self, new_state: State | None) -> None: ...
    @callback
    def _async_update_current_temperature_event(self, event: Event[EventStateChangedData]) -> None: ...
    @callback
    def _async_update_current_temperature(self, new_state: State | None) -> None: ...
    @callback
    def _async_update_filter_change_indicator_event(self, event: Event[EventStateChangedData]) -> None: ...
    @callback
    def _async_update_filter_change_indicator(self, new_state: State | None) -> None: ...
    @callback
    def _async_update_filter_life_level_event(self, event: Event[EventStateChangedData]) -> None: ...
    @callback
    def _async_update_filter_life_level(self, new_state: State | None) -> None: ...
    @callback
    def async_update_state(self, new_state: State) -> None: ...
    def set_chars(self, char_values: dict[str, Any]) -> None: ...
