from .coordinator import InComfortConfigEntry as InComfortConfigEntry, InComfortDataCoordinator as InComfortDataCoordinator
from .entity import IncomfortBoilerEntity as IncomfortBoilerEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from incomfortclient import Heater as InComfortHeater
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class IncomfortBinarySensorEntityDescription(BinarySensorEntityDescription):
    value_key: str
    extra_state_attributes_fn: Callable[[dict[str, Any]], dict[str, Any]] | None = ...
    entity_category: EntityCategory = ...

SENSOR_TYPES: tuple[IncomfortBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: InComfortConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class IncomfortBinarySensor(IncomfortBoilerEntity, BinarySensorEntity):
    entity_description: IncomfortBinarySensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: InComfortDataCoordinator, heater: InComfortHeater, description: IncomfortBinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any] | None: ...
