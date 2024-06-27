from . import PlugwiseConfigEntry as PlugwiseConfigEntry
from .const import LOCATION as LOCATION, SelectOptionsType as SelectOptionsType, SelectType as SelectType
from .coordinator import PlugwiseDataUpdateCoordinator as PlugwiseDataUpdateCoordinator
from .entity import PlugwiseEntity as PlugwiseEntity
from .util import plugwise_command as plugwise_command
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

@dataclass(frozen=True, kw_only=True)
class PlugwiseSelectEntityDescription(SelectEntityDescription):
    key: SelectType
    options_key: SelectOptionsType
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, options, options_key) -> None: ...

SELECT_TYPES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: PlugwiseConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PlugwiseSelectEntity(PlugwiseEntity, SelectEntity):
    entity_description: PlugwiseSelectEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: PlugwiseDataUpdateCoordinator, device_id: str, entity_description: PlugwiseSelectEntityDescription) -> None: ...
    @property
    def current_option(self) -> str: ...
    @property
    def options(self) -> list[str]: ...
    async def async_select_option(self, option: str) -> None: ...
