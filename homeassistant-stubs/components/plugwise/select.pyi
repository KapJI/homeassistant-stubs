from .const import DOMAIN as DOMAIN
from .coordinator import PlugwiseDataUpdateCoordinator as PlugwiseDataUpdateCoordinator
from .entity import PlugwiseEntity as PlugwiseEntity
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from plugwise import Smile as Smile
from plugwise.constants import SelectOptionsType as SelectOptionsType, SelectType as SelectType

@dataclass
class PlugwiseSelectDescriptionMixin:
    command: Callable[[Smile, str, str], Awaitable[None]]
    options_key: SelectOptionsType
    def __init__(self, command, options_key) -> None: ...

@dataclass
class PlugwiseSelectEntityDescription(SelectEntityDescription, PlugwiseSelectDescriptionMixin):
    key: SelectType
    def __init__(self, command, options_key, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, options) -> None: ...

SELECT_TYPES: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PlugwiseSelectEntity(PlugwiseEntity, SelectEntity):
    entity_description: PlugwiseSelectEntityDescription
    _attr_unique_id: Incomplete
    _attr_options: Incomplete
    def __init__(self, coordinator: PlugwiseDataUpdateCoordinator, device_id: str, entity_description: PlugwiseSelectEntityDescription) -> None: ...
    @property
    def current_option(self) -> str: ...
    async def async_select_option(self, option: str) -> None: ...
