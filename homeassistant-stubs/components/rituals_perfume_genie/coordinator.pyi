from .const import DOMAIN as DOMAIN, UPDATE_INTERVAL as UPDATE_INTERVAL
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from pyrituals import Diffuser as Diffuser

_LOGGER: Incomplete

class RitualsDataUpdateCoordinator(DataUpdateCoordinator[None]):
    diffuser: Incomplete
    def __init__(self, hass: HomeAssistant, diffuser: Diffuser) -> None: ...
    async def _async_update_data(self) -> None: ...
