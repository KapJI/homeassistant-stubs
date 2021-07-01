from .const import DOMAIN as DOMAIN
from .model import CanaryData as CanaryData
from canary.api import Api as Api, Location as Location
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any

_LOGGER: Any

class CanaryDataUpdateCoordinator(DataUpdateCoordinator):
    canary: Any
    def __init__(self, hass: HomeAssistant, api: Api) -> None: ...
    def _update_data(self) -> CanaryData: ...
    async def _async_update_data(self) -> CanaryData: ...
