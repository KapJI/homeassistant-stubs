from . import AladdinConnectConfigEntry as AladdinConnectConfigEntry, AladdinConnectCoordinator as AladdinConnectCoordinator
from .entity import AladdinConnectEntity as AladdinConnectEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

@dataclass(frozen=True, kw_only=True)
class AccSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[AladdinConnectClient, str, int], float | None]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, value_fn) -> None: ...

SENSORS: tuple[AccSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: AladdinConnectConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AladdinConnectSensor(AladdinConnectEntity, SensorEntity):
    entity_description: AccSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: AladdinConnectCoordinator, device: GarageDoor, description: AccSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> float | None: ...
