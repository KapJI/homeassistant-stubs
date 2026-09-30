from .const import CONF_ELECTRICITY_PRICE_INTERVAL as CONF_ELECTRICITY_PRICE_INTERVAL, DEFAULT_ELECTRICITY_PRICE_INTERVAL as DEFAULT_ELECTRICITY_PRICE_INTERVAL, DOMAIN as DOMAIN, ELECTRICITY_INTERVALS as ELECTRICITY_INTERVALS, LOGGER as LOGGER, SCAN_INTERVAL as SCAN_INTERVAL, THRESHOLD_HOUR as THRESHOLD_HOUR
from _typeshed import Incomplete
from datetime import date, timedelta
from energyzero import EnergyPrices as EnergyPrices, PriceType
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import NamedTuple, override
from zoneinfo import ZoneInfo

type EnergyZeroConfigEntry = ConfigEntry[EnergyZeroDataUpdateCoordinator]
class EnergyZeroData(NamedTuple):
    electricity_market_today: EnergyPrices
    electricity_market_tomorrow: EnergyPrices | None
    electricity_all_in_today: EnergyPrices
    electricity_all_in_tomorrow: EnergyPrices | None
    gas_today: EnergyPrices | None
    electricity_price_step: timedelta
    def next_price(self, prices: EnergyPrices, tomorrow: EnergyPrices | None) -> float | None: ...

class EnergyZeroDataUpdateCoordinator(DataUpdateCoordinator[EnergyZeroData]):
    config_entry: ConfigEntry
    electricity_interval: Incomplete
    electricity_price_step: Incomplete
    energyzero: Incomplete
    def __init__(self, hass: HomeAssistant, entry: EnergyZeroConfigEntry) -> None: ...
    async def _async_get_electricity_prices(self, day: date, local_tz: ZoneInfo) -> dict[PriceType, EnergyPrices]: ...
    @override
    async def _async_update_data(self) -> EnergyZeroData: ...
