from . import get_device_info as get_device_info
from .const import ATTRIBUTION as ATTRIBUTION, CONDITION_MAP as CONDITION_MAP, DOMAIN as DOMAIN, METOFFICE_COORDINATES as METOFFICE_COORDINATES, METOFFICE_HOURLY_COORDINATOR as METOFFICE_HOURLY_COORDINATOR, METOFFICE_NAME as METOFFICE_NAME
from .helpers import get_attribute as get_attribute
from _typeshed import Incomplete
from dataclasses import dataclass
from datapoint.Forecast import Forecast
from homeassistant.components.sensor import EntityCategory as EntityCategory, SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import DEGREE as DEGREE, PERCENTAGE as PERCENTAGE, UV_INDEX as UV_INDEX, UnitOfLength as UnitOfLength, UnitOfSpeed as UnitOfSpeed, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

ATTR_LAST_UPDATE: str

@dataclass(frozen=True, kw_only=True)
class MetOfficeSensorEntityDescription(SensorEntityDescription):
    native_attr_name: str

SENSOR_TYPES: tuple[MetOfficeSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class MetOfficeCurrentSensor(CoordinatorEntity[DataUpdateCoordinator[Forecast]], SensorEntity):
    _attr_attribution = ATTRIBUTION
    _attr_has_entity_name: bool
    entity_description: MetOfficeSensorEntityDescription
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: DataUpdateCoordinator[Forecast], hass_data: dict[str, Any], description: MetOfficeSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
    @property
    def icon(self) -> str | None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
