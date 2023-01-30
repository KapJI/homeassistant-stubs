from _typeshed import Incomplete
from bs4 import BeautifulSoup
from datetime import timedelta
from homeassistant.components.rest import RestData as RestData
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete

class ScrapeCoordinator(DataUpdateCoordinator[BeautifulSoup]):
    _rest: Incomplete
    def __init__(self, hass: HomeAssistant, rest: RestData, update_interval: timedelta) -> None: ...
    async def _async_update_data(self) -> BeautifulSoup: ...
