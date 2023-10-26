import abc
import asyncio
from .const import ATTR_WEATHER_APPARENT_TEMPERATURE as ATTR_WEATHER_APPARENT_TEMPERATURE, ATTR_WEATHER_CLOUD_COVERAGE as ATTR_WEATHER_CLOUD_COVERAGE, ATTR_WEATHER_DEW_POINT as ATTR_WEATHER_DEW_POINT, ATTR_WEATHER_HUMIDITY as ATTR_WEATHER_HUMIDITY, ATTR_WEATHER_OZONE as ATTR_WEATHER_OZONE, ATTR_WEATHER_PRECIPITATION_UNIT as ATTR_WEATHER_PRECIPITATION_UNIT, ATTR_WEATHER_PRESSURE as ATTR_WEATHER_PRESSURE, ATTR_WEATHER_PRESSURE_UNIT as ATTR_WEATHER_PRESSURE_UNIT, ATTR_WEATHER_TEMPERATURE as ATTR_WEATHER_TEMPERATURE, ATTR_WEATHER_TEMPERATURE_UNIT as ATTR_WEATHER_TEMPERATURE_UNIT, ATTR_WEATHER_UV_INDEX as ATTR_WEATHER_UV_INDEX, ATTR_WEATHER_VISIBILITY as ATTR_WEATHER_VISIBILITY, ATTR_WEATHER_VISIBILITY_UNIT as ATTR_WEATHER_VISIBILITY_UNIT, ATTR_WEATHER_WIND_BEARING as ATTR_WEATHER_WIND_BEARING, ATTR_WEATHER_WIND_GUST_SPEED as ATTR_WEATHER_WIND_GUST_SPEED, ATTR_WEATHER_WIND_SPEED as ATTR_WEATHER_WIND_SPEED, ATTR_WEATHER_WIND_SPEED_UNIT as ATTR_WEATHER_WIND_SPEED_UNIT, DOMAIN as DOMAIN, UNIT_CONVERSIONS as UNIT_CONVERSIONS, VALID_UNITS as VALID_UNITS, WeatherEntityFeature as WeatherEntityFeature
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Iterable
from datetime import timedelta
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import PRECISION_HALVES as PRECISION_HALVES, PRECISION_TENTHS as PRECISION_TENTHS, PRECISION_WHOLE as PRECISION_WHOLE, UnitOfPressure as UnitOfPressure, UnitOfSpeed as UnitOfSpeed, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.config_validation import PLATFORM_SCHEMA as PLATFORM_SCHEMA, PLATFORM_SCHEMA_BASE as PLATFORM_SCHEMA_BASE
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.entity_platform import EntityPlatform as EntityPlatform
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator, TimestampDataUpdateCoordinator as TimestampDataUpdateCoordinator
from homeassistant.loader import async_get_issue_tracker as async_get_issue_tracker, async_suggest_report_issue as async_suggest_report_issue
from homeassistant.util.dt import utcnow as utcnow
from homeassistant.util.json import JsonValueType as JsonValueType
from homeassistant.util.unit_system import US_CUSTOMARY_SYSTEM as US_CUSTOMARY_SYSTEM
from typing import Any, Final, Generic, Literal, Required, TypeVar, TypedDict

_LOGGER: Incomplete
ATTR_CONDITION_CLASS: str
ATTR_CONDITION_CLEAR_NIGHT: str
ATTR_CONDITION_CLOUDY: str
ATTR_CONDITION_EXCEPTIONAL: str
ATTR_CONDITION_FOG: str
ATTR_CONDITION_HAIL: str
ATTR_CONDITION_LIGHTNING: str
ATTR_CONDITION_LIGHTNING_RAINY: str
ATTR_CONDITION_PARTLYCLOUDY: str
ATTR_CONDITION_POURING: str
ATTR_CONDITION_RAINY: str
ATTR_CONDITION_SNOWY: str
ATTR_CONDITION_SNOWY_RAINY: str
ATTR_CONDITION_SUNNY: str
ATTR_CONDITION_WINDY: str
ATTR_CONDITION_WINDY_VARIANT: str
ATTR_FORECAST: str
ATTR_FORECAST_IS_DAYTIME: Final[str]
ATTR_FORECAST_CONDITION: Final[str]
ATTR_FORECAST_HUMIDITY: Final[str]
ATTR_FORECAST_NATIVE_PRECIPITATION: Final[str]
ATTR_FORECAST_PRECIPITATION: Final[str]
ATTR_FORECAST_PRECIPITATION_PROBABILITY: Final[str]
ATTR_FORECAST_NATIVE_PRESSURE: Final[str]
ATTR_FORECAST_PRESSURE: Final[str]
ATTR_FORECAST_NATIVE_APPARENT_TEMP: Final[str]
ATTR_FORECAST_APPARENT_TEMP: Final[str]
ATTR_FORECAST_NATIVE_TEMP: Final[str]
ATTR_FORECAST_TEMP: Final[str]
ATTR_FORECAST_NATIVE_TEMP_LOW: Final[str]
ATTR_FORECAST_TEMP_LOW: Final[str]
ATTR_FORECAST_TIME: Final[str]
ATTR_FORECAST_WIND_BEARING: Final[str]
ATTR_FORECAST_NATIVE_WIND_GUST_SPEED: Final[str]
ATTR_FORECAST_WIND_GUST_SPEED: Final[str]
ATTR_FORECAST_NATIVE_WIND_SPEED: Final[str]
ATTR_FORECAST_WIND_SPEED: Final[str]
ATTR_FORECAST_NATIVE_DEW_POINT: Final[str]
ATTR_FORECAST_DEW_POINT: Final[str]
ATTR_FORECAST_CLOUD_COVERAGE: Final[str]
ATTR_FORECAST_UV_INDEX: Final[str]
ENTITY_ID_FORMAT: Incomplete
SCAN_INTERVAL: Incomplete
ROUNDING_PRECISION: int
SERVICE_GET_FORECAST: Final[str]
_ObservationUpdateCoordinatorT = TypeVar('_ObservationUpdateCoordinatorT', bound='DataUpdateCoordinator[Any]')
_DailyForecastUpdateCoordinatorT = TypeVar('_DailyForecastUpdateCoordinatorT', bound='TimestampDataUpdateCoordinator[Any]')
_HourlyForecastUpdateCoordinatorT = TypeVar('_HourlyForecastUpdateCoordinatorT', bound='TimestampDataUpdateCoordinator[Any]')
_TwiceDailyForecastUpdateCoordinatorT = TypeVar('_TwiceDailyForecastUpdateCoordinatorT', bound='TimestampDataUpdateCoordinator[Any]')

def round_temperature(temperature: float | None, precision: float) -> float | None: ...

class Forecast(TypedDict, total=False):
    condition: str | None
    datetime: Required[str]
    humidity: float | None
    precipitation_probability: int | None
    cloud_coverage: int | None
    native_precipitation: float | None
    precipitation: None
    native_pressure: float | None
    pressure: None
    native_temperature: float | None
    temperature: None
    native_templow: float | None
    templow: None
    native_apparent_temperature: float | None
    wind_bearing: float | str | None
    native_wind_gust_speed: float | None
    native_wind_speed: float | None
    wind_speed: None
    native_dew_point: float | None
    uv_index: float | None
    is_daytime: bool | None

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class WeatherEntityDescription(EntityDescription):
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

class PostInitMeta(abc.ABCMeta):
    def __call__(cls, *args: Any, **kwargs: Any) -> Any: ...

class PostInit(metaclass=PostInitMeta):
    @abc.abstractmethod
    def __post_init__(self, *args: Any, **kwargs: Any) -> None: ...

class WeatherEntity(Entity, PostInit):
    _entity_component_unrecorded_attributes: Incomplete
    entity_description: WeatherEntityDescription
    _attr_condition: str | None
    _attr_forecast: list[Forecast] | None
    _attr_humidity: float | None
    _attr_ozone: float | None
    _attr_cloud_coverage: int | None
    _attr_uv_index: float | None
    _attr_precision: float
    _attr_state: None
    _attr_wind_bearing: float | str | None
    _attr_native_pressure: float | None
    _attr_native_pressure_unit: str | None
    _attr_native_apparent_temperature: float | None
    _attr_native_temperature: float | None
    _attr_native_temperature_unit: str | None
    _attr_native_visibility: float | None
    _attr_native_visibility_unit: str | None
    _attr_native_precipitation_unit: str | None
    _attr_native_wind_gust_speed: float | None
    _attr_native_wind_speed: float | None
    _attr_native_wind_speed_unit: str | None
    _attr_native_dew_point: float | None
    _forecast_listeners: dict[Literal['daily', 'hourly', 'twice_daily'], list[Callable[[list[JsonValueType] | None], None]]]
    __weather_reported_legacy_forecast: bool
    __weather_legacy_forecast: bool
    _weather_option_temperature_unit: str | None
    _weather_option_pressure_unit: str | None
    _weather_option_visibility_unit: str | None
    _weather_option_precipitation_unit: str | None
    _weather_option_wind_speed_unit: str | None
    def __post_init__(self, *args: Any, **kwargs: Any) -> None: ...
    def __init_subclass__(cls, **kwargs: Any) -> None: ...
    def add_to_platform_start(self, hass: HomeAssistant, platform: EntityPlatform, parallel_updates: asyncio.Semaphore | None) -> None: ...
    def _report_legacy_forecast(self, hass: HomeAssistant) -> None: ...
    async def async_internal_added_to_hass(self) -> None: ...
    @property
    def native_apparent_temperature(self) -> float | None: ...
    @property
    def native_temperature(self) -> float | None: ...
    @property
    def native_temperature_unit(self) -> str | None: ...
    @property
    def native_dew_point(self) -> float | None: ...
    @property
    def _default_temperature_unit(self) -> str: ...
    @property
    def _temperature_unit(self) -> str: ...
    @property
    def native_pressure(self) -> float | None: ...
    @property
    def native_pressure_unit(self) -> str | None: ...
    @property
    def _default_pressure_unit(self) -> str: ...
    @property
    def _pressure_unit(self) -> str: ...
    @property
    def humidity(self) -> float | None: ...
    @property
    def native_wind_gust_speed(self) -> float | None: ...
    @property
    def native_wind_speed(self) -> float | None: ...
    @property
    def native_wind_speed_unit(self) -> str | None: ...
    @property
    def _default_wind_speed_unit(self) -> str: ...
    @property
    def _wind_speed_unit(self) -> str: ...
    @property
    def wind_bearing(self) -> float | str | None: ...
    @property
    def ozone(self) -> float | None: ...
    @property
    def cloud_coverage(self) -> float | None: ...
    @property
    def uv_index(self) -> float | None: ...
    @property
    def native_visibility(self) -> float | None: ...
    @property
    def native_visibility_unit(self) -> str | None: ...
    @property
    def _default_visibility_unit(self) -> str: ...
    @property
    def _visibility_unit(self) -> str: ...
    @property
    def forecast(self) -> list[Forecast] | None: ...
    async def async_forecast_daily(self) -> list[Forecast] | None: ...
    async def async_forecast_twice_daily(self) -> list[Forecast] | None: ...
    async def async_forecast_hourly(self) -> list[Forecast] | None: ...
    @property
    def native_precipitation_unit(self) -> str | None: ...
    @property
    def _default_precipitation_unit(self) -> str: ...
    @property
    def _precipitation_unit(self) -> str: ...
    @property
    def precision(self) -> float: ...
    @property
    def state_attributes(self) -> dict[str, Any]: ...
    def _convert_forecast(self, native_forecast_list: list[Forecast]) -> list[JsonValueType]: ...
    @property
    def state(self) -> str | None: ...
    @property
    def condition(self) -> str | None: ...
    def async_registry_entry_updated(self) -> None: ...
    def _async_subscription_started(self, forecast_type: Literal['daily', 'hourly', 'twice_daily']) -> None: ...
    def _async_subscription_ended(self, forecast_type: Literal['daily', 'hourly', 'twice_daily']) -> None: ...
    def async_subscribe_forecast(self, forecast_type: Literal['daily', 'hourly', 'twice_daily'], forecast_listener: Callable[[list[JsonValueType] | None], None]) -> CALLBACK_TYPE: ...
    async def async_update_listeners(self, forecast_types: Iterable[Literal['daily', 'hourly', 'twice_daily']] | None) -> None: ...

def raise_unsupported_forecast(entity_id: str, forecast_type: str) -> None: ...
async def async_get_forecast_service(weather: WeatherEntity, service_call: ServiceCall) -> ServiceResponse: ...

class CoordinatorWeatherEntity(CoordinatorEntity[_ObservationUpdateCoordinatorT], WeatherEntity, Generic[_ObservationUpdateCoordinatorT, _DailyForecastUpdateCoordinatorT, _HourlyForecastUpdateCoordinatorT, _TwiceDailyForecastUpdateCoordinatorT]):
    forecast_coordinators: Incomplete
    forecast_valid: Incomplete
    unsub_forecast: Incomplete
    def __init__(self, observation_coordinator: _ObservationUpdateCoordinatorT, *, context: Any = ..., daily_coordinator: _DailyForecastUpdateCoordinatorT | None = ..., hourly_coordinator: _DailyForecastUpdateCoordinatorT | None = ..., twice_daily_coordinator: _DailyForecastUpdateCoordinatorT | None = ..., daily_forecast_valid: timedelta | None = ..., hourly_forecast_valid: timedelta | None = ..., twice_daily_forecast_valid: timedelta | None = ...) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def _remove_forecast_listener(self, forecast_type: Literal['daily', 'hourly', 'twice_daily']) -> None: ...
    def _async_subscription_started(self, forecast_type: Literal['daily', 'hourly', 'twice_daily']) -> None: ...
    def _handle_daily_forecast_coordinator_update(self) -> None: ...
    def _handle_hourly_forecast_coordinator_update(self) -> None: ...
    def _handle_twice_daily_forecast_coordinator_update(self) -> None: ...
    def _handle_forecast_update(self, forecast_type: Literal['daily', 'hourly', 'twice_daily']) -> None: ...
    def _async_subscription_ended(self, forecast_type: Literal['daily', 'hourly', 'twice_daily']) -> None: ...
    async def _async_refresh_forecast(self, coordinator: TimestampDataUpdateCoordinator[Any], forecast_valid_time: timedelta | None) -> bool: ...
    def _async_forecast_daily(self) -> list[Forecast] | None: ...
    def _async_forecast_hourly(self) -> list[Forecast] | None: ...
    def _async_forecast_twice_daily(self) -> list[Forecast] | None: ...
    async def _async_forecast(self, forecast_type: Literal['daily', 'hourly', 'twice_daily']) -> list[Forecast] | None: ...
    async def async_forecast_daily(self) -> list[Forecast] | None: ...
    async def async_forecast_hourly(self) -> list[Forecast] | None: ...
    async def async_forecast_twice_daily(self) -> list[Forecast] | None: ...

class SingleCoordinatorWeatherEntity(CoordinatorWeatherEntity[_ObservationUpdateCoordinatorT, TimestampDataUpdateCoordinator[None], TimestampDataUpdateCoordinator[None], TimestampDataUpdateCoordinator[None]]):
    def __init__(self, coordinator: _ObservationUpdateCoordinatorT, context: Any = ...) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
