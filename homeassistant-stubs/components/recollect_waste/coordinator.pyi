from .const import CONF_PLACE_ID as CONF_PLACE_ID, CONF_SERVICE_ID as CONF_SERVICE_ID, LOGGER as LOGGER
from _typeshed import Incomplete
from aiorecollect.client import PickupEvent
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

DEFAULT_UPDATE_INTERVAL: Incomplete

class ReCollectWasteDataUpdateCoordinator(DataUpdateCoordinator[list[PickupEvent]]):
    config_entry: ConfigEntry
    _client: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry) -> None: ...
    async def _async_update_data(self) -> list[PickupEvent]: ...
