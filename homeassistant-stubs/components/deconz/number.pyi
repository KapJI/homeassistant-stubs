from .entity import DeconzDevice as DeconzDevice
from .hub import DeconzHub as DeconzHub
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.number import DOMAIN as NUMBER_DOMAIN, NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pydeconz.gateway import DeconzSession as DeconzSession
from pydeconz.interfaces.sensors import SensorResources
from pydeconz.models.event import EventType as EventType
from typing import Any

@dataclass(frozen=True, kw_only=True)
class DeconzNumberDescription(NumberEntityDescription):
    instance_check: type[_T]
    name_suffix: str
    set_fn: Callable[[DeconzSession, str, int], Coroutine[Any, Any, dict[str, Any]]]
    update_key: str
    value_fn: Callable[[_T], float | None]
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., max_value=..., min_value=..., mode=..., native_max_value=..., native_min_value=..., native_step=..., native_unit_of_measurement=..., step=..., instance_check, name_suffix, set_fn, update_key, value_fn) -> None: ...

ENTITY_DESCRIPTIONS: tuple[DeconzNumberDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DeconzNumber(DeconzDevice[SensorResources], NumberEntity):
    TYPE = NUMBER_DOMAIN
    entity_description: DeconzNumberDescription
    unique_id_suffix: Incomplete
    _name_suffix: Incomplete
    _update_key: Incomplete
    def __init__(self, device: SensorResources, hub: DeconzHub, description: DeconzNumberDescription) -> None: ...
    @property
    def native_value(self) -> float | None: ...
    async def async_set_native_value(self, value: float) -> None: ...
