import datetime
from . import RoborockCoordinators as RoborockCoordinators
from .const import DOMAIN as DOMAIN
from .coordinator import RoborockDataUpdateCoordinator as RoborockDataUpdateCoordinator
from .device import RoborockEntityV1 as RoborockEntityV1
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from datetime import time
from homeassistant.components.time import TimeEntity as TimeEntity, TimeEntityDescription as TimeEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util import slugify as slugify
from roborock.command_cache import CacheableAttribute
from roborock.version_1_apis.roborock_client_v1 import AttributeCache as AttributeCache
from typing import Any

_LOGGER: Incomplete

@dataclass(frozen=True, kw_only=True)
class RoborockTimeDescription(TimeEntityDescription):
    cache_key: CacheableAttribute
    update_value: Callable[[AttributeCache, datetime.time], Coroutine[Any, Any, None]]
    get_value: Callable[[AttributeCache], datetime.time]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, cache_key, update_value, get_value) -> None: ...

TIME_DESCRIPTIONS: list[RoborockTimeDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RoborockTimeEntity(RoborockEntityV1, TimeEntity):
    entity_description: RoborockTimeDescription
    def __init__(self, unique_id: str, coordinator: RoborockDataUpdateCoordinator, entity_description: RoborockTimeDescription) -> None: ...
    @property
    def native_value(self) -> time | None: ...
    async def async_set_value(self, value: time) -> None: ...
