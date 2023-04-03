from _typeshed import Incomplete
from homeassistant.components.weather import ATTR_CONDITION_CLOUDY as ATTR_CONDITION_CLOUDY, ATTR_CONDITION_EXCEPTIONAL as ATTR_CONDITION_EXCEPTIONAL, ATTR_CONDITION_FOG as ATTR_CONDITION_FOG, ATTR_CONDITION_HAIL as ATTR_CONDITION_HAIL, ATTR_CONDITION_LIGHTNING as ATTR_CONDITION_LIGHTNING, ATTR_CONDITION_LIGHTNING_RAINY as ATTR_CONDITION_LIGHTNING_RAINY, ATTR_CONDITION_PARTLYCLOUDY as ATTR_CONDITION_PARTLYCLOUDY, ATTR_CONDITION_POURING as ATTR_CONDITION_POURING, ATTR_CONDITION_RAINY as ATTR_CONDITION_RAINY, ATTR_CONDITION_SNOWY as ATTR_CONDITION_SNOWY, ATTR_CONDITION_SNOWY_RAINY as ATTR_CONDITION_SNOWY_RAINY, ATTR_CONDITION_SUNNY as ATTR_CONDITION_SUNNY, ATTR_CONDITION_WINDY as ATTR_CONDITION_WINDY, ATTR_CONDITION_WINDY_VARIANT as ATTR_CONDITION_WINDY_VARIANT, Forecast as Forecast, WeatherEntity as WeatherEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import UnitOfPressure as UnitOfPressure, UnitOfSpeed as UnitOfSpeed, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType

CONDITION_CLASSES: dict[str, list[str]]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def setup_platform(hass: HomeAssistant, config: ConfigType, add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = ...) -> None: ...

class DemoWeather(WeatherEntity):
    _attr_attribution: str
    _attr_should_poll: bool
    _attr_name: Incomplete
    _condition: Incomplete
    _native_temperature: Incomplete
    _native_temperature_unit: Incomplete
    _humidity: Incomplete
    _native_pressure: Incomplete
    _native_pressure_unit: Incomplete
    _native_wind_speed: Incomplete
    _native_wind_speed_unit: Incomplete
    _forecast: Incomplete
    def __init__(self, name: str, condition: str, temperature: float, humidity: float, pressure: float, wind_speed: float, temperature_unit: str, pressure_unit: str, wind_speed_unit: str, forecast: list[list]) -> None: ...
    @property
    def native_temperature(self) -> float: ...
    @property
    def native_temperature_unit(self) -> str: ...
    @property
    def humidity(self) -> float: ...
    @property
    def native_wind_speed(self) -> float: ...
    @property
    def native_wind_speed_unit(self) -> str: ...
    @property
    def native_pressure(self) -> float: ...
    @property
    def native_pressure_unit(self) -> str: ...
    @property
    def condition(self) -> str: ...
    @property
    def forecast(self) -> list[Forecast]: ...
