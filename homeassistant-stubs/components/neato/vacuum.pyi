from .const import ACTION as ACTION, ALERTS as ALERTS, ERRORS as ERRORS, MODE as MODE, NEATO_DOMAIN as NEATO_DOMAIN, NEATO_LOGIN as NEATO_LOGIN, NEATO_MAP_DATA as NEATO_MAP_DATA, NEATO_PERSISTENT_MAPS as NEATO_PERSISTENT_MAPS, NEATO_ROBOTS as NEATO_ROBOTS, SCAN_INTERVAL_MINUTES as SCAN_INTERVAL_MINUTES
from .hub import NeatoHub as NeatoHub
from homeassistant.components.vacuum import ATTR_STATUS as ATTR_STATUS, STATE_CLEANING as STATE_CLEANING, STATE_DOCKED as STATE_DOCKED, STATE_ERROR as STATE_ERROR, STATE_RETURNING as STATE_RETURNING, SUPPORT_BATTERY as SUPPORT_BATTERY, SUPPORT_CLEAN_SPOT as SUPPORT_CLEAN_SPOT, SUPPORT_LOCATE as SUPPORT_LOCATE, SUPPORT_MAP as SUPPORT_MAP, SUPPORT_PAUSE as SUPPORT_PAUSE, SUPPORT_RETURN_HOME as SUPPORT_RETURN_HOME, SUPPORT_START as SUPPORT_START, SUPPORT_STATE as SUPPORT_STATE, SUPPORT_STOP as SUPPORT_STOP, StateVacuumEntity as StateVacuumEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_MODE as ATTR_MODE, STATE_IDLE as STATE_IDLE, STATE_PAUSED as STATE_PAUSED
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pybotvac import Robot as Robot
from typing import Any

_LOGGER: Any
SCAN_INTERVAL: Any
SUPPORT_NEATO: Any
ATTR_CLEAN_START: str
ATTR_CLEAN_STOP: str
ATTR_CLEAN_AREA: str
ATTR_CLEAN_BATTERY_START: str
ATTR_CLEAN_BATTERY_END: str
ATTR_CLEAN_SUSP_COUNT: str
ATTR_CLEAN_SUSP_TIME: str
ATTR_CLEAN_PAUSE_TIME: str
ATTR_CLEAN_ERROR_TIME: str
ATTR_LAUNCHED_FROM: str
ATTR_NAVIGATION: str
ATTR_CATEGORY: str
ATTR_ZONE: str

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NeatoConnectedVacuum(StateVacuumEntity):
    robot: Any
    _available: Any
    _mapdata: Any
    _name: Any
    _robot_has_map: Any
    _robot_maps: Any
    _robot_serial: Any
    _status_state: Any
    _clean_state: Any
    _state: Any
    _clean_time_start: Any
    _clean_time_stop: Any
    _clean_area: Any
    _clean_battery_start: Any
    _clean_battery_end: Any
    _clean_susp_charge_count: Any
    _clean_susp_time: Any
    _clean_pause_time: Any
    _clean_error_time: Any
    _launched_from: Any
    _battery_level: Any
    _robot_boundaries: Any
    _robot_stats: Any
    def __init__(self, neato: NeatoHub, robot: Robot, mapdata: Union[dict[str, Any], None], persistent_maps: Union[dict[str, Any], None]) -> None: ...
    def update(self) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def supported_features(self) -> int: ...
    @property
    def battery_level(self) -> Union[int, None]: ...
    @property
    def available(self) -> bool: ...
    @property
    def icon(self) -> str: ...
    @property
    def state(self) -> Union[str, None]: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    def start(self) -> None: ...
    def pause(self) -> None: ...
    def return_to_base(self, **kwargs: Any) -> None: ...
    def stop(self, **kwargs: Any) -> None: ...
    def locate(self, **kwargs: Any) -> None: ...
    def clean_spot(self, **kwargs: Any) -> None: ...
    def neato_custom_cleaning(self, mode: str, navigation: str, category: str, zone: Union[str, None] = ...) -> None: ...
