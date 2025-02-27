from .const import DEFAULT_POLL_INTERVAL as DEFAULT_POLL_INTERVAL, DOMAIN as DOMAIN, REQUEST_TIMEOUT as REQUEST_TIMEOUT
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from laundrify_aio import LaundrifyAPI as LaundrifyAPI, LaundrifyDevice

_LOGGER: Incomplete

class LaundrifyUpdateCoordinator(DataUpdateCoordinator[dict[str, LaundrifyDevice]]):
    config_entry: ConfigEntry
    laundrify_api: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry, laundrify_api: LaundrifyAPI) -> None: ...
    async def _async_update_data(self) -> dict[str, LaundrifyDevice]: ...
