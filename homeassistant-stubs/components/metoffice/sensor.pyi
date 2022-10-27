from . import get_device_info as get_device_info
from .const import ATTRIBUTION as ATTRIBUTION, CONDITION_CLASSES as CONDITION_CLASSES, DOMAIN as DOMAIN, METOFFICE_COORDINATES as METOFFICE_COORDINATES, METOFFICE_DAILY_COORDINATOR as METOFFICE_DAILY_COORDINATOR, METOFFICE_HOURLY_COORDINATOR as METOFFICE_HOURLY_COORDINATOR, METOFFICE_NAME as METOFFICE_NAME, MODE_DAILY as MODE_DAILY, VISIBILITY_CLASSES as VISIBILITY_CLASSES, VISIBILITY_DISTANCE_CLASSES as VISIBILITY_DISTANCE_CLASSES
from .data import MetOfficeData as MetOfficeData
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import LENGTH_KILOMETERS as LENGTH_KILOMETERS, PERCENTAGE as PERCENTAGE, SPEED_MILES_PER_HOUR as SPEED_MILES_PER_HOUR, TEMP_CELSIUS as TEMP_CELSIUS, UV_INDEX as UV_INDEX
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

ATTR_LAST_UPDATE: str
ATTR_SENSOR_ID: str
ATTR_SITE_ID: str
ATTR_SITE_NAME: str
SENSOR_TYPES: tuple[SensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MetOfficeCurrentSensor(CoordinatorEntity[DataUpdateCoordinator[MetOfficeData]], SensorEntity):
    _attr_attribution: Incomplete
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_device_info: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_entity_registry_enabled_default: Incomplete
    def __init__(self, coordinator: DataUpdateCoordinator[MetOfficeData], hass_data: dict[str, Any], use_3hourly: bool, description: SensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> Union[Any, None]: ...
    @property
    def icon(self) -> Union[str, None]: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
