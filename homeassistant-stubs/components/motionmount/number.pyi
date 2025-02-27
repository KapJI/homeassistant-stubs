import motionmount
from . import MotionMountConfigEntry as MotionMountConfigEntry
from .const import DOMAIN as DOMAIN
from .entity import MotionMountEntity as MotionMountEntity
from _typeshed import Incomplete
from homeassistant.components.number import NumberEntity as NumberEntity
from homeassistant.const import PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: MotionMountConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class MotionMountExtension(MotionMountEntity, NumberEntity):
    _attr_native_max_value: int
    _attr_native_min_value: int
    _attr_native_unit_of_measurement = PERCENTAGE
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    def __init__(self, mm: motionmount.MotionMount, config_entry: MotionMountConfigEntry) -> None: ...
    @property
    def native_value(self) -> float: ...
    async def async_set_native_value(self, value: float) -> None: ...

class MotionMountTurn(MotionMountEntity, NumberEntity):
    _attr_native_max_value: int
    _attr_native_min_value: int
    _attr_native_unit_of_measurement = PERCENTAGE
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    def __init__(self, mm: motionmount.MotionMount, config_entry: MotionMountConfigEntry) -> None: ...
    @property
    def native_value(self) -> float: ...
    async def async_set_native_value(self, value: float) -> None: ...
