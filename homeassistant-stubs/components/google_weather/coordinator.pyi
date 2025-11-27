from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from datetime import timedelta
from google_weather_api import CurrentConditionsResponse, DailyForecastResponse, GoogleWeatherApi as GoogleWeatherApi, HourlyForecastResponse
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigSubentry as ConfigSubentry
from homeassistant.const import CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import TimestampDataUpdateCoordinator as TimestampDataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import TypeVar

_LOGGER: Incomplete
T = TypeVar('T', bound=CurrentConditionsResponse | DailyForecastResponse | HourlyForecastResponse | None)

@dataclass
class GoogleWeatherSubEntryRuntimeData:
    coordinator_observation: GoogleWeatherCurrentConditionsCoordinator
    coordinator_daily_forecast: GoogleWeatherDailyForecastCoordinator
    coordinator_hourly_forecast: GoogleWeatherHourlyForecastCoordinator

@dataclass
class GoogleWeatherRuntimeData:
    api: GoogleWeatherApi
    subentries_runtime_data: dict[str, GoogleWeatherSubEntryRuntimeData]
type GoogleWeatherConfigEntry = ConfigEntry[GoogleWeatherRuntimeData]

class GoogleWeatherBaseCoordinator(TimestampDataUpdateCoordinator[T]):
    config_entry: GoogleWeatherConfigEntry
    subentry: Incomplete
    _data_type_name: Incomplete
    _api_method: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: GoogleWeatherConfigEntry, subentry: ConfigSubentry, data_type_name: str, update_interval: timedelta, api_method: Callable[..., Awaitable[T]]) -> None: ...
    async def _async_update_data(self) -> T: ...

class GoogleWeatherCurrentConditionsCoordinator(GoogleWeatherBaseCoordinator[CurrentConditionsResponse]):
    def __init__(self, hass: HomeAssistant, config_entry: GoogleWeatherConfigEntry, subentry: ConfigSubentry, api: GoogleWeatherApi) -> None: ...

class GoogleWeatherDailyForecastCoordinator(GoogleWeatherBaseCoordinator[DailyForecastResponse]):
    def __init__(self, hass: HomeAssistant, config_entry: GoogleWeatherConfigEntry, subentry: ConfigSubentry, api: GoogleWeatherApi) -> None: ...

class GoogleWeatherHourlyForecastCoordinator(GoogleWeatherBaseCoordinator[HourlyForecastResponse]):
    def __init__(self, hass: HomeAssistant, config_entry: GoogleWeatherConfigEntry, subentry: ConfigSubentry, api: GoogleWeatherApi) -> None: ...
