from .const import DOMAIN as DOMAIN, WMO_TO_HA_CONDITION_MAP as WMO_TO_HA_CONDITION_MAP
from _typeshed import Incomplete
from homeassistant.components.weather import Forecast as Forecast, WeatherEntity as WeatherEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import UnitOfPrecipitationDepth as UnitOfPrecipitationDepth, UnitOfSpeed as UnitOfSpeed, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from open_meteo import Forecast as OpenMeteoForecast

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class OpenMeteoWeatherEntity(CoordinatorEntity[DataUpdateCoordinator[OpenMeteoForecast]], WeatherEntity):
    _attr_has_entity_name: bool
    _attr_native_precipitation_unit: Incomplete
    _attr_native_temperature_unit: Incomplete
    _attr_native_wind_speed_unit: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, *, entry: ConfigEntry, coordinator: DataUpdateCoordinator[OpenMeteoForecast]) -> None: ...
    @property
    def condition(self) -> Union[str, None]: ...
    @property
    def native_temperature(self) -> Union[float, None]: ...
    @property
    def native_wind_speed(self) -> Union[float, None]: ...
    @property
    def wind_bearing(self) -> Union[float, str, None]: ...
    @property
    def forecast(self) -> Union[list[Forecast], None]: ...
