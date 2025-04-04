from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from airgradient import AirGradientClient as AirGradientClient, Config as Config, Measures as Measures
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

type AirGradientConfigEntry = ConfigEntry[AirGradientCoordinator]
@dataclass
class AirGradientData:
    measures: Measures
    config: Config

class AirGradientCoordinator(DataUpdateCoordinator[AirGradientData]):
    config_entry: AirGradientConfigEntry
    _current_version: str
    client: Incomplete
    serial_number: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: AirGradientConfigEntry, client: AirGradientClient) -> None: ...
    async def _async_setup(self) -> None: ...
    async def _async_update_data(self) -> AirGradientData: ...
