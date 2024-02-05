from .const import DOMAIN as DOMAIN
from .controller import EcovacsController as EcovacsController
from .entity import EcovacsCapabilityEntityDescription as EcovacsCapabilityEntityDescription, EcovacsDescriptionEntity as EcovacsDescriptionEntity, EcovacsEntity as EcovacsEntity, EventT as EventT
from .util import get_supported_entitites as get_supported_entitites
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from deebot_client.capabilities import CapabilitySet
from homeassistant.components.number import NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Generic

@dataclass(kw_only=True, frozen=True)
class EcovacsNumberEntityDescription(NumberEntityDescription, EcovacsCapabilityEntityDescription, Generic[EventT]):
    native_max_value_fn: Callable[[EventT], float | int | None] = ...
    value_fn: Callable[[EventT], float | None]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, capability_fn, max_value, min_value, mode, native_max_value, native_min_value, native_step, native_unit_of_measurement, step, native_max_value_fn, value_fn) -> None: ...

ENTITY_DESCRIPTIONS: tuple[EcovacsNumberEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class EcovacsNumberEntity(EcovacsDescriptionEntity[CapabilitySet[EventT, int]], NumberEntity):
    entity_description: EcovacsNumberEntityDescription
    _attr_native_value: Incomplete
    _attr_native_max_value: Incomplete
    async def async_added_to_hass(self) -> None: ...
    async def async_set_native_value(self, value: float) -> None: ...
