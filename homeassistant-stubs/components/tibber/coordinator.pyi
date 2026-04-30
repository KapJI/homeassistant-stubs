import tibber
from .const import DOMAIN as DOMAIN, TibberConfigEntry as TibberConfigEntry
from _typeshed import Incomplete
from datetime import datetime, timedelta
from homeassistant.components.recorder import get_instance as get_instance
from homeassistant.components.recorder.models import StatisticData as StatisticData, StatisticMeanType as StatisticMeanType, StatisticMetaData as StatisticMetaData
from homeassistant.components.recorder.statistics import async_add_external_statistics as async_add_external_statistics, get_last_statistics as get_last_statistics, statistics_during_period as statistics_during_period
from homeassistant.const import UnitOfEnergy as UnitOfEnergy
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from homeassistant.util.unit_conversion import EnergyConverter as EnergyConverter
from tibber.data_api import TibberDevice
from typing import TypedDict

FIVE_YEARS: Incomplete
_LOGGER: Incomplete

class TibberHomeData(TypedDict):
    currency: str
    price_unit: str
    current_price: float | None
    current_price_time: datetime | None
    intraday_price_ranking: float | None
    max_price: float
    avg_price: float
    min_price: float
    off_peak_1: float
    peak: float
    off_peak_2: float
    month_cost: float | None
    peak_hour: float | None
    peak_hour_time: datetime | None
    month_cons: float | None
    app_nickname: str | None
    grid_company: str | None
    estimated_annual_consumption: int | None

def _build_home_data(home: tibber.TibberHome) -> TibberHomeData: ...

class TibberCoordinator[_DataT](DataUpdateCoordinator[_DataT]):
    config_entry: TibberConfigEntry
    _runtime_data: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: TibberConfigEntry, *, name: str, update_interval: timedelta | None = None) -> None: ...
    async def _async_get_client(self) -> tibber.Tibber: ...

class TibberDataCoordinator(TibberCoordinator[None]):
    def __init__(self, hass: HomeAssistant, config_entry: TibberConfigEntry, tibber_connection: tibber.Tibber) -> None: ...
    async def _async_update_data(self) -> None: ...
    async def _insert_statistics(self) -> None: ...

class TibberPriceCoordinator(TibberCoordinator[dict[str, TibberHomeData]]):
    _price_fetch_coordinator: Incomplete
    _unsub_price_fetch_listener: CALLBACK_TYPE | None
    def __init__(self, hass: HomeAssistant, config_entry: TibberConfigEntry, price_fetch_coordinator: TibberFetchPriceCoordinator) -> None: ...
    @callback
    def _build_price_data(self) -> dict[str, TibberHomeData]: ...
    update_interval: Incomplete
    @callback
    def _async_handle_price_fetch_update(self) -> None: ...
    @callback
    def _schedule_refresh(self) -> None: ...
    def _unschedule_refresh(self) -> None: ...
    def _time_until_next_15_minute(self) -> timedelta: ...
    async def _async_update_data(self) -> dict[str, TibberHomeData]: ...

class TibberFetchPriceCoordinator(TibberCoordinator[dict[str, tibber.TibberHome]]):
    _tomorrow_price_poll_threshold_seconds: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: TibberConfigEntry) -> None: ...
    update_interval: Incomplete
    async def _async_update_data(self) -> dict[str, tibber.TibberHome]: ...

class TibberDataAPICoordinator(TibberCoordinator[dict[str, TibberDevice]]):
    sensors_by_device: dict[str, dict[str, tibber.data_api.Sensor]]
    def __init__(self, hass: HomeAssistant, entry: TibberConfigEntry) -> None: ...
    def _build_sensor_lookup(self, devices: dict[str, TibberDevice]) -> None: ...
    def get_sensor(self, device_id: str, sensor_id: str) -> tibber.data_api.Sensor | None: ...
    async def _async_setup(self) -> None: ...
    async def _async_update_data(self) -> dict[str, TibberDevice]: ...
