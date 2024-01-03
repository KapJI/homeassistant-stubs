from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from dataclasses import dataclass
from datetime import timedelta
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from pydrawise import HydrawiseBase as HydrawiseBase
from pydrawise.schema import Controller as Controller, User as User, Zone as Zone

@dataclass
class HydrawiseData:
    user: User
    controllers: dict[int, Controller]
    zones: dict[int, Zone]
    def __init__(self, user, controllers, zones) -> None: ...

class HydrawiseDataUpdateCoordinator(DataUpdateCoordinator[HydrawiseData]):
    api: HydrawiseBase
    def __init__(self, hass: HomeAssistant, api: HydrawiseBase, scan_interval: timedelta) -> None: ...
    async def _async_update_data(self) -> HydrawiseData: ...
