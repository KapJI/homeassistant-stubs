from .const import DOMAIN as DOMAIN, WMO_TO_HA_CONDITION_MAP as WMO_TO_HA_CONDITION_MAP
from homeassistant.components.weather import Forecast as Forecast, WeatherEntity as WeatherEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from open_meteo import Forecast as OpenMeteoForecast
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class OpenMeteoWeatherEntity(CoordinatorEntity, WeatherEntity):
    _attr_temperature_unit: Any
    coordinator: DataUpdateCoordinator[OpenMeteoForecast]
    _attr_unique_id: Any
    _attr_name: Any
    _attr_device_info: Any
    def __init__(self, entry: ConfigEntry, coordinator: DataUpdateCoordinator) -> None: ...
    @property
    def condition(self) -> Union[str, None]: ...
    @property
    def temperature(self) -> Union[float, None]: ...
    @property
    def wind_speed(self) -> Union[float, None]: ...
    @property
    def wind_bearing(self) -> Union[float, str, None]: ...
    @property
    def forecast(self) -> Union[list[Forecast], None]: ...
