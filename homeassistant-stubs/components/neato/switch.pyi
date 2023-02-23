from .const import NEATO_DOMAIN as NEATO_DOMAIN, NEATO_LOGIN as NEATO_LOGIN, NEATO_ROBOTS as NEATO_ROBOTS, SCAN_INTERVAL_MINUTES as SCAN_INTERVAL_MINUTES
from .hub import NeatoHub as NeatoHub
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pybotvac.robot import Robot as Robot
from typing import Any

_LOGGER: Incomplete
SCAN_INTERVAL: Incomplete
SWITCH_TYPE_SCHEDULE: str
SWITCH_TYPES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NeatoConnectedSwitch(SwitchEntity):
    type: Incomplete
    robot: Incomplete
    _available: bool
    _robot_name: Incomplete
    _state: Incomplete
    _schedule_state: Incomplete
    _clean_state: Incomplete
    _robot_serial: Incomplete
    def __init__(self, neato: NeatoHub, robot: Robot, switch_type: str) -> None: ...
    def update(self) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def available(self) -> bool: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def entity_category(self) -> EntityCategory: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    def turn_on(self, **kwargs: Any) -> None: ...
    def turn_off(self, **kwargs: Any) -> None: ...
