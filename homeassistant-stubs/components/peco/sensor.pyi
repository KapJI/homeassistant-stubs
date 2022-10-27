from . import PECOCoordinatorData as PECOCoordinatorData
from .const import ATTR_CONTENT as ATTR_CONTENT, CONF_COUNTY as CONF_COUNTY, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from typing import Final

class PECOSensorEntityDescriptionMixin:
    value_fn: Callable[[PECOCoordinatorData], Union[int, str]]
    attribute_fn: Callable[[PECOCoordinatorData], dict[str, str]]
    def __init__(self, value_fn, attribute_fn) -> None: ...

class PECOSensorEntityDescription(SensorEntityDescription, PECOSensorEntityDescriptionMixin):
    def __init__(self, value_fn, attribute_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, unit_of_measurement, suggested_unit_of_measurement, last_reset, native_unit_of_measurement, state_class) -> None: ...

PARALLEL_UPDATES: Final[int]
SENSOR_LIST: tuple[PECOSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PecoSensor(CoordinatorEntity[DataUpdateCoordinator[PECOCoordinatorData]], SensorEntity):
    entity_description: PECOSensorEntityDescription
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, description: PECOSensorEntityDescription, county: str, coordinator: DataUpdateCoordinator[PECOCoordinatorData]) -> None: ...
    @property
    def native_value(self) -> Union[int, str]: ...
    @property
    def extra_state_attributes(self) -> dict[str, str]: ...
