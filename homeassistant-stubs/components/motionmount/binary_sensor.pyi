import motionmount
from . import MotionMountConfigEntry as MotionMountConfigEntry
from .entity import MotionMountEntity as MotionMountEntity
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: MotionMountConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class MotionMountMovingSensor(MotionMountEntity, BinarySensorEntity):
    _attr_device_class: Incomplete
    _attr_translation_key: str
    _attr_entity_category: Incomplete
    _attr_entity_registry_enabled_default: bool
    _attr_unique_id: Incomplete
    def __init__(self, mm: motionmount.MotionMount, config_entry: MotionMountConfigEntry) -> None: ...
    @property
    def is_on(self) -> bool: ...
