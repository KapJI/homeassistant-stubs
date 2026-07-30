from .const import LOGGER as LOGGER, PLACEHOLDER_API_KEY as PLACEHOLDER_API_KEY
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_URL as CONF_URL
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.httpx_client import get_async_client as get_async_client
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import override

UPDATE_INTERVAL_CONNECTED: Incomplete
UPDATE_INTERVAL_DISCONNECTED: Incomplete
type LiteLLMConfigEntry = ConfigEntry[LiteLLMDataUpdateCoordinator]

class LiteLLMDataUpdateCoordinator(DataUpdateCoordinator[None]):
    config_entry: LiteLLMConfigEntry
    client: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: LiteLLMConfigEntry) -> None: ...
    update_interval: Incomplete
    @override
    async def _async_update_data(self) -> None: ...
    @callback
    @override
    def async_set_updated_data(self, data: None) -> None: ...
    last_update_success: bool
    @callback
    def mark_connection_error(self) -> None: ...
