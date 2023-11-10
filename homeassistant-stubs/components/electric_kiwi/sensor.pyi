from .const import ATTRIBUTION as ATTRIBUTION, DOMAIN as DOMAIN
from .coordinator import ElectricKiwiHOPDataCoordinator as ElectricKiwiHOPDataCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from electrickiwi_api.model import Hop as Hop
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

_LOGGER: Incomplete
ATTR_EK_HOP_START: str
ATTR_EK_HOP_END: str

@dataclass
class ElectricKiwiHOPRequiredKeysMixin:
    value_func: Callable[[Hop], datetime]
    def __init__(self, value_func) -> None: ...

@dataclass
class ElectricKiwiHOPSensorEntityDescription(SensorEntityDescription, ElectricKiwiHOPRequiredKeysMixin):
    def __init__(self, value_func, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement) -> None: ...

def _check_and_move_time(hop: Hop, time: str) -> datetime: ...

HOP_SENSOR_TYPES: tuple[ElectricKiwiHOPSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ElectricKiwiHOPEntity(CoordinatorEntity[ElectricKiwiHOPDataCoordinator], SensorEntity):
    entity_description: ElectricKiwiHOPSensorEntityDescription
    _attr_has_entity_name: bool
    _attr_attribution = ATTRIBUTION
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: ElectricKiwiHOPDataCoordinator, description: ElectricKiwiHOPSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> datetime: ...
