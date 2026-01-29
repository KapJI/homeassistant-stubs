import tibber
from .const import DOMAIN as DOMAIN, TibberConfigEntry as TibberConfigEntry
from _typeshed import Incomplete
from homeassistant.components.recorder import get_instance as get_instance
from homeassistant.components.recorder.models import StatisticData as StatisticData, StatisticMeanType as StatisticMeanType, StatisticMetaData as StatisticMetaData
from homeassistant.components.recorder.statistics import async_add_external_statistics as async_add_external_statistics, get_last_statistics as get_last_statistics, statistics_during_period as statistics_during_period
from homeassistant.const import UnitOfEnergy as UnitOfEnergy
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from homeassistant.util.unit_conversion import EnergyConverter as EnergyConverter
from tibber.data_api import TibberDevice

FIVE_YEARS: Incomplete
_LOGGER: Incomplete

class TibberDataCoordinator(DataUpdateCoordinator[None]):
    config_entry: TibberConfigEntry
    _tibber_connection: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: TibberConfigEntry, tibber_connection: tibber.Tibber) -> None: ...
    async def _async_update_data(self) -> None: ...
    async def _insert_statistics(self) -> None: ...

class TibberDataAPICoordinator(DataUpdateCoordinator[dict[str, TibberDevice]]):
    config_entry: TibberConfigEntry
    _runtime_data: Incomplete
    sensors_by_device: dict[str, dict[str, tibber.data_api.Sensor]]
    def __init__(self, hass: HomeAssistant, entry: TibberConfigEntry) -> None: ...
    def _build_sensor_lookup(self, devices: dict[str, TibberDevice]) -> None: ...
    def get_sensor(self, device_id: str, sensor_id: str) -> tibber.data_api.Sensor | None: ...
    async def _async_get_client(self) -> tibber.Tibber: ...
    async def _async_setup(self) -> None: ...
    async def _async_update_data(self) -> dict[str, TibberDevice]: ...
