from .coordinator import FlexitConfigEntry as FlexitConfigEntry, FlexitCoordinator as FlexitCoordinator
from .entity import FlexitEntity as FlexitEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from flexit_bacnet import FlexitBACnet as FlexitBACnet
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

@dataclass(kw_only=True, frozen=True)
class FlexitBinarySensorEntityDescription(BinarySensorEntityDescription):
    value_fn: Callable[[FlexitBACnet], bool]

SENSOR_TYPES: tuple[FlexitBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: FlexitConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

PARALLEL_UPDATES: int

class FlexitBinarySensor(FlexitEntity, BinarySensorEntity):
    entity_description: FlexitBinarySensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: FlexitCoordinator, entity_description: FlexitBinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
