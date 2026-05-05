from .const import DOMAIN as DOMAIN
from .coordinator import UptimeRobotDataUpdateCoordinator as UptimeRobotDataUpdateCoordinator
from .entity import UptimeRobotEntity as UptimeRobotEntity
from collections.abc import Awaitable, Callable as Callable, Coroutine
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from pyuptimerobot import UptimeRobotMonitor as UptimeRobotMonitor
from typing import Any, Concatenate

def uptimerobot_api_call[_T: UptimeRobotEntity, **_P](func: Callable[Concatenate[_T, _P], Awaitable[None]]) -> Callable[Concatenate[_T, _P], Coroutine[Any, Any, None]]: ...
def new_device_listener(coordinator: UptimeRobotDataUpdateCoordinator, new_devices_callback: Callable[[list[UptimeRobotMonitor]], None]) -> Callable[[], None]: ...
