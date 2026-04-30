from .const import ObjectClassType as ObjectClassType
from .coordinator import ComelitConfigEntry as ComelitConfigEntry, ComelitSerialBridge as ComelitSerialBridge, ComelitVedoSystem as ComelitVedoSystem
from .utils import new_device_listener as new_device_listener
from _typeshed import Incomplete
from aiocomelit.api import ComelitVedoAreaObject, ComelitVedoZoneObject
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Final

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class ComelitBinarySensorEntityDescription(BinarySensorEntityDescription):
    object_type: str
    is_on_fn: Callable[[ComelitVedoAreaObject | ComelitVedoZoneObject], bool]
    available_fn: Callable[[ComelitVedoAreaObject | ComelitVedoZoneObject], bool] = ...

BINARY_SENSOR_TYPES: Final[tuple[ComelitBinarySensorEntityDescription, ...]]

async def async_setup_entry(hass: HomeAssistant, config_entry: ComelitConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ComelitVedoBinarySensorEntity(CoordinatorEntity[ComelitVedoSystem | ComelitSerialBridge], BinarySensorEntity):
    entity_description: ComelitBinarySensorEntityDescription
    _attr_has_entity_name: bool
    _object_index: Incomplete
    _object_type: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: ComelitVedoSystem | ComelitSerialBridge, object_data: ComelitVedoAreaObject | ComelitVedoZoneObject, config_entry_entry_id: str, description: ComelitBinarySensorEntityDescription) -> None: ...
    @property
    def _object(self) -> ComelitVedoAreaObject | ComelitVedoZoneObject: ...
    @property
    def available(self) -> bool: ...
    @property
    def is_on(self) -> bool: ...
