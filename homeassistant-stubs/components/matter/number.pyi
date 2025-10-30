from .entity import MatterEntity as MatterEntity, MatterEntityDescription as MatterEntityDescription
from .helpers import get_matter as get_matter
from .models import MatterDiscoverySchema as MatterDiscoverySchema
from _typeshed import Incomplete
from chip.clusters.ClusterObjects import ClusterAttributeDescriptor as ClusterAttributeDescriptor, ClusterCommand as ClusterCommand
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.number import NumberDeviceClass as NumberDeviceClass, NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription, NumberMode as NumberMode
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, Platform as Platform, UnitOfLength as UnitOfLength, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

@dataclass(frozen=True, kw_only=True)
class MatterNumberEntityDescription(NumberEntityDescription, MatterEntityDescription): ...

@dataclass(frozen=True, kw_only=True)
class MatterRangeNumberEntityDescription(NumberEntityDescription, MatterEntityDescription):
    ha_to_device: Callable[[Any], Any] = ...
    min_attribute: type[ClusterAttributeDescriptor] | None = ...
    max_attribute: type[ClusterAttributeDescriptor]
    format_min_value: Callable[[float], float] = ...
    format_max_value: Callable[[float], float] = ...
    command: Callable[[int], ClusterCommand]

class MatterNumber(MatterEntity, NumberEntity):
    entity_description: MatterNumberEntityDescription
    async def async_set_native_value(self, value: float) -> None: ...
    _attr_native_value: Incomplete
    @callback
    def _update_from_device(self) -> None: ...

class MatterRangeNumber(MatterEntity, NumberEntity):
    entity_description: MatterRangeNumberEntityDescription
    async def async_set_native_value(self, value: float) -> None: ...
    _attr_native_value: Incomplete
    _attr_native_min_value: Incomplete
    _attr_native_max_value: Incomplete
    @callback
    def _update_from_device(self) -> None: ...

class MatterLevelControlNumber(MatterEntity, NumberEntity):
    entity_description: MatterNumberEntityDescription
    async def async_set_native_value(self, value: float) -> None: ...
    _attr_native_value: Incomplete
    @callback
    def _update_from_device(self) -> None: ...

DISCOVERY_SCHEMAS: Incomplete
