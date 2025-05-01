from .entity import MatterEntity as MatterEntity, MatterEntityDescription as MatterEntityDescription
from .helpers import get_matter as get_matter
from .models import MatterDiscoverySchema as MatterDiscoverySchema
from _typeshed import Incomplete
from chip.clusters import Objects as clusters
from chip.clusters.ClusterObjects import ClusterAttributeDescriptor as ClusterAttributeDescriptor, ClusterCommand as ClusterCommand
from chip.clusters.Types import Nullable as Nullable
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

NUMBER_OF_RINSES_STATE_MAP: Incomplete
NUMBER_OF_RINSES_STATE_MAP_REVERSE: Incomplete
type SelectCluster = clusters.ModeSelect | clusters.OvenMode | clusters.LaundryWasherMode | clusters.RefrigeratorAndTemperatureControlledCabinetMode | clusters.RvcRunMode | clusters.RvcCleanMode | clusters.DishwasherMode | clusters.EnergyEvseMode | clusters.DeviceEnergyManagementMode | clusters.WaterHeaterMode

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

@dataclass(frozen=True)
class MatterSelectEntityDescription(SelectEntityDescription, MatterEntityDescription): ...

@dataclass(frozen=True, kw_only=True)
class MatterMapSelectEntityDescription(MatterSelectEntityDescription):
    measurement_to_ha: Callable[[int], str | None]
    ha_to_native_value: Callable[[str], int | None]
    list_attribute: type[ClusterAttributeDescriptor]

@dataclass(frozen=True, kw_only=True)
class MatterListSelectEntityDescription(MatterSelectEntityDescription):
    list_attribute: type[ClusterAttributeDescriptor]
    command: Callable[[int], ClusterCommand] | None = ...

class MatterAttributeSelectEntity(MatterEntity, SelectEntity):
    entity_description: MatterSelectEntityDescription
    async def async_select_option(self, option: str) -> None: ...
    _attr_current_option: Incomplete
    @callback
    def _update_from_device(self) -> None: ...

class MatterMapSelectEntity(MatterAttributeSelectEntity):
    entity_description: MatterMapSelectEntityDescription
    _attr_options: Incomplete
    @callback
    def _update_from_device(self) -> None: ...

class MatterModeSelectEntity(MatterAttributeSelectEntity):
    async def async_select_option(self, option: str) -> None: ...
    _attr_options: Incomplete
    _attr_current_option: Incomplete
    _attr_name: Incomplete
    @callback
    def _update_from_device(self) -> None: ...

class MatterListSelectEntity(MatterEntity, SelectEntity):
    entity_description: MatterListSelectEntityDescription
    async def async_select_option(self, option: str) -> None: ...
    _attr_options: Incomplete
    _attr_current_option: Incomplete
    @callback
    def _update_from_device(self) -> None: ...

DISCOVERY_SCHEMAS: Incomplete
