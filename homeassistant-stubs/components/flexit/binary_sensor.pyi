from .coordinator import FlexitConfigEntry as FlexitConfigEntry, FlexitDataCoordinator as FlexitDataCoordinator
from .entity import FlexitEntity as FlexitEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from flexit_modbus import Measurements as Measurements
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

@dataclass(kw_only=True, frozen=True)
class FlexitBinarySensorEntityDescription(BinarySensorEntityDescription):
    value_fn: Callable[[Measurements], bool | None]

BINARY_SENSORS: tuple[FlexitBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: FlexitConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class FlexitBinarySensor(FlexitEntity, BinarySensorEntity):
    entity_description: FlexitBinarySensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: FlexitDataCoordinator, entity_description: FlexitBinarySensorEntityDescription) -> None: ...
    @property
    @override
    def is_on(self) -> bool | None: ...
