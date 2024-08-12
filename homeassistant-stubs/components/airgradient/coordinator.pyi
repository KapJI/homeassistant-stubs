from . import AirGradientConfigEntry as AirGradientConfigEntry
from .const import LOGGER as LOGGER
from _typeshed import Incomplete
from airgradient import AirGradientClient as AirGradientClient, Config, Measures
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

class AirGradientCoordinator(DataUpdateCoordinator[_DataT]):
    config_entry: AirGradientConfigEntry
    client: Incomplete
    serial_number: Incomplete
    def __init__(self, hass: HomeAssistant, client: AirGradientClient) -> None: ...
    async def _async_update_data(self) -> _DataT: ...
    async def _update_data(self) -> _DataT: ...

class AirGradientMeasurementCoordinator(AirGradientCoordinator[Measures]):
    async def _update_data(self) -> Measures: ...

class AirGradientConfigCoordinator(AirGradientCoordinator[Config]):
    async def _update_data(self) -> Config: ...
