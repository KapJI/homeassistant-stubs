from .const import DOMAIN as DOMAIN, REQUEST_TIMEOUT as REQUEST_TIMEOUT
from .model import LaundrifyDevice as LaundrifyDevice
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from laundrify_aio import LaundrifyAPI as LaundrifyAPI

_LOGGER: Incomplete

class LaundrifyUpdateCoordinator(DataUpdateCoordinator):
    laundrify_api: Incomplete
    def __init__(self, hass: HomeAssistant, laundrify_api: LaundrifyAPI, poll_interval: int) -> None: ...
    async def _async_update_data(self) -> dict[str, LaundrifyDevice]: ...
