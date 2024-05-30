from .const import LOGGER as LOGGER
from APsystemsEZ1 import APsystemsEZ1M as APsystemsEZ1M, ReturnOutputData
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

class ApSystemsDataCoordinator(DataUpdateCoordinator[ReturnOutputData]):
    api: Incomplete
    def __init__(self, hass: HomeAssistant, api: APsystemsEZ1M) -> None: ...
    async def _async_update_data(self) -> ReturnOutputData: ...
