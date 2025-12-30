from .const import ObjectClassType as ObjectClassType
from .coordinator import ComelitConfigEntry as ComelitConfigEntry, ComelitSerialBridge as ComelitSerialBridge, ComelitVedoSystem as ComelitVedoSystem
from .utils import new_device_listener as new_device_listener
from _typeshed import Incomplete
from aiocomelit.api import ComelitVedoZoneObject
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: ComelitConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ComelitVedoBinarySensorEntity(CoordinatorEntity[ComelitVedoSystem | ComelitSerialBridge], BinarySensorEntity):
    _attr_has_entity_name: bool
    _attr_device_class: Incomplete
    _zone_index: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: ComelitVedoSystem | ComelitSerialBridge, zone: ComelitVedoZoneObject, config_entry_entry_id: str) -> None: ...
    @property
    def _zone(self) -> ComelitVedoZoneObject: ...
    @property
    def available(self) -> bool: ...
    @property
    def is_on(self) -> bool: ...
