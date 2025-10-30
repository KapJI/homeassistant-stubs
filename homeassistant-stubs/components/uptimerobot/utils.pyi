from .coordinator import UptimeRobotDataUpdateCoordinator as UptimeRobotDataUpdateCoordinator
from collections.abc import Callable as Callable
from pyuptimerobot import UptimeRobotMonitor as UptimeRobotMonitor

def new_device_listener(coordinator: UptimeRobotDataUpdateCoordinator, new_devices_callback: Callable[[list[UptimeRobotMonitor]], None]) -> Callable[[], None]: ...
