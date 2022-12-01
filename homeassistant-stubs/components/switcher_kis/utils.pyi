from .const import DATA_BRIDGE as DATA_BRIDGE, DISCOVERY_TIME_SEC as DISCOVERY_TIME_SEC, DOMAIN as DOMAIN
from _typeshed import Incomplete
from aioswitcher.api.remotes import SwitcherBreezeRemoteManager
from aioswitcher.bridge import SwitcherBase as SwitcherBase
from collections.abc import Callable as Callable
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import singleton as singleton
from typing import Any

_LOGGER: Incomplete

async def async_start_bridge(hass: HomeAssistant, on_device_callback: Callable[[SwitcherBase], Any]) -> None: ...
async def async_stop_bridge(hass: HomeAssistant) -> None: ...
async def async_discover_devices() -> dict[str, SwitcherBase]: ...
def get_breeze_remote_manager(hass: HomeAssistant) -> SwitcherBreezeRemoteManager: ...
