import motionmount
from . import MotionMountConfigEntry as MotionMountConfigEntry
from .entity import MotionMountEntity as MotionMountEntity
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Final

PARALLEL_UPDATES: int
ERROR_MESSAGES: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, entry: MotionMountConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class MotionMountErrorStatusSensor(MotionMountEntity, SensorEntity):
    _attr_device_class: Incomplete
    _attr_options: Incomplete
    _attr_translation_key: str
    _attr_entity_category: Incomplete
    _attr_entity_registry_enabled_default: bool
    _attr_unique_id: Incomplete
    def __init__(self, mm: motionmount.MotionMount, config_entry: MotionMountConfigEntry) -> None: ...
    @property
    def native_value(self) -> str: ...
