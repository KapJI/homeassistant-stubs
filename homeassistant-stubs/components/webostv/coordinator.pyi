from .const import DOMAIN as DOMAIN, LOGGER as LOGGER, WEBOSTV_EXCEPTIONS as WEBOSTV_EXCEPTIONS
from _typeshed import Incomplete
from aiowebostv import WebOsClient as WebOsClient, WebOsTvState as WebOsTvState
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigEntryState as ConfigEntryState
from homeassistant.const import CONF_CLIENT_SECRET as CONF_CLIENT_SECRET, CONF_HOST as CONF_HOST
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.trigger import PluggableAction as PluggableAction
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import override

SCAN_INTERVAL: Incomplete
type WebOsTvConfigEntry = ConfigEntry[WebOsTvDataUpdateCoordinator]

class WebOsTvDataUpdateCoordinator(DataUpdateCoordinator[None]):
    config_entry: WebOsTvConfigEntry
    client: Incomplete
    turn_on: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: WebOsTvConfigEntry, client: WebOsClient) -> None: ...
    @override
    async def _async_update_data(self) -> None: ...
    async def async_handle_update(self, tv_state: WebOsTvState) -> None: ...

def update_client_key(hass: HomeAssistant, entry: WebOsTvConfigEntry, client: WebOsClient) -> None: ...
