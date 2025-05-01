from .coordinator import ComelitConfigEntry as ComelitConfigEntry, ComelitVedoSystem as ComelitVedoSystem
from _typeshed import Incomplete
from aiocomelit import ComelitVedoZoneObject as ComelitVedoZoneObject
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: ComelitConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ComelitVedoBinarySensorEntity(CoordinatorEntity[ComelitVedoSystem], BinarySensorEntity):
    _attr_has_entity_name: bool
    _attr_device_class: Incomplete
    _zone_index: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: ComelitVedoSystem, zone: ComelitVedoZoneObject, config_entry_entry_id: str) -> None: ...
    @property
    def is_on(self) -> bool: ...
