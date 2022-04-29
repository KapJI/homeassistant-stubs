from .const import NEATO_DOMAIN as NEATO_DOMAIN, NEATO_LOGIN as NEATO_LOGIN, NEATO_MAP_DATA as NEATO_MAP_DATA, NEATO_ROBOTS as NEATO_ROBOTS, SCAN_INTERVAL_MINUTES as SCAN_INTERVAL_MINUTES
from .hub import NeatoHub as NeatoHub
from _typeshed import Incomplete
from homeassistant.components.camera import Camera as Camera
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pybotvac.robot import Robot as Robot
from typing import Any

_LOGGER: Incomplete
SCAN_INTERVAL: Incomplete
ATTR_GENERATED_AT: str

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NeatoCleaningMap(Camera):
    robot: Incomplete
    neato: Incomplete
    _mapdata: Incomplete
    _available: Incomplete
    _robot_name: Incomplete
    _robot_serial: Incomplete
    _generated_at: Incomplete
    _image_url: Incomplete
    _image: Incomplete
    def __init__(self, neato: NeatoHub, robot: Robot, mapdata: Union[dict[str, Any], None]) -> None: ...
    def camera_image(self, width: Union[int, None] = ..., height: Union[int, None] = ...) -> Union[bytes, None]: ...
    def update(self) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def available(self) -> bool: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
