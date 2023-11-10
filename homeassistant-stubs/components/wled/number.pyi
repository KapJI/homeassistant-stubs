from .const import ATTR_INTENSITY as ATTR_INTENSITY, ATTR_SPEED as ATTR_SPEED, DOMAIN as DOMAIN
from .coordinator import WLEDDataUpdateCoordinator as WLEDDataUpdateCoordinator
from .helpers import wled_exception_handler as wled_exception_handler
from .models import WLEDEntity as WLEDEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.number import NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from wled import Segment as Segment

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

@dataclass
class WLEDNumberDescriptionMixin:
    value_fn: Callable[[Segment], float | None]
    def __init__(self, value_fn) -> None: ...

@dataclass
class WLEDNumberEntityDescription(NumberEntityDescription, WLEDNumberDescriptionMixin):
    def __init__(self, value_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, max_value, min_value, mode, native_max_value, native_min_value, native_step, native_unit_of_measurement, step) -> None: ...

NUMBERS: Incomplete

class WLEDNumber(WLEDEntity, NumberEntity):
    entity_description: WLEDNumberEntityDescription
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _segment: Incomplete
    def __init__(self, coordinator: WLEDDataUpdateCoordinator, segment: int, description: WLEDNumberEntityDescription) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def native_value(self) -> float | None: ...
    async def async_set_native_value(self, value: float) -> None: ...

def async_update_segments(coordinator: WLEDDataUpdateCoordinator, current_ids: set[int], async_add_entities: AddEntitiesCallback) -> None: ...
