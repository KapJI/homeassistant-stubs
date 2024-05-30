from . import TVWeatherConfigEntry as TVWeatherConfigEntry
from .const import ATTRIBUTION as ATTRIBUTION, CONF_STATION as CONF_STATION, DOMAIN as DOMAIN
from .coordinator import TVDataUpdateCoordinator as TVDataUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import DEGREE as DEGREE, PERCENTAGE as PERCENTAGE, UnitOfLength as UnitOfLength, UnitOfSpeed as UnitOfSpeed, UnitOfTemperature as UnitOfTemperature, UnitOfVolumetricFlux as UnitOfVolumetricFlux
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from pytrafikverket.trafikverket_weather import WeatherStationInfo as WeatherStationInfo

PRECIPITATION_TYPE: Incomplete

@dataclass(frozen=True, kw_only=True)
class TrafikverketSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[WeatherStationInfo], StateType | datetime]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, value_fn) -> None: ...

def add_utc_timezone(date_time: datetime | None) -> datetime | None: ...

SENSOR_TYPES: tuple[TrafikverketSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: TVWeatherConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TrafikverketWeatherStation(CoordinatorEntity[TVDataUpdateCoordinator], SensorEntity):
    entity_description: TrafikverketSensorEntityDescription
    _attr_attribution = ATTRIBUTION
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: TVDataUpdateCoordinator, entry_id: str, sensor_station: str, description: TrafikverketSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType | datetime: ...
