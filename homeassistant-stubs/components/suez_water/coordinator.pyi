from .const import CONF_COUNTER_ID as CONF_COUNTER_ID, DATA_REFRESH_INTERVAL as DATA_REFRESH_INTERVAL, DOMAIN as DOMAIN
from _typeshed import Incomplete
from dataclasses import dataclass
from datetime import date
from homeassistant.components.recorder import get_instance as get_instance
from homeassistant.components.recorder.models import StatisticData as StatisticData, StatisticMetaData as StatisticMetaData
from homeassistant.components.recorder.statistics import StatisticMeanType as StatisticMeanType, StatisticsRow as StatisticsRow, async_add_external_statistics as async_add_external_statistics, get_last_statistics as get_last_statistics
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, CURRENCY_EURO as CURRENCY_EURO, UnitOfVolume as UnitOfVolume
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryError as ConfigEntryError
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from homeassistant.util.unit_conversion import VolumeConverter as VolumeConverter
from pysuez import SuezClient, TelemetryMeasure as TelemetryMeasure

_LOGGER: Incomplete

@dataclass
class SuezWaterAggregatedAttributes:
    this_month_consumption: dict[str, float]
    previous_month_consumption: dict[str, float]
    last_year_overall: int
    this_year_overall: int
    history: dict[str, float]
    highest_monthly_consumption: float

@dataclass
class SuezWaterData:
    aggregated_value: float
    aggregated_attr: SuezWaterAggregatedAttributes
    price: float | None
type SuezWaterConfigEntry = ConfigEntry[SuezWaterCoordinator]

class SuezWaterCoordinator(DataUpdateCoordinator[SuezWaterData]):
    _suez_client: SuezClient
    config_entry: SuezWaterConfigEntry
    _counter_id: Incomplete
    _cost_statistic_id: Incomplete
    _water_statistic_id: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: SuezWaterConfigEntry) -> None: ...
    async def _async_setup(self) -> None: ...
    async def _async_update_data(self) -> SuezWaterData: ...
    async def _update_statistics(self, current_price: float | None) -> None: ...
    def _build_statistics(self, current_price: float | None, consumption_sum: float, cost_sum: float, last_stats: date | None, usage: list[TelemetryMeasure]) -> tuple[list[StatisticData], list[StatisticData]]: ...
    def _persist_statistics(self, consumption_statistics: list[StatisticData], cost_statistics: list[StatisticData]) -> None: ...
    def _get_statistics_metadata(self, id: str, name: str, unit: str, unit_class: str | None) -> StatisticMetaData: ...
    async def _get_last_stat(self, id: str) -> StatisticsRow | None: ...
