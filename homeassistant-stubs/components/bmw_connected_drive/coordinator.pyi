from .const import CONF_READ_ONLY as CONF_READ_ONLY, CONF_REFRESH_TOKEN as CONF_REFRESH_TOKEN, DOMAIN as DOMAIN
from _typeshed import Incomplete
from bimmer_connected.account import MyBMWAccount
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_REGION as CONF_REGION, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

SCAN_INTERVAL: Incomplete
_LOGGER: Incomplete

class BMWDataUpdateCoordinator(DataUpdateCoordinator):
    account: MyBMWAccount
    read_only: Incomplete
    _entry: Incomplete
    def __init__(self, hass: HomeAssistant, *, entry: ConfigEntry) -> None: ...
    async def _async_update_data(self) -> None: ...
    def _update_config_entry_refresh_token(self, refresh_token: Union[str, None]) -> None: ...
    def notify_listeners(self) -> None: ...
