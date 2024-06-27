from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

_LOGGER: Incomplete

class AladdinConnectCoordinator(DataUpdateCoordinator[None]):
    acc: Incomplete
    doors: Incomplete
    def __init__(self, hass: HomeAssistant, acc: AladdinConnectClient) -> None: ...
    async def async_setup(self) -> None: ...
    async def _async_update_data(self) -> None: ...
