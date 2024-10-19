from .entity import MatterEntity as MatterEntity, MatterEntityDescription as MatterEntityDescription
from .helpers import get_matter as get_matter
from .models import MatterDiscoverySchema as MatterDiscoverySchema
from _typeshed import Incomplete
from chip.clusters.Types import Nullable as Nullable
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

@dataclass(frozen=True)
class MatterSelectEntityDescription(SelectEntityDescription, MatterEntityDescription):
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., measurement_to_ha=..., ha_to_native_value=..., options=...) -> None: ...

class MatterSelectEntity(MatterEntity, SelectEntity):
    entity_description: MatterSelectEntityDescription
    async def async_select_option(self, option: str) -> None: ...
    _attr_current_option: Incomplete
    def _update_from_device(self) -> None: ...

class MatterModeSelectEntity(MatterSelectEntity):
    async def async_select_option(self, option: str) -> None: ...
    _attr_options: Incomplete
    _attr_current_option: Incomplete
    _attr_name: Incomplete
    def _update_from_device(self) -> None: ...

DISCOVERY_SCHEMAS: Incomplete
