from .const import DEFAULT_PORT as DEFAULT_PORT, DEFAULT_UPDATE_INTERVAL as DEFAULT_UPDATE_INTERVAL, DEFAULT_USERNAME as DEFAULT_USERNAME, DOMAIN as DOMAIN, LOGGER as LOGGER, P1_UPDATE_INTERVAL as P1_UPDATE_INTERVAL
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryError as ConfigEntryError
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.debounce import Debouncer as Debouncer
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from plugwise import GwEntityData

type PlugwiseConfigEntry = ConfigEntry[PlugwiseDataUpdateCoordinator]
class PlugwiseDataUpdateCoordinator(DataUpdateCoordinator[dict[str, GwEntityData]]):
    _connected: bool
    _current_devices: set[str]
    _stored_devices: set[str]
    new_devices: set[str]
    config_entry: PlugwiseConfigEntry
    api: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: PlugwiseConfigEntry) -> None: ...
    update_interval: Incomplete
    async def _connect(self) -> None: ...
    async def _async_setup(self) -> None: ...
    async def _async_update_data(self) -> dict[str, GwEntityData]: ...
    def _async_add_remove_devices(self, data: dict[str, GwEntityData]) -> None: ...
    def _async_remove_devices(self, data: dict[str, GwEntityData]) -> None: ...
