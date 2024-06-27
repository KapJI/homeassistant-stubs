from . import AirGradientConfigEntry as AirGradientConfigEntry
from .const import LOGGER as LOGGER
from _typeshed import Incomplete
from airgradient import AirGradientClient as AirGradientClient, Config, Measures
from datetime import timedelta
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

class AirGradientCoordinator(DataUpdateCoordinator[_DataT]):
    _update_interval: timedelta
    config_entry: AirGradientConfigEntry
    client: Incomplete
    serial_number: Incomplete
    def __init__(self, hass: HomeAssistant, client: AirGradientClient) -> None: ...
    async def _async_update_data(self) -> _DataT: ...
    async def _update_data(self) -> _DataT: ...

class AirGradientMeasurementCoordinator(AirGradientCoordinator[Measures]):
    _update_interval: Incomplete
    async def _update_data(self) -> Measures: ...

class AirGradientConfigCoordinator(AirGradientCoordinator[Config]):
    _update_interval: Incomplete
    async def _update_data(self) -> Config: ...
