from .coordinator import AladdinConnectConfigEntry as AladdinConnectConfigEntry, AladdinConnectCoordinator as AladdinConnectCoordinator
from .entity import AladdinConnectEntity as AladdinConnectEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from genie_partner_sdk.model import GarageDoor as GarageDoor
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

@dataclass(frozen=True, kw_only=True)
class AladdinConnectSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[GarageDoor], float | None]

SENSOR_TYPES: tuple[AladdinConnectSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: AladdinConnectConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class AladdinConnectSensor(AladdinConnectEntity, SensorEntity):
    entity_description: AladdinConnectSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: AladdinConnectCoordinator, entity_description: AladdinConnectSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> float | None: ...
