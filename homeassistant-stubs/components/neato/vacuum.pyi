from .const import ACTION as ACTION, ALERTS as ALERTS, ERRORS as ERRORS, MODE as MODE, NEATO_LOGIN as NEATO_LOGIN, NEATO_MAP_DATA as NEATO_MAP_DATA, NEATO_PERSISTENT_MAPS as NEATO_PERSISTENT_MAPS, NEATO_ROBOTS as NEATO_ROBOTS, SCAN_INTERVAL_MINUTES as SCAN_INTERVAL_MINUTES
from .entity import NeatoEntity as NeatoEntity
from .hub import NeatoHub as NeatoHub
from _typeshed import Incomplete
from homeassistant.components.vacuum import ATTR_STATUS as ATTR_STATUS, STATE_CLEANING as STATE_CLEANING, STATE_DOCKED as STATE_DOCKED, STATE_ERROR as STATE_ERROR, STATE_RETURNING as STATE_RETURNING, StateVacuumEntity as StateVacuumEntity, VacuumEntityFeature as VacuumEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_MODE as ATTR_MODE, STATE_IDLE as STATE_IDLE, STATE_PAUSED as STATE_PAUSED
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pybotvac import Robot as Robot
from typing import Any

_LOGGER: Incomplete
SCAN_INTERVAL: Incomplete
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

class NeatoConnectedVacuum(NeatoEntity, StateVacuumEntity):
    _attr_supported_features: Incomplete
    _attr_name: Incomplete
    _attr_available: Incomplete
    _mapdata: Incomplete
    _robot_has_map: Incomplete
    _robot_maps: Incomplete
    _robot_serial: Incomplete
    _attr_unique_id: Incomplete
    _status_state: Incomplete
    _state: Incomplete
    _clean_time_start: Incomplete
    _clean_time_stop: Incomplete
    _clean_area: Incomplete
    _clean_battery_start: Incomplete
    _clean_battery_end: Incomplete
    _clean_susp_charge_count: Incomplete
    _clean_susp_time: Incomplete
    _clean_pause_time: Incomplete
    _clean_error_time: Incomplete
    _launched_from: Incomplete
    _robot_boundaries: Incomplete
    _robot_stats: Incomplete
    def __init__(self, neato: NeatoHub, robot: Robot, mapdata: dict[str, Any] | None, persistent_maps: dict[str, Any] | None) -> None: ...
    _attr_state: Incomplete
    _attr_battery_level: Incomplete
    def update(self) -> None: ...
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
    def neato_custom_cleaning(self, mode: str, navigation: str, category: str, zone: str | None = None) -> None: ...
