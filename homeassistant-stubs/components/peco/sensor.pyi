from .const import CONF_COUNTY as CONF_COUNTY, DOMAIN as DOMAIN
from collections.abc import Callable as Callable
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from peco import OutageResults
from typing import Any, Final

class PECOSensorEntityDescriptionMixin:
    value_fn: Callable[[OutageResults], int]
    def __init__(self, value_fn) -> None: ...

class PECOSensorEntityDescription(SensorEntityDescription, PECOSensorEntityDescriptionMixin):
    def __init__(self, value_fn, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement, last_reset, native_unit_of_measurement, state_class) -> None: ...

PARALLEL_UPDATES: Final[int]
SENSOR_LIST: tuple[PECOSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PecoSensor(CoordinatorEntity[DataUpdateCoordinator[OutageResults]], SensorEntity):
    _attr_state_class: Any
    _attr_icon: str
    entity_description: PECOSensorEntityDescription
    _attr_name: Any
    _attr_unique_id: Any
    def __init__(self, description: PECOSensorEntityDescription, county: str, coordinator: DataUpdateCoordinator[OutageResults]) -> None: ...
    @property
    def native_value(self) -> int: ...
