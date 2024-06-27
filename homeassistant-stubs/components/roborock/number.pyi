from . import RoborockCoordinators as RoborockCoordinators
from .const import DOMAIN as DOMAIN
from .coordinator import RoborockDataUpdateCoordinator as RoborockDataUpdateCoordinator
from .device import RoborockEntityV1 as RoborockEntityV1
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.number import NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util import slugify as slugify
from roborock.command_cache import CacheableAttribute
from roborock.version_1_apis.roborock_client_v1 import AttributeCache as AttributeCache
from typing import Any

_LOGGER: Incomplete

@dataclass(frozen=True, kw_only=True)
class RoborockNumberDescription(NumberEntityDescription):
    cache_key: CacheableAttribute
    update_value: Callable[[AttributeCache, float], Coroutine[Any, Any, None]]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, max_value, min_value, mode, native_max_value, native_min_value, native_step, native_unit_of_measurement, step, cache_key, update_value) -> None: ...

NUMBER_DESCRIPTIONS: list[RoborockNumberDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RoborockNumberEntity(RoborockEntityV1, NumberEntity):
    entity_description: RoborockNumberDescription
    def __init__(self, unique_id: str, coordinator: RoborockDataUpdateCoordinator, entity_description: RoborockNumberDescription) -> None: ...
    @property
    def native_value(self) -> float | None: ...
    async def async_set_native_value(self, value: float) -> None: ...
