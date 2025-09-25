from .const import DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER, UPDATE_INTERVAL_DAILY_FORECAST as UPDATE_INTERVAL_DAILY_FORECAST, UPDATE_INTERVAL_HOURLY_FORECAST as UPDATE_INTERVAL_HOURLY_FORECAST, UPDATE_INTERVAL_OBSERVATION as UPDATE_INTERVAL_OBSERVATION
from _typeshed import Incomplete
from accuweather import AccuWeather as AccuWeather
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from datetime import timedelta
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, TimestampDataUpdateCoordinator as TimestampDataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any

EXCEPTIONS: Incomplete
_LOGGER: Incomplete

@dataclass
class AccuWeatherData:
    coordinator_observation: AccuWeatherObservationDataUpdateCoordinator
    coordinator_daily_forecast: AccuWeatherDailyForecastDataUpdateCoordinator
    coordinator_hourly_forecast: AccuWeatherHourlyForecastDataUpdateCoordinator
type AccuWeatherConfigEntry = ConfigEntry[AccuWeatherData]

class AccuWeatherObservationDataUpdateCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    config_entry: AccuWeatherConfigEntry
    accuweather: Incomplete
    location_key: Incomplete
    device_info: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: AccuWeatherConfigEntry, accuweather: AccuWeather) -> None: ...
    async def _async_update_data(self) -> dict[str, Any]: ...

class AccuWeatherForecastDataUpdateCoordinator(TimestampDataUpdateCoordinator[list[dict[str, Any]]]):
    config_entry: AccuWeatherConfigEntry
    accuweather: Incomplete
    location_key: Incomplete
    _fetch_method: Incomplete
    device_info: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: AccuWeatherConfigEntry, accuweather: AccuWeather, coordinator_type: str, update_interval: timedelta, fetch_method: Callable[..., Awaitable[list[dict[str, Any]]]]) -> None: ...
    async def _async_update_data(self) -> list[dict[str, Any]]: ...

class AccuWeatherDailyForecastDataUpdateCoordinator(AccuWeatherForecastDataUpdateCoordinator):
    def __init__(self, hass: HomeAssistant, config_entry: AccuWeatherConfigEntry, accuweather: AccuWeather) -> None: ...

class AccuWeatherHourlyForecastDataUpdateCoordinator(AccuWeatherForecastDataUpdateCoordinator):
    def __init__(self, hass: HomeAssistant, config_entry: AccuWeatherConfigEntry, accuweather: AccuWeather) -> None: ...

def _get_device_info(location_key: str, name: str) -> DeviceInfo: ...
