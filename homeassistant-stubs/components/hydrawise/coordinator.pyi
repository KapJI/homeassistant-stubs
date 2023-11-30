from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from datetime import timedelta
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from pydrawise import HydrawiseBase as HydrawiseBase
from pydrawise.schema import User

class HydrawiseDataUpdateCoordinator(DataUpdateCoordinator[User]):
    api: Incomplete
    def __init__(self, hass: HomeAssistant, api: HydrawiseBase, scan_interval: timedelta) -> None: ...
    async def _async_update_data(self) -> User: ...
