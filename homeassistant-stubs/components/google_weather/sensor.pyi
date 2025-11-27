from .coordinator import GoogleWeatherConfigEntry as GoogleWeatherConfigEntry, GoogleWeatherCurrentConditionsCoordinator as GoogleWeatherCurrentConditionsCoordinator
from .entity import GoogleWeatherBaseEntity as GoogleWeatherBaseEntity
from collections.abc import Callable as Callable
from dataclasses import dataclass
from google_weather_api import CurrentConditionsResponse as CurrentConditionsResponse
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigSubentry as ConfigSubentry
from homeassistant.const import DEGREE as DEGREE, PERCENTAGE as PERCENTAGE, UV_INDEX as UV_INDEX, UnitOfLength as UnitOfLength, UnitOfPressure as UnitOfPressure, UnitOfSpeed as UnitOfSpeed, UnitOfTemperature as UnitOfTemperature, UnitOfVolumetricFlux as UnitOfVolumetricFlux
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class GoogleWeatherSensorDescription(SensorEntityDescription):
    value_fn: Callable[[CurrentConditionsResponse], str | int | float | None]

SENSOR_TYPES: tuple[GoogleWeatherSensorDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: GoogleWeatherConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class GoogleWeatherSensor(CoordinatorEntity[GoogleWeatherCurrentConditionsCoordinator], GoogleWeatherBaseEntity, SensorEntity):
    entity_description: GoogleWeatherSensorDescription
    def __init__(self, coordinator: GoogleWeatherCurrentConditionsCoordinator, subentry: ConfigSubentry, description: GoogleWeatherSensorDescription) -> None: ...
    @property
    def native_value(self) -> str | int | float | None: ...
