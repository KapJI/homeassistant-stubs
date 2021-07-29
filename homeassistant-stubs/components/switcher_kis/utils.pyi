from .const import DATA_BRIDGE as DATA_BRIDGE, DISCOVERY_TIME_SEC as DISCOVERY_TIME_SEC, DOMAIN as DOMAIN
from aioswitcher.bridge import SwitcherBase as SwitcherBase
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from typing import Any, Callable

_LOGGER: Any

async def async_start_bridge(hass: HomeAssistant, on_device_callback: Callable[[SwitcherBase], Any]) -> None: ...
async def async_stop_bridge(hass: HomeAssistant) -> None: ...
async def async_discover_devices() -> dict[str, SwitcherBase]: ...
