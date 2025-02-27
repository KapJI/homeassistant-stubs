from .const import ATTR_SMHI_THUNDER_PROBABILITY as ATTR_SMHI_THUNDER_PROBABILITY, ENTITY_ID_SENSOR_FORMAT as ENTITY_ID_SENSOR_FORMAT
from .coordinator import SMHIConfigEntry as SMHIConfigEntry
from .entity import SmhiWeatherBaseEntity as SmhiWeatherBaseEntity
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.components.weather import ATTR_CONDITION_CLEAR_NIGHT as ATTR_CONDITION_CLEAR_NIGHT, ATTR_CONDITION_CLOUDY as ATTR_CONDITION_CLOUDY, ATTR_CONDITION_EXCEPTIONAL as ATTR_CONDITION_EXCEPTIONAL, ATTR_CONDITION_FOG as ATTR_CONDITION_FOG, ATTR_CONDITION_HAIL as ATTR_CONDITION_HAIL, ATTR_CONDITION_LIGHTNING as ATTR_CONDITION_LIGHTNING, ATTR_CONDITION_LIGHTNING_RAINY as ATTR_CONDITION_LIGHTNING_RAINY, ATTR_CONDITION_PARTLYCLOUDY as ATTR_CONDITION_PARTLYCLOUDY, ATTR_CONDITION_POURING as ATTR_CONDITION_POURING, ATTR_CONDITION_RAINY as ATTR_CONDITION_RAINY, ATTR_CONDITION_SNOWY as ATTR_CONDITION_SNOWY, ATTR_CONDITION_SNOWY_RAINY as ATTR_CONDITION_SNOWY_RAINY, ATTR_CONDITION_SUNNY as ATTR_CONDITION_SUNNY, ATTR_CONDITION_WINDY as ATTR_CONDITION_WINDY, ATTR_CONDITION_WINDY_VARIANT as ATTR_CONDITION_WINDY_VARIANT, ATTR_FORECAST_CLOUD_COVERAGE as ATTR_FORECAST_CLOUD_COVERAGE, ATTR_FORECAST_CONDITION as ATTR_FORECAST_CONDITION, ATTR_FORECAST_HUMIDITY as ATTR_FORECAST_HUMIDITY, ATTR_FORECAST_NATIVE_PRECIPITATION as ATTR_FORECAST_NATIVE_PRECIPITATION, ATTR_FORECAST_NATIVE_PRESSURE as ATTR_FORECAST_NATIVE_PRESSURE, ATTR_FORECAST_NATIVE_TEMP as ATTR_FORECAST_NATIVE_TEMP, ATTR_FORECAST_NATIVE_TEMP_LOW as ATTR_FORECAST_NATIVE_TEMP_LOW, ATTR_FORECAST_NATIVE_WIND_GUST_SPEED as ATTR_FORECAST_NATIVE_WIND_GUST_SPEED, ATTR_FORECAST_NATIVE_WIND_SPEED as ATTR_FORECAST_NATIVE_WIND_SPEED, ATTR_FORECAST_TIME as ATTR_FORECAST_TIME, ATTR_FORECAST_WIND_BEARING as ATTR_FORECAST_WIND_BEARING, Forecast as Forecast, SingleCoordinatorWeatherEntity as SingleCoordinatorWeatherEntity, WeatherEntityFeature as WeatherEntityFeature
from homeassistant.const import CONF_LATITUDE as CONF_LATITUDE, CONF_LOCATION as CONF_LOCATION, CONF_LONGITUDE as CONF_LONGITUDE, UnitOfLength as UnitOfLength, UnitOfPrecipitationDepth as UnitOfPrecipitationDepth, UnitOfPressure as UnitOfPressure, UnitOfSpeed as UnitOfSpeed, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import sun as sun
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pysmhi import SMHIForecast as SMHIForecast
from typing import Any, Final

CONDITION_CLASSES: Final[dict[str, list[int]]]
CONDITION_MAP: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: SMHIConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SmhiWeather(SmhiWeatherBaseEntity, SingleCoordinatorWeatherEntity):
    _attr_native_temperature_unit: Incomplete
    _attr_native_visibility_unit: Incomplete
    _attr_native_precipitation_unit: Incomplete
    _attr_native_wind_speed_unit: Incomplete
    _attr_native_pressure_unit: Incomplete
    _attr_supported_features: Incomplete
    _attr_native_temperature: Incomplete
    _attr_humidity: Incomplete
    _attr_native_wind_speed: Incomplete
    _attr_wind_bearing: Incomplete
    _attr_native_visibility: Incomplete
    _attr_native_pressure: Incomplete
    _attr_native_wind_gust_speed: Incomplete
    _attr_cloud_coverage: Incomplete
    _attr_condition: Incomplete
    def update_entity_data(self) -> None: ...
    @property
    def extra_state_attributes(self) -> Mapping[str, Any] | None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    def _get_forecast_data(self, forecast_data: list[SMHIForecast] | None) -> list[Forecast] | None: ...
    def _async_forecast_daily(self) -> list[Forecast] | None: ...
    def _async_forecast_hourly(self) -> list[Forecast] | None: ...
