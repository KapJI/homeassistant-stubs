from .const import CONF_COUNTER_ID as CONF_COUNTER_ID, DATA_REFRESH_INTERVAL as DATA_REFRESH_INTERVAL, DOMAIN as DOMAIN
from collections.abc import Mapping
from dataclasses import dataclass
from datetime import date
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant, _LOGGER as _LOGGER
from homeassistant.exceptions import ConfigEntryError as ConfigEntryError
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pysuez import SuezClient
from typing import Any

@dataclass
class SuezWaterAggregatedAttributes:
    this_month_consumption: dict[date, float]
    previous_month_consumption: dict[date, float]
    last_year_overall: dict[str, float]
    this_year_overall: dict[str, float]
    history: dict[date, float]
    highest_monthly_consumption: float
    def __init__(self, this_month_consumption, previous_month_consumption, last_year_overall, this_year_overall, history, highest_monthly_consumption) -> None: ...

@dataclass
class SuezWaterData:
    aggregated_value: float
    aggregated_attr: Mapping[str, Any]
    price: float
    def __init__(self, aggregated_value, aggregated_attr, price) -> None: ...

class SuezWaterCoordinator(DataUpdateCoordinator[SuezWaterData]):
    _suez_client: SuezClient
    config_entry: ConfigEntry
    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry) -> None: ...
    async def _async_setup(self) -> None: ...
    async def _async_update_data(self) -> SuezWaterData: ...
