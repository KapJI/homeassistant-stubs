from _typeshed import Incomplete
from aioaseko import Unit as Unit, Variable
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

_LOGGER: Incomplete

class AsekoDataUpdateCoordinator(DataUpdateCoordinator[dict[str, Variable]]):
    _unit: Incomplete
    def __init__(self, hass: HomeAssistant, unit: Unit) -> None: ...
    async def _async_update_data(self) -> dict[str, Variable]: ...
