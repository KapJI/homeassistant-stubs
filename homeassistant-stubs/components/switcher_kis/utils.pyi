from .const import DISCOVERY_TIME_SEC as DISCOVERY_TIME_SEC
from _typeshed import Incomplete
from aioswitcher.api.remotes import SwitcherBreezeRemoteManager
from aioswitcher.bridge import SwitcherBase as SwitcherBase
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import singleton as singleton

_LOGGER: Incomplete

async def async_has_devices(hass: HomeAssistant) -> bool: ...
def get_breeze_remote_manager(hass: HomeAssistant) -> SwitcherBreezeRemoteManager: ...
